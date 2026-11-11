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
the development distribution.

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

The GUI is maintained in the separate
[`nomad-gui` repository](https://gitlab.mpcdf.mpg.de/nomad-lab/nomad-gui){:target="_blank" rel="noopener"}.
Follow that repository's maintained development and testing instructions.

## Build custom Oasis image

To create a custom Oasis image (e.g. with custom plugins), you could use the [nomad-distro-template](https://github.com/FAIRmat-NFDI/nomad-distro-template){:target="_blank" rel="noopener"} by clicking the [**Use this template** button](https://github.com/new?template_name=nomad-distro-template&template_owner=FAIRmat-NFDI){:target="_blank" rel="noopener"}. For detailed instructions on building and deploying custom Oasis images, please refer to the documentation in that repository.

## Setup your IDE

Follow the editor and workspace configuration in
[`nomad-distro-dev`](https://github.com/FAIRmat-NFDI/nomad-distro-dev){:target="_blank" rel="noopener"}
so your IDE uses the same Python environment as the development distribution.
Configure your editor to use Ruff for linting and formatting, Mypy for static
analysis, and pytest for backend tests. See the
[contribution guidelines](contrib.md) for the project's code quality expectations.
