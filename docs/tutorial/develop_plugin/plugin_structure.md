# Develop a NOMAD plugin

In this tutorial series, you will develop a custom NOMAD plugin that extends NOMAD with a domain-specific schema package and a parser. To follow the full development workflow, we chose several possible applications as an example, including simplified optical microscopy measurements and black-body radiation calculations. The tutorial utilizes a set of exercises leading to the development of a working plugin that can be tested locally and integrated into a NOMAD Oasis deployment. The exercises cover everything from creating a plugin repository and defining schemas to implementing parsing and testing.

---

## What you will learn

In this tutorial, you will learn how to:

1. Create and version-control a NOMAD plugin repository using Git and GitHub
2. Generate a plugin project using the official NOMAD cookiecutter template
3. Set up a development and testing environment for the plugin

In the following tutorials, you will create a custom schema package and a parser.

---

## Before you begin

This tutorial assumes basic familiarity with Python and Git, as well as minimal experience of using NOMAD. It is intended for users who want to extend local NOMAD deployment (NOMAD Oasis) with custom functionality.

Before starting this tutorial, make sure you have the following:

1. **GitHub account**
   Required to create and manage the plugin repository. You can create a free account at [github.com/signup](https://github.com/signup){:target="_blank" rel="noopener"}.

2. **Basic understanding of Python**
   You should be comfortable reading and writing basic Python code, including modules, functions,
   and classes.

3. **Basic understanding of NOMAD metainfo**
   Familiarity with NOMAD’s metainfo system is helpful. If needed, review [FAIRmat Tutorial 8](https://www.fairmat-nfdi.eu/events/fairmat-tutorial-8/tutorial-8-materials){:target="_blank" rel="noopener"}.

4. **Local or cloud-based development environment**
   You need either:

    - A local machine with Python ≥ 3.12, git, and any Integrated Development Environment (IDE), or
    - Access to GitHub Codespaces for cloud-based development.

??? info "Background concepts used in this tutorial (optional)"
    This tutorial touches on several common software-development tools and concepts.
    You do **not** need to master them in advance, but the links below may be helpful
    if you are unfamiliar with any of them:

    - [what is Git](https://learn.microsoft.com/en-us/devops/develop/git/what-is-git){:target="_blank" rel="noopener"}
    - [what is an IDE](https://aws.amazon.com/what-is/ide/){:target="_blank" rel="noopener"}
    - [what is VSCode (an example of IDE)](https://code.visualstudio.com/docs/getstarted/overview){:target="_blank" rel="noopener"}
    - [what is Pip](https://realpython.com/lessons/what-is-pip-overview/){:target="_blank" rel="noopener"}
    - [what is a Python virtual environment](https://realpython.com/python-virtual-environments-a-primer/#why-do-you-need-virtual-environments){:target="_blank" rel="noopener"}
    - [what is uv](https://realpython.com/ref/tools/uv/){:target="_blank" rel="noopener"}
    - [creating a Python package](https://packaging.python.org/en/latest/tutorials/packaging-projects/){:target="_blank" rel="noopener"}
    - [uploading a package to PyPI](https://www.freecodecamp.org/news/how-to-create-and-upload-your-first-python-package-to-pypi/){:target="_blank" rel="noopener"}
    - [what is cruft](https://cruft.github.io/cruft/){:target="_blank" rel="noopener"}

---

## Create a plugin repository

First, you will version-control your NOMAD plugin by creating a GitHub repository from the official template. Start from the official GitHub template repository at
[github.com/FAIRmat-NFDI/nomad-plugin-template](https://github.com/FAIRmat-NFDI/nomad-plugin-template){:target="_blank" rel="noopener"}.

To create a new repository from the template, select **Use this template** and then choose
**Create a new repository**. You must be logged in to GitHub to see this option.

![Use template](../images/use_template_dark.png#gh-dark-mode-only)
![Use template](../images/use_template_light.png#gh-light-mode-only)

Enter a repository name (for example, `nomad-optical-microscopy`) and select **Create repository** to complete the setup.
<!-- TODO: add image slider to show the two steps -->

## Generate the plugin structure

Next, you will generate the initial structure of the plugin by applying the official NOMAD cookiecutter template.

### Choose a development environment

In this step, you can proceed in one of the two following ways:

1. Use GitHub Codespaces (cloud-based development), or
2. Develop locally.

#### Option 1: Using GitHub Codespaces (Recommended)

To use a GitHub Codespace for plugin development, click on the **<> Code** button in the repository and choose **Create codespace on main**.

![Use codespace](../images/codespace_dark.png#gh-dark-mode-only)
![Use codespace](../images/codespace_light.png#gh-light-mode-only)

#### Option 2: Developing locally

If you prefer to work locally, click on the **<> Code** button in the repository and choose the **“Local”** tab, copy the repository URL, and clone it to a selected location in your machine by running in terminal:

```sh
cd LOCAL/PATH/ON/YOUR/MACHINE
git clone PATH/COPIED/FROM/REPOSITORY
cd REPOSITORY_NAME
```

### Use cruft to generate the plugin

Cruft is a tool that creates projects from Cookiecutter templates and keeps them up to date as the template evolves.

#### Install cruft

*Skip this step if you are using GitHub Codespaces (cruft is available by default).*

Install [cruft](https://pypi.org/project/cruft/){:target="_blank" rel="noopener"}, preferably using
`pipx` by running the following:

```sh
# pipx is strongly recommended.
pipx install cruft

# If pipx is not an option,
# you can install cruft in your Python user directory.
python -m pip install --user cruft
```

#### Run cruft

Generate the plugin structure by running in terminal:

```sh
cruft create https://github.com/FAIRmat-NFDI/cookiecutter-nomad-plugin
```

Cookiecutter prompts you for information regarding your plugin. Enter values appropriate for your plugin.
For example:

```no-highlight
  [1/12] full_name (John Doe): Hampus Näsström
  [2/12] email (john.doe@physik.hu-berlin.de): hampus.naesstroem@physik.hu-berlin.de
  [3/12] github_username (foo): hampusnasstrom
  [4/12] plugin_name (foobar): optical-microscopy
  [5/12] module_name (optical_microscopy):
  [6/12] short_description (NOMAD example template): A schema package and parser plugin for optical microscopy.
  [7/12] version (0.1.0):
  [8/12] Select license
    1 - MIT
    2 - BSD-3
    3 - GNU GPL v3.0+
    4 - Apache Software License 2.0
    Choose from [1/2/3/4] (1):
  [9/12] include_schema_package [y/n] (y): y
  [10/12] include_normalizer [y/n] (y): n
  [11/12] include_parser [y/n] (y): y
  [12/12] include_app [y/n] (y): n
```

Selecting `y` for include_schema_package creates a Python package for the schema, and similarly for the parser.

!!! success "You have just created a minimal NOMAD plugin with a plugin entry point for a schema package"
    ```no-highlight
    optical-microscopy/
    ├── LICENSE
    ├── MANIFEST.in
    ├── README.md
    ├── docs
    │   └── ...
    ├── mkdocs.yml
    ├── move_template_files.sh
    ├── pyproject.toml
    ├── src
    │   └── optical_microscopy
    │       ├── __init__.py
    │       ├── parsers
    │       │   ├── __init__.py
    │       │   └── parser.py
    │       └── schema_packages
    │           ├── __init__.py
    │           └── schema_package.py
    └── tests
        ├── conftest.py
        ├── data
        │   └── test.archive.yaml
        ├── parsers
        │   └── test_parser.py
        └── schema_packages
            └── test_schema.py
    ```

The plugin is generated in a subdirectory. Move the files to the repository root using the provided helper script:

```sh
sh optical-microscopy/move_template_files.sh
```

Finally, add the files to Git and commit the changes you have made:

```sh
git add -A
git commit -m "Generated plugin from cookiecutter template"
git push
```

#### Enable cruft updates

The template repository includes a GitHub Actions workflow that checks for updates to the cookiecutter template. The workflow runs automatically once a week and can also be triggered manually. To enable this functionality, grant the workflow permission to write to the repository and create pull requests.

From your plugin repository on GitHub, open the **Settings** page, and navigate to **Actions → General** (on the left pane):

![Use template](../images/github_settings_dark.png#gh-dark-mode-only)
![Use template](../images/github_settings_light.png#gh-light-mode-only)

Scroll to the bottom of the page, select the "Read and write permissions"
and check the "Allow GitHub Actions to create and approve pull requests" options, and then click **Save**.

![Use template](../images/workflow_permissions_dark.png#gh-dark-mode-only)
![Use template](../images/workflow_permissions_light.png#gh-light-mode-only)

## Developing the plugin

The structure of the plugin is now ready for development for your specific purposes. If you plan to work with a single plugin and can avoid using NOMAD GUI functionality, stand-alone installation of the plugin will be sufficient. If you plan to work with multiple plugins or GUI-specific functionality, or if you wish to develop the core NOMAD package, we recommend using a dedicated [`nomad-distro-dev`](https://github.com/FAIRmat-NFDI/nomad-distro-dev){:target="_blank" rel="noopener"} development environment.

### Option 1: Stand-alone installation of the plugin

In this step, you will set up a Python environment and install the plugin for local development. This can be done conveniently in one step using [uv](https://docs.astral.sh/uv/getting-started/installation/){:target="_blank" rel="noopener"} or in several steps with pip.

#### (Recommended) Installation with uv

Open the terminal, navigate to the folder with your plugin using `cd`. Set up the plugin:

```sh
uv sync --extra dev
```

This sets up a dynamic Python environment. To run a command within the python environment, use:

```sh
uv run <command>
```

#### (Alternative) Installation with pip

Open the terminal, navigate to the folder with your plugin using `cd`. Create a virtual environment using Python 3.12 and activate it:

```sh
python3.12 -m venv .pyenv
source .pyenv/bin/activate
```

Install the plugin package in editable mode using the NOMAD package registry:

```sh
pip install --upgrade pip
pip install -e '.[dev]'
```

You can stop using the virtual environment by running:

```sh
deactivate
```

And return to it by running again in the terminal in the project folder:

```sh
source .pyenv/bin/activate
```

### Option 2: `nomad-distro-dev`

This option is designed to be used with a local Linux-based machine. The `nomad-distro-dev` also works with macOS or Windows, but some NOMAD plugins might not function correctly there.

This setup is required when you need to verify plugin behavior in the NOMAD GUI.

Start with forking [`nomad-distro-dev`](https://github.com/FAIRmat-NFDI/nomad-distro-dev){:target="_blank" rel="noopener"} repository (`Fork` -> `Create a new fork` in the upper right part of the page). You will also need the following additional software installed on your system:

- [Docker](https://docs.docker.com/engine/install/){:target="_blank" rel="noopener"} - generally, only `docker-compose` functionality will be needed

- [uv](https://docs.astral.sh/uv/getting-started/installation/){:target="_blank" rel="noopener"} python package manager, version 0.5.14 or above

- [node.js](https://nodejs.org/en){:target="_blank" rel="noopener"} version 20 or above and [yarn](https://classic.yarnpkg.com/en/docs/install){:target="_blank" rel="noopener"} version 1.22 or above are necessary to run the GUI

Then, follow the instructions in the `nomad-distro-dev` readme file under the [`Basic infra`](https://github.com/FAIRmat-NFDI/nomad-distro-dev#basic-infra){:target="_blank" rel="noopener"} and [`Developing nomad + plugins locally`](https://github.com/FAIRmat-NFDI/nomad-distro-dev#developing-nomad--plugins-locally){:target="_blank" rel="noopener"} headings.

## Next steps

In the next tutorials you will learn how to add data schemas and file parsers to an existing NOMAD plugin.
