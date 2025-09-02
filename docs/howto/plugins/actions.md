# How to define actions

!!! tip "Warning"

    NOMAD Actions are a preview feature available starting from NOMAD version `nomad-lab>=1.3.18.dev89`.
    Please note that this is an early release: some functionality may change, and you might encounter bugs.

    We’d love your feedback to help us improve NOMAD Actions, please don’t hesitate to reach out and share your thoughts.

Actions allow to define executable workflows in NOMAD. They are an
alternative to [normalizers](../../tutorial/custom.md#custom-normalizers) and can
be configured to use specialized workers instead of the NOMAD internal worker.
It allows for better resource allocation like GPUs for specific actions.

!!! tip "Important"

    Defining actions is more complicated when compared to defining
    normalizers in the schema packages and parser packages. If the processing
    workflow involves trivial data manipulation (for example, populating a
    quantity based on another quantity, reading and importing data from a raw
    file, etc.), consider using normalizers and parsers. On other hand, if your
    workflow requires robust interaction with an external API, longer
    processing time (for example, days), or special resource allocation, use actions.

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
   │   │   ├── __init__.py
   │   │   ├── actions
   │   │   │   ├── __init__.py
   │   │   │   ├── myaction
   │   │   │   │   ├── __init__.py
   │   │   │   │   ├── activities.py
   │   │   │   │   ├── workflows.py
   │   │   │   │   ├── models.py
   ├── LICENSE.txt
   ├── README.md
   └── pyproject.toml
```

The boilerplate code makes it easier to define actions. Start with replacing
the example code in `activities.py` with your code and adjusting the input data
model in the `models.py` with the required fields for your activity.

See the documentation on [plugin development guidelines](./plugins.md#plugin-development-guidelines)
for more details on the best development practices for plugins, including linting, testing and documenting.

By default, we provide `CPU` and `GPU` task queues. While defining an action,
it is assigned to one of these queues. If your action depends on packages that
are not required for the NOMAD installation, you can add them as
optional dependencies in the `pyproject.toml` for the given task queue:

```toml
[project]
name = "nomad-example"
...

[optional-dependencies]
gpu-action = ["torch"]
cpu-action = ["aiohttp"]
```

## Action entry point

The entry point defines basic information about your action and is used to
automatically load it into a NOMAD distribution. It is an instance of a
`ActionEntryPoint` or its subclass and it contains a `load` method which
returns a `Action` instance.

The `Action` instance can be used to add workflows and activities, along
with the task queue where they will be registered. You will learn more about
`Action` class in the [next section](#action-class). The entry point should be defined
in `*/actions/__init__.py` like this:

```py
from nomad.actions import TaskQueue
from pydantic import Field
from temporalio import workflow

with workflow.unsafe.imports_passed_through():
    from nomad.config.models.plugins import ActionEntryPoint


class MyActionEntryPoint(ActionEntryPoint):
    task_queue: str = Field(
        default=TaskQueue.CPU, description='Determines the task queue for this action'
    )

    def load(self):
        from nomad.actions import Action

        from nomad_example.actions.myaction.activities import get_request
        from nomad_example.actions.myaction.workflows import ExampleWorkflow

        return Action(
            task_queue=self.task_queue,
            workflow=ExampleWorkflow,
            activities=[get_request],
        )


my_action = MyActionEntryPoint(
    name='MyAction',
    description='My custom action.',
)
```

Here you can see that a new subclass of `MyActionEntryPoint` was defined. In
this new class you can override the `load` method to determine how the
`Action` class is loaded, but you can also extend the
`ActionEntryPoint` model to add new configurable parameters for this schema
package as explained [here](../../explanation/plugin_system.
md#plugin-configuration).

We also instantiate an object `my_action` from the new subclass. This is the
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
myaction = "nomad_example.actions.myaction:my_action"
```

## `Action` class

The `load`-method of an action entry point returns an instance of a
`nomad.actions.Action` class which describes the action through
a collection of activities and workflows that connect them. It also specifies the task queue for which the workflows and activities are registered. Once the
workflows are made available through the `Action`, they can be triggered
using the `start_action` funtion. This adds a workflow run instance to the specified task queue. You can learn more about it in the [next section](#integrating-action-with-schemas).

We use [Temporal](https://docs.temporal.io/temporal)'s workflow-activity
abstraction here. Activities are the atomic unit of execution. They should
ideally be defined as
[idempotent](https://docs.temporal.io/activity-definition#idempotency),
allowing Temporal to retry automatically based on a policy until the activity
is successfully completed. For example, an idempotent activity that gets data
from an external resource via API can keep retrying until a status
code 200 (successful response) is achieved. Once the activities are
defined, a workflow arranges them in a sequence and defines flow of data from
one activity to another.

You can add these definitions in `*/myaction/activities.py` and
`*/myaction/workflows.py`. Temporal requires the input and output of the
activities and workflows to be serializable. We recommend defining Pydantic
models for them in `*/myaction/models.py`. These files could look like this:

**nomad_example/actions/myaction/models.py**

```py
from pydantic import BaseModel, Field


class BaseWorkflowInput(BaseModel):
    """Base input model for workflows"""

    upload_id: str = Field(
        ...,
        description='Unique identifier for the upload associated with the workflow.',
    )
    user_id: str = Field(
        ..., description='Unique identifier for the user who initiated the workflow.'
    )


class ExampleWorkflowInput(BaseWorkflowInput):
    """Input model for the workflow"""

    cid: int = Field(
        ..., description='PubChem compound identifier for a chemical compound.'
    )


class GetRequestInput(BaseModel):
    """Input model for the activity"""

    url: str = Field(..., description='URL for get request.')
    timeout: int = Field(..., description='Timeout for the request.')
```

Here we extend `BaseWorkflowInput` for defining the input model
of the workflow and simply extend `BaseModel` class from
Pydantic to define the input model of the activity.

!!! tip "Important"
    We provide a Pydantic base model `BaseWorkflowInput` in the plugin template code and recommend to inherit it for defining the workflow's input
    model. It provides fields like `user_id` and `upload_id` which are required
    to execute a workflow in NOMAD. These fields are required to enable
    database interaction via actions.

**nomad_example/actions/myaction/activities.py**

```py
from temporalio import activity

from nomad_example.actions.myaction.models import GetRequestInput


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
            response.raise_for_status()
            return await response.json()
```

Here we define an activity by using the Temporal decorator `activity.defn` on
the `get_request` function. The activity interacts with an external API
asynchronously. Non-blocking activities allow Temporal to efficiently manage
the task queues, handling multiple workflows at once. We use `GetRequestInput`
model to define the argument of this activity.

**nomad_example/actions/myaction/workflows.py**

```py
from datetime import timedelta

from temporalio import workflow
from temporalio.common import RetryPolicy

with workflow.unsafe.imports_passed_through():
    from nomad_example.actions.myaction.activities import get_request
    from nomad_example.actions.myaction.models import (
        ExampleWorkflowInput,
        GetRequestInput,
    )


@workflow.defn
class ExampleWorkflow:
    @workflow.run
    async def run(self, data: ExampleWorkflowInput) -> dict:
        retry_policy = RetryPolicy(
            maximum_attempts=3,
        )
        get_request_input = GetRequestInput(
            url='https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/'
            f'cid/{data.cid}/property/Title,SMILES/JSON',
            timeout=10,
        )
        result = await workflow.execute_activity(
            get_request,
            get_request_input,
            start_to_close_timeout=timedelta(seconds=60),
            retry_policy=retry_policy,
        )
        return result
```

Here we make a workflow definition by creating as a Python class and using
the Temporal decorator `workflow.defn`.
The name of workflow is automatically taken from the unique ID of the
action entry point, which is nothing but the package path to its definition.
For our example, it will be `nomad_example.actions.myaction:my_action`.

We define the workflow *function* in the `run` method of the workflow
definition class and use the Temporal decorator `workflow.run`. It describes the
sequence of activities and the flow of data from one to another. Using appropriate data models, we pass the data from the workflow input to the activity inputs.

Each activity is executed by `workflow.execute_activity` function which
also specifies the activity's retry policy and timeouts.
[Retry Policy](https://docs.temporal.io/encyclopedia/retry-policies)
tells Temporal how to retry an activity that failed in the current execution.
Attributes like `initial_interval`, `backoff_coefficient`, and
`maximum_interval` control the interval between retries. The attribute
`maximum_attempts` specifies the maximum retries that can be made in case of
failures.

Activity timeouts can detect failures, simply because the activity exceeds the
maximum expected execution time. Temporal provides multiple
[timeouts](https://docs.temporal.io/encyclopedia/detecting-activity-failures).
The attribute `start_to_close_timeout` specifies the timeout for an activity
execution, i.e., the time spent after a worker starts executing an activity
till it is finished. For most cases, setting this alone is enough and
recommended. Make sure that the timeout is longer than the maximum possible
time for the activity execution to complete. For example, while setting one for
an activity that makes an API call, determine the median call time and add some
buffer to it.

!!! tip "Important"
    The default retry policy has unlimited `maximum_attempts`. We strongly
    recommend to **always set a custom retry policy** with finite `maximum_attempts` to avoid forever running workflows.
    In addition, **always set appropriate timeouts** for activities to prevent stuck executions.

## Integrating action with schemas

After actions are defined, it is possible to intergrate their workflows with
[schemas](../../reference/glossary.md#schema) and run them from NOMAD
entries.

Every action has a unique name based on the package path of its entry point.
We can run a workflow using `start_action`
function, which takes the action name and an instance of its input model:

```py
from nomad.actions.utils import start_action

from nomad_example.actions.myaction.models import ExampleWorkflowInput

workflow_id = start_action(
    action_name='nomad_example.actions.myaction:my_action',
    data=ExampleWorkflowInput(
        user_id='NOMAD User ID',
        upload_id='NOMAD Upload ID',
        cid=962,  # CID for Water
    ),
)
```

`start_action` returns a string containing a unique workflow ID assigned to the
triggered workflow run. This can be used to get the current status of the
workflow using `get_action_status` function which takes the workflow ID as an
input and returns a `temporalio.client.WorkflowExecutionStatus` object:

```py
from nomad.actions.utils import get_action_status

workflow_status = get_action_status(workflow_id)

print(workflow_status.name)  # example output: RUNNING
```

You can add these functionalities in the `normalize` of an
[ELN schema](../customization/elns.md) and trigger actions from the ELN
entries. A schema that uses ELN quantities to trigger actions can look like this:

```py
from nomad.actions.utils import get_action_status, start_action
from nomad.datamodel.data import EntryData
from nomad.datamodel.metainfo.annotations import ELNAnnotation, ELNComponentEnum
from nomad.datamodel.metainfo.basesections.v1 import PureSubstanceSection
from nomad.metainfo import Quantity, SchemaPackage, SubSection

from nomad_example.actions.myaction.models import ExampleWorkflowInput

m_package = SchemaPackage()


class ExampleWorkflow(EntryData):
    """A section to run an example workflow using a PubChem CID."""

    cid = Quantity(
        type=int,
        description='PubChem CID of the compound.',
        a_eln=ELNAnnotation(component=ELNComponentEnum.NumberEditQuantity),
    )
    workflow_id = Quantity(
        type=str,
        description='Unique ID of the workflow.',
    )
    workflow_status = Quantity(
        type=str,
        description='Status of the workflow based on the available workflow ID.',
    )
    pubchem_result = SubSection(
        section_def=PureSubstanceSection,
        description='Data populated based on PubChem API call for given CID.',
    )

    trigger_run_action = Quantity(
        type=bool,
        description='Starts an asynchronous run of the example action.',
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.ActionEditQuantity,
            label='Run Example Action',
        ),
    )
    trigger_get_action_status = Quantity(
        type=bool,
        description='Fetches the status for the available workflow ID.',
        a_eln=ELNAnnotation(
            component=ELNComponentEnum.ActionEditQuantity,
            label='Get Action Status',
        ),
    )

    def run_action(self, archive, logger=None):
        """Run the action with the provided archive."""
        try:
            if not self.cid:
                logger.warn(
                    'No CID provided for the workflow. Cannot run the workflow.'
                )
                return
            self.pubchem_result = None
            self.workflow_status = None
            self.workflow_id = None
            action_name = 'nomad_example.actions.myaction:my_action'
            input_data = ExampleWorkflowInput(
                user_id=archive.metadata.authors[0].user_id,
                upload_id=archive.metadata.upload_id,
                cid=self.cid,
            )
            self.workflow_id = start_action(action_name=action_name, data=input_data)
            self.trigger_get_action_status = True
        except Exception as e:
            logger.error(f'Error running workflow: {e}')

    def normalize(self, archive, logger=None):
        super().normalize(archive, logger)
        if self.trigger_run_action:
            if self.workflow_status == 'RUNNING':
                logger.warn('Workflow is already running. Cannot start a new one.')
            else:
                self.run_action(archive, logger)
            self.trigger_run_action = False
        if self.trigger_get_action_status:
            if self.workflow_id:
                try:
                    status = get_action_status(self.workflow_id)
                    self.workflow_status = status.name
                except Exception as e:
                    logger.error(f'Error getting workflow status: {e}. ')
            self.trigger_get_action_status = False


m_package.__init_metainfo__()
```

Here we define an `EntryData` section with ELN quantities like `cid`, which
takes a integer input, and `trigger_run_action`, which is an actionable
button. When the `trigger_run_action` button is clicked, the `start_action`
function is triggered from inside the `run_action` method.
`workflow_id` quantity is populated as a result, which is used in the next step
to get the status of the workflow.

When `trigger_get_action_status` is clicked, the status for the available `workflow_id` is requested and is saved as a string in `workflow_status`
quantity. This status can be mainly `RUNNING`, `COMPLETED`, `FAILED`, `CANCELLED` or `TERMINATED`. Everytime a workflow run is triggered, the status for it is also requested.

It is also possible to re-trigger the workflow run if the status is not
`RUNNING`. Of course, the new workflow run will now have a different workflow
ID.

After we run the workflow, we can also write back the results into the entry
using the utilities described in the next section.

## Utilities for actions

Interaction with your Oasis's database from Actions provides a powerful way of
manipulating it. For example, once you run an action, you might want to save
its output in an existing NOMAD entry, or even create new ones. We provide a
curated set of utils in `nomad.actions.utils` module to perform these tasks.

!!! tip "Important"
    Since interacting with database directly (bypassing the API endpoint)
    through Actions is highly risky, we strongly recommend to only do this
    through the functions defined under `nomad.actions.utils`
    module. If you have to perform a task that is not covered in the utils,
    please use the available API endpoints and interact with the database via
    the network.

!!! note "Note"
    This part of the documentation is under development.

## Adding to your oasis

Make sure your oasis repo is up to date with the template by following the
update [guide](https://github.com/FAIRmat-NFDI/nomad-distro-template?tab=readme-ov-file#updating-the-distribution-from-the-template). This ensures
that the necessary containers for `temporal` is setup correctly.

In addition to configuring the temporal service, you’ll also need to build new Docker images for both the gpu and cpu workers. The relevant extras for these workflows can be set in the pyproject.toml of the distro:

```toml
[project]
name = "nomad-distro-template"
...

[optional-dependencies]
plugins = ["nomad-example"]
gpu-action = ["nomad-example[gpu-action]"]
cpu-action = ["nomad-example[cpu-action]"]
```

To implement the necessary changes, including image build steps and updates to
docker-compose, the Dockerfile, and GitHub Actions, you can refer to this
[pull request](https://github.com/FAIRmat-NFDI/nomad-distro-template/pull/109/files)
as a guide.
