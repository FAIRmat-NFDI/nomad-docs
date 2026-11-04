# How to get started in development

## Set up a local development environment

Use the [NOMAD development distribution (`nomad-distro-dev`)](https://github.com/FAIRmat-NFDI/nomad-distro-dev){:target="_blank" rel="noopener"}
for local development of the core `nomad` package and NOMAD plugins, including testing
plugins in the GUI.

Fork the repository and follow its maintained README instructions:

- [Basic infrastructure](https://github.com/FAIRmat-NFDI/nomad-distro-dev#basic-infra){:target="_blank" rel="noopener"}
  for prerequisites and starting the required services.
- [Developing NOMAD and plugins locally](https://github.com/FAIRmat-NFDI/nomad-distro-dev#developing-nomad--plugins-locally){:target="_blank" rel="noopener"}
  for installing dependencies, configuring plugins, and running the backend and GUI.

Keep infrastructure, environment configuration, and startup instructions in that
repository as the source of truth rather than combining them with older setup guides.
The development distribution is not intended for production; use the
[Oasis deployment guide](../oasis/deploy.md) for deploying an Oasis.

For installing and using the NOMAD Python package `nomad-lab` directly, see
[Manage and find data > Programmatically > Use the API](../manage/program/api.md).
For developing a plugin without running the full NOMAD stack, see
[stand-alone plugin installation](../../tutorial/develop_plugin/plugin_structure.md#option-1-stand-alone-installation-of-the-plugin).

## Running tests

Set up your environment using `nomad-distro-dev` first. Run the following backend
commands from the NOMAD source checkout, using the Python environment prepared by
the development distribution. Run frontend commands from its `gui` directory.

### Backend tests

To run the tests some additional settings and files are necessary that are not part
of the codebase.

You have to provide static files to serve the docs and NOMAD distribution:

```shell
./scripts/generate_docs_artifacts.sh
rm -rf site && mkdocs build && mv site nomad/app/static/docs
```

Start the required infrastructure services following the
[`nomad-distro-dev` instructions](https://github.com/FAIRmat-NFDI/nomad-distro-dev#basic-infra){:target="_blank" rel="noopener"}.
The tests need Elasticsearch, MongoDB, and Temporal; other services should be mocked
or provided by the tests. Do not run a separate NOMAD worker against the test task
queues, since it can consume tasks intended for test workers.

```shell
pytest -sv tests
```

!!! note
    Some of these tests will fail because a few large files are not included in the Git
    repository. You may ignore these for local testing, they are still checked by the
    CI/CD pipeline:

    ```text
    FAILED tests/archive/test_archive.py::test_read_springer - AttributeError: 'NoneType' object has no attribute 'seek'
    FAILED tests/normalizing/test_material.py::test_material_bulk - assert None
    FAILED tests/normalizing/test_system.py::test_springer_normalizer - IndexError: list index out of range
    ```

    Tests for plugins excluded from your NOMAD configuration will also fail.

We use Ruff and Mypy to maintain code quality. Additionally, we recommend installing the Ruff [plugins](https://docs.astral.sh/ruff/integrations/){:target="_blank" rel="noopener"} for your code editor to streamline the process. To execute Ruff and Mypy from the command line, you can utilize the following command:

```shell
nomad dev qa --skip-tests
```

We use ruff as a linter and as an autoformatter. If you only want to lint your code, you can run:

```shell
ruff check .
```

To format your code you can run:

```shell
ruff format .
```

To run all tests and code QA:

```shell
nomad dev qa
```

This mimics the tests and checks that the GitLab CI/CD will perform.

#### Custom pytest options

##### `--fixture-filters`

You may want to run only tests that use a specific fixture, e.g. if you are editing that fixture. For example, to run only tests with the `worker` fixture, use `pytest --fixture-filters worker`. If you list more than one, all of them must be requested by the test to be included.

You can also negate a fixture by prefixing its name with `!`. For example, to run all tests that do not depend on the `worker` fixture, use `pytest --fixture-filters '!worker'` (quotes are needed for `!`).

Note that if `test1` depends on `fixture1`, and `fixture1` depends on `fixture2`, then `test1` also depends on `fixture2`, even though it was not explicitly listed as a parameter.

### Frontend tests

We use
[`testing-library`](https://testing-library.com/docs/react-testing-library/intro/){:target="_blank" rel="noopener"}
to implement our GUI tests and `testing-library` itself uses
[`Jest`](https://jestjs.io/){:target="_blank" rel="noopener"} to run the tests. Tests are written in `*.spec.js`
files that accompany the implementation. Tests should focus on functionality,
not on implementation details: `testing-library` is designed to enforce this kind
of testing.

!!! note

    When testing HTML output, the elements are rendered using
    [jsdom](https://github.com/jsdom/jsdom){:target="_blank" rel="noopener"}: this is not completely identical
    to using an actual browser (e.g. does not support WebGL), but in practice
    is realistic enough for the majority of the test.

#### Test structure

We have adopted a `pytest`-like structure for organizing the test utilities:
each source code folder may contain a `conftest.spec.js` file that contains
utilities that are relevant for testing the code in that particular folder.
These utilities can usually be placed into the following categories:

- Custom renders: When testing React components, the
  [`render`](https://testing-library.com/docs/react-testing-library/api/#render){:target="_blank" rel="noopener"} function
  is used to display them on the test DOM. Typically your components require
  some parts of the infrastructure to work properly, which is achieved by
  wrapping your component with other components that provide a context. Custom
  render functions can do this automatically for you, e.g. the default render
  as exported from `src/components/conftest.spec.js` wraps your components with an
  infrastructure that is very similar to the production app. See
  [React Testing Library > custom-render](https://testing-library.com/docs/react-testing-library/setup/#custom-render){:target="_blank" rel="noopener"}
  for more information.

- Custom queries: See
  [React Testing Library > custom-queries](https://testing-library.com/docs/react-testing-library/setup/#add-custom-queries){:target="_blank" rel="noopener"}
  for more information.

- Custom expects: These are reusable functions that perform actual tests using
  the `expect` function. Whenever the same tests are performed by several
  `*.spec.js` files, you should formalize these common tests into an
  `expect*` function and place it in a relevant `conftest.spec.js` file.

Often your components will need to communicate with the API during tests. One
should generally avoid using manually created mocks for the API traffic, and
instead prefer using API responses that originate from an actual API call
during testing. It requires a lot of work to manually create mocks
and keep them up-to-date, and true integration tests are impossible
to perform with live communication with an API. In order to simplify the API
communication during testing, you can use the `startAPI`+`closeAPI` functions, that
will prepare the API traffic for you. A simple example could look like this:

```javascript
import React from 'react'
import { waitFor } from '@testing-library/dom'
import { startAPI, closeAPI, screen } from '../../conftest'
import { renderSearchEntry, expectInputHeader } from '../conftest'

test('periodic table shows the elements retrieved through the API', async () => {
  startAPI('<state_name>', '<snapshot_name>')
  renderSearchEntry(...)
  expect(...)
  closeAPI()
})
```

Here the important parameters are:

- `<state_name>`: Specifies an initial backend configuration for this test. These
  states are defined as Python functions that are stored in
  `nomad-FAIR/tests/states`, example given below. These functions may, for example,
  prepare several uploads, entries, etc. for the test.

- `<snapshot_name>`: Specifies a filepath for reading/recording pre-recorded API
  traffic.

An example of a simple test state could look like this:

```python
from nomad import infrastructure
from nomad.utils import create_uuid
from nomad.utils.exampledata import ExampleData


def search():
    infrastructure.setup()
    main_author = infrastructure.user_management.get_user(username='test')
    data = ExampleData(main_author=main_author)
    upload_id = create_uuid()
    data.create_upload(upload_id=upload_id, published=True, embargo_length=0)
    data.create_entry(
        upload_id=upload_id,
        entry_id=create_uuid(),
        mainfile='test_content/test_entry/mainfile.json',
        results={'material': {'elements': ['C', 'H']}, 'method': {}, 'properties': {}},
    )
    data.save()
```

When running in the online mode (see below), this function will be executed in
order to prepare the application backend. The `closeAPI` function will handle
cleaning the test state between successive `startAPI` calls: it will completely
wipe out MongoDB, Elasticsearch and the upload files.

#### Running frontend tests

The tests can be run in two different modes. *Offline testing* uses
pre-recorded files to mock the API traffic during testing. This allows one to
run tests more quickly without a server. During *online testing*, the tests
perform calls to a running server where a test state has been prepared. This
mode can be used to perform integration tests but also to record the snapshot
files needed by the offline testing.

Before running tests, ensure that the GUI artifacts are up-to-date. Run this from
the NOMAD source checkout:

```sh
./scripts/generate_gui_test_artifacts.sh
```

As snapshot tests do not connect to the server, the artifacts cannot be
fetched dynamically from the server and static files need to be used instead.
Note that you should not push these files to Git: the CI/CD pipeline will
automatically generate them.

##### Offline testing

This is the way our CI pipeline runs the tests and should be used locally, e.g.
whenever you wish to reproduce pipeline errors or when your tests do not
involve any API traffic.

Run `yarn test` to run the whole suite, or `yarn test [<filename>]` to run a specific test.

##### Online testing

When you wish to record API traffic for offline testing, or to perform
integration tests, you will need to have a server running with the correct
configuration. To do this, follow these steps:

1. Start the required infrastructure following the
   [`nomad-distro-dev` instructions](https://github.com/FAIRmat-NFDI/nomad-distro-dev#basic-infra){:target="_blank" rel="noopener"}.

2. From the NOMAD source checkout, start `nomad admin run appworker` with the config
   found in `gui/tests/nomad.yaml`:
   `export NOMAD_CONFIG=gui/tests/nomad.yaml && nomad admin run appworker`

3. Activate the correct Python virtual environment before running the tests
   with Yarn (Yarn will run the Python functions that prepare the state).

4. From the `gui` directory, run `yarn test-record [<filename>]` to record a
   snapshot file, or `yarn test-integration [<filename>]` to perform the test
   without recording.

!!! warning
    Online tests delete database contents and uploaded files when resetting test
    state. Use a dedicated test configuration and data, never a production Oasis.

## Build custom Oasis image

To create a custom Oasis image (e.g. with custom plugins), you could use the [nomad-distro-template](https://github.com/FAIRmat-NFDI/nomad-distro-template){:target="_blank" rel="noopener"} by clicking the [**Use this template** button](https://github.com/new?template_name=nomad-distro-template&template_owner=FAIRmat-NFDI){:target="_blank" rel="noopener"}. For detailed instructions on building and deploying custom Oasis images, please refer to the documentation in that repository.

## Setup your IDE

Follow the editor and workspace configuration in
[`nomad-distro-dev`](https://github.com/FAIRmat-NFDI/nomad-distro-dev){:target="_blank" rel="noopener"}
so your IDE uses the same Python environment as the development distribution.
Configure your editor to use Ruff for linting and formatting, Mypy for static
analysis, and pytest for backend tests. See the
[contribution guidelines](contrib.md) for the project's code quality expectations.
