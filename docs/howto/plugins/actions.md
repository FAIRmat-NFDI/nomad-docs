# How to define actions

Actions allow to define executable workflows in NOMAD. They provide an
alternative to entry normalize methods and are well-suited for setting up
long-running workflows, like running training and inferring ML models, or
workflows that need to interact with external APIs. Dedicated
workers can be configured to manage workflows, allowing targeted allocation of
resources like GPUs for specific tasks.

This documentation shows you how to write a plugin entry point for an action.
You should read the [introduction to plugins](./plugins.md)
to have a basic understanding of how plugins and plugin entry points work in the NOMAD ecosystem.

## Getting started

You can use our [template repository](https://github.com/FAIRmat-NFDI/nomad-plugin-template) to
create an initial structure for a plugin containing an action.
The relevant part of the repository layout will look something like this:

```txt
nomad-example
   ├── src
   │   ├── nomad_example
   │   │   ├── actions
   │   │   │   ├── __init__.py
   │   │   │   ├── activities.py
   │   │   │   ├── workflows.py
   │   │   │   ├── models.py
   ├── LICENSE.txt
   ├── README.md
   └── pyproject.toml
```

See the documentation on [plugin development guidelines](./plugins.md#plugin-development-guidelines)
for more details on the best development practices for plugins, including linting, testing and documenting.

## Action entry point

The entry point defines basic information about your action and is used to
automatically load it into a NOMAD distribution. It is an instance of a
`ActionEntryPoint` or its subclass and it contains a `load` method which
returns a `nomad.orchestrator.base.ActionHandler` instance that contains the
definition of the workflows and activities, along with the task queue to be
used for this Action. You will learn more about
`ActionHandler` class in the next sections. The entry point should be defined
in `*/actions/__init__.py` like this:

```py
from nomad.config.models.plugins import ActionEntryPoint


class MyActionEntryPoint(ActionEntryPoint):

    def load(self):
        from nomad.orchestrator.base import ActionHandler
        from nomad.orchestrator.shared.constant import TaskQueue

        from nomad_example.actions.workflows import ExampleWorkflow
        from nomad_example.actions.activities import get_request

        return ActionHandler(
            workflows=[ExampleWorkflow],
            activities=[get_request],
            task_queue=TaskQueue.CPU
        )


myaction = MyActionEntryPoint(
    name='MyAction',
    description='My custom action.',
)
```

Here you can see that a new subclass of `MyActionEntryPoint` was defined. In
this new class you can override the `load` method to determine how the
`ActionHandler` class is loaded, but you can also extend the
`ActionEntryPoint` model to add new configurable parameters for this schema
package as explained [here](../../explanation/plugin_system.
md#plugin-configuration).

We also instantiate an object `myaction` from the new subclass. This is the
final entry point instance in which you specify the default parameterization
and other details about the action. In the reference you can see all of the
available
[configuration options for a `ActionEntryPoint`](../../reference/plugins.
md#actionentrypoint).

The entry point instance should then be added to the `[project.entry-points.
'nomad.plugin']` table in `pyproject.toml` in order for it to be automatically
detected:

```toml
[project.entry-points.'nomad.plugin']
myaction = "nomad_example.actions:myaction"
```

## `ActionHandler` class

The `load`-method of an action entry point returns an instance of a
`nomad.orchestrator.base.ActionHandler` class which describes the action through
a collection of activities and a workflow that connects them. We use
[Temporal](https://docs.temporal.io/temporal)'s workflow-activity
abstraction here.

Activities are the atomic unit of execution. They should ideally be defined as
[idempotent](https://docs.temporal.io/activity-definition#idempotency),
allowing Temporal to retry automatically based on a policy until the activity
is successfully completed. For example, an idempotent activity that gets data
from an external resource via API will keep retrying until a status
code 200 (successful response) is achieved. Workflow defines a sequence of
activities and flow of data from one activity to another.

You can add these definitions in `*/actions/activities.py` and
`*/actions/workflows.py`. Temporal requires the input and output of the
activities and workflows to be serializable. We recommend defining Pydantic models for them in `*/actions/models.py`. These files could look like this:

**nomad_example/actions/models.py**

```py

from pydantic import BaseModel, Field
from nomad.orchestrator.workflows.models import BaseWorkflowInput


class ExampleWorkflowInput(BaseWorkflowInput):
    cid: int = Field(
        ..., description='PubChem compound identifier for a chemical compound.'
    )


class GetRequestInput(BaseModel):
    url: str = Field(..., description='URL for get request.')
    timeout: int = Field(..., description='Timeout for the request.')

```

Here we extend `BaseWorkflowInput` for defining the input model
of the workflow and simply extend `BaseModel` class from
Pydantic to define the input model of the activity.

!!! important
    We strongly recommend to extend the Pydantic base model `nomad.orchestrator
    models.BaseWorkflowInput` to define the input model for your workflow. It
    provides additional fields like `user_id` and `upload_id` which are
    required to execute a workflow in NOMAD. If the input to your workflows
    running on `GPU` and `CPU` task queues does not include these fields, the
    workflow will fail.

**nomad_example/actions/activities.py**

```py
from temporalio import activity

from nomad_example.actions.workflows.models import GetRequestInput


@activity.defn
async def get_request(data: GetRequestInput):
    """
    Perform a GET request to the specified URL with the provided timeout.
    """
    import aiohttp

    async with aiohttp.ClientSession() as session:
        async with session.get(
            data.url,
            timeout=data.timeout,
        ) as response:
            if response.status != 200:
                raise ValueError(
                    f'GET request failed with status {response.status}'
                )
            return await response.json()

```

Here we define an activity by using the Temporal decorator `activity.defn` on
the `get_request` function. The activity interacts with an external API
asynchronously. Non-blocking activities allow Temporal to efficiently manage
the task queues, handling multiple workflows at once. We use `GetRequestInput`
model to define the argument of this activity.

**nomad_example/actions/workflows.py**

```py
from datetime import timedelta

from temporalio import workflow
from temporalio.common import RetryPolicy

with workflow.unsafe.imports_passed_through():
    from nomad.orchestrator import BaseWorkflow
    from nomad_example.actions.workflows.activities import get_request
    from nomad_example.actions.workflows.models import (
        ExampleWorkflowInput,
        GetRequestInput,
    )


@workflow.defn(name='nomad_example.actions.workflows.ExampleWorkflow')
class ExampleWorkflow:
    @workflow.run
    async def run(self, data: ExampleWorkflowInput) -> dict:
        retry_policy = RetryPolicy(
            maximum_attempts=3,
        )
        get_request_input = GetRequestInput(
            url=(
                'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/'
                f'cid/{data.cid}/property/Title,SMILES/JSON',
            ),
            timeout=10,
        )
        result = await workflow.execute_activity(
            get_request,
            get_request_input,
            start_to_close_timeout=timedelta(seconds=30),
            retry_policy=retry_policy,
        )
        return result
```

Here we define the workflow as a class and describe the
sequence of activities under `run` method which uses the Temporal decorator
`workflow.run`. The name of the workflow, defined in the Temporal decorator
`workflow.defn`, needs to be unique. We recommend using the module path of the
workflow class as workflow name to ensure uniqueness among all the plugins
added to a NOMAD installation.
The workflow defines the flow of data into the activities. Using appropriate
data models, we pass the data from the workflow input to the activity input.
The activity is executed by `workflow.execute_activity` function which
can be used to specify retry policies and different types of timeout.

!!! important
    The default retry policy has unlimited attempts, meaning that if an activity
    fails, Temporal will keep retrying it forever. If this behavior is not
    required for your action, we strongly recommend to set a custom retry
    policy with finite `maximum_attempts` to avoid forever running workflows.

## Integrating action with schemas

After actions are defined, it is possible to run them from within NOMAD
entries by integrating them with [schemas](../../reference/glossary.md#schema).

The workflows defined through `ActionHandler` have unique names associated with
them. We can run a workflow using `start_workflow`
function, which takes the workflow name, an instance of its input model, and
the name of the task queue that should be used:

```py
from nomad.orchestrator.utils import start_workflow
from nomad.orchestrator.shared.constant import TaskQueue

from nomad_example.actions.models import ExampleWorkflowInput

workflow_id: str = start_workflow(
    workflow_name='nomad_example.actions.workflows.ExampleWorkflow',
    data=ExampleWorkflowInput(
        user_id='NOMAD User ID',
        upload_id='NOMAD Upload ID',
        cid=962,
    ),
    task_queue=TaskQueue.CPU,
)
```

!!! important
    Make sure the task queue used in `start_workflow` function corresponds to
    the task queue specified in the `ActionHandler` containing this workflow.

`start_workflow` returns a string containing a unique workflow ID assigned to the
triggered workflow run. This can be used to get the current status of the
workflow using `get_workflow_status` function which
takes the workflow ID as an input and returns a `WorkflowExecutionStatus` object:

```py
from nomad.orchestrator.utils import get_workflow_status
from temporalio.client import WorkflowExecutionStatus

workflow_status: WorkflowExecutionStatus = get_workflow_status(workflow_id)

print(workflow_status.name)  # example output: RUNNING
```

You can add these functionalities in the `normalize` of an
[ELN schema](../customization/elns.md) and trigger actions from the ELN
entries. A schema that uses ELN quantities to trigger actions can look like this:

```py

```

Here we did something.

## Using workflow artifacts directory

- `from nomad.orchestrator.utils import workflow_artifacts_dir`

## Defining workers for task queues

- A bit about the task queues
- How to standard workers for CPU and GPU ("switching on" docker settings)
- How to define custom workers for the available queues

## Adding to your oasis

- What are the steps needed for adding these workers and switch on temporal