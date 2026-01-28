# How to create a NORTH tool

NORTH (NOMAD Remote Tools Hub) is NOMAD's hub for running data analysis tools in isolated,
containerized environments. It enables tools to be executed reproducibly and securely while
being tightly integrated with the NOMAD data infrastructure.

This documentation shows you how to write a plugin entry point for a NORTH tool.
You should read the [introduction to plugins](../plugins.md)
to have a basic understanding of how plugins and plugin entry points work in the NOMAD ecosystem.

## Getting started

You can use our [template repository](https://github.com/FAIRmat-NFDI/nomad-plugin-template){:target="_blank" rel="noopener"} to
create an initial structure for a plugin containing a custom NORTH tool.
The relevant part of the repository layout will look something like this:

<!-- markdownlint-disable MD044 -->
```txt
nomad-example
   ├── .github/workflows
   │   ├── publish-north.yaml
   ├── src
   │   ├── nomad_example
   │   │   ├── __init__.py
   │   │   ├── north_tools
   |   |   |   ├── my_tool
   |   │   │   │   ├── __init__.py
   |   │   │   │   ├── Dockerfile
   |   |   │   │   └── README.md
   |   │   |   └── __init__.py
   ├── LICENSE.txt
   ├── README.md
   ├── Dockerfile
   └── pyproject.toml
```

See the documentation on [plugin development guidelines](../plugins.md#plugin-development-guidelines)
for more details on the best development practices for plugins, including linting, testing and documenting.

## NORTH tool entry point

The entry point defines basic information about your NORTH tool and is used to
automatically load it into a NOMAD distribution. It is an instance of a
`NorthToolEntryPoint` or its subclass.

The `NORTHTool` instance can be used to define which Docker image the NORTH tools is to run.
You will learn more about creating these images in the [next section](#creating-north-images). The entry point should be defined
in `*/north_tools/__init__.py` like this:

<!-- markdownlint-disable MD044 -->
```py

from nomad.config.models.north import NORTHTool
from nomad.config.models.plugins import NorthToolEntryPoint

tool = NORTHTool(
    image='ghcr.io/FAIRMat-NFDI/nomad-example/jupyter:latest',
    description='An example Jupyter Notebook served in NORTH',
    external_mounts=[],
    file_extensions=['ipynb'],
    icon='logo/jupyter.svg',
    image_pull_policy='Always',
    default_url='/lab',
    maintainer=[
        {'email': 'fairmat@physik.hu-berlin.de', 'name': 'John Doe'}
    ],
    mount_path='/home/jovyan',
    privileged=False,
    with_path=True,
    display_name='MyTool',
)

my_north_tool = NorthToolEntryPoint(id='my-north-tool', north_tool=tool)
```

!!! note
    To test a Docker image in NOMAD NORTH tool, you do not need to publish the Docker image in a registry but can build it locally and add the image in the NORTHTool configuration. NOMAD NORTH tool will check for local images first before pulling from a registry. 

Here you can see that a `NORTHTool` object called `tool` was defined. We also instantiate
the entry point object `my_north_tool` using the tool. This is the
final entry point instance in which you specify the default parameterization
and other details about the NORTH tools. In the reference you can see all of the
available configuration options for a [`NorthToolEntryPoint`](../../../reference/plugins.
md#northtoolentrypoint) and a [`NorthTool`](../../../reference/config.md#northtool).

### Key Configuration Options

When defining your NORTH tool, consider these important configuration options:

- **image**: Location of the Docker image (e.g., `ghcr.io/<username>/<plugin-name>:latest`). This should point to a container registry where your image is published.
- **file_extensions**: The file extensions of files that this tool should be launchable for.
- **mount_path**: The directory inside the container where NOMAD data or other relevant files for data analysis will be mounted (e.g., `/home/jovyan/data` for Jupyter-based tools).
- **default_url**: The optional suffix of URL path when the tool launches (e.g., `/lab` for JupyterLab).
- **with_path**: Boolean, whether the tool supports a path to a file or directory. This also enables tools to be launched from files in the NOMAD UI.
- **display_name**: The name of the tool displayed in the list NOMAD NORTH tools.
- **description**: A brief description of what the tool does.
- **maintainer**: List of maintainer information with name and email.
- **image_pull_policy**: When to pull the image in K8s deployments.

The entry point instance should then be added to the `[project.entry-points.'nomad.plugin']`
table in `pyproject.toml` in order for it to be automatically
detected:

```toml
[project.entry-points.'nomad.plugin']
mynorthtool = "nomad_example.north_tools:my_north_tool"
```

## Creating `NORTH` images
The core of a NORTH tool is the container image that contains the actual software tools, examples,
and environment needed to run the tool. In this section we will discuss how to create
such images. Docker images can be built either locally or remotely, instructed via the GitHub CI (discussed later).

### Prerequisites

Before creating NORTH images, ensure you have:

- **Docker installed**: [Get Docker](https://www.docker.com/get-started){:target="_blank" rel="noopener"} installed on your local system. This allows you to build and test images locally before publishing.
- **Base image selected**: Choose an appropriate slim base image for your tool (e.g., `<image-name:tag>` like `quay.io/jupyter/scipy-notebook:2025-10-20` for Jupyter-based tools).
- **Container registry access**: Access to a container registry for publishing your images (see [Docker registries](#docker-registries)).

For Docker best practices, refer to the [official Docker documentation](https://docs.docker.com/develop/dev-best-practices/){:target="_blank" rel="noopener"}.

### Docker Registries

NORTH tools support images from various container registries:

- **GitHub Container Registry (GHCR)**: `ghcr.io/<username>/<image-name>` - Recommended for GitHub-hosted projects. Integrates seamlessly with GitHub Actions.
- **Docker Hub**: `docker.io/<username>/<image-name>` - Popular public registry with free tier for public images.
- **Quay.io**: `quay.io/<username>/<image-name>` - Red Hat's container registry with strong security features.
- **Private registries**: Custom registry URLs for organization-specific deployments.

!!! note "Publishing Your Images"
    You are not required to push your images to FAIRmat repositories. You can publish images to your own GitHub Container Registry (e.g., `ghcr.io/<your-username>/<your-repo>`) or any other registry you have access to.

### Jupyter-based tools
Jupyter-based NORTH tools provide users with an interactive computing environment for data analysis 
and visualization. These tools are particularly useful for exploratory data analysis, creating 
reproducible workflows, and sharing computational narratives.

#### Dockerfile Structure

A Dockerfile for a Jupyter-based NORTH tool typically consists of several stages. Here, we will go through a typical Dockerfile splitting the discussion in several parts. For a full example of the Dockerfile, follow [Dockerfile in cookiecutter-nomad-plugin](https://github.com/FAIRmat-NFDI/cookiecutter-nomad-plugin/blob/main/%7B%7Bcookiecutter.plugin_name%7D%7D/py_sources/src/north_tools/%7B%7Bcookiecutter.north_tool_name%7D%7D/Dockerfile) 

The build arguments at the top allow customization of the image:

```Dockerfile
ARG BASE_JUPYTER=quay.io/jupyter/scipy-notebook
ARG JUPYTER_TAG=2025-10-20
ARG UV_VERSION=0.9
ARG PLUGIN_NAME="PLUGIN"
FROM ghcr.io/astral-sh/uv:${UV_VERSION} AS uv_stage

FROM ${BASE_JUPYTER}:${JUPYTER_TAG} AS scipy_notebook
```

In this part of the Dockerfile, we define several [build variables](https://docs.docker.com/build/building/variables/). Unlike [ENV variables](https://docs.docker.com/build/building/variables/#environment-variables) that are available to the container at runtime, mind [scoping](https://docs.docker.com/build/building/variables/#scoping) of ARG variables.

- `BASE_JUPYTER`: Specifies the base Jupyter image (e.g., `<image-name>` like `quay.io/jupyter/scipy-notebook`)
- `JUPYTER_TAG`: Specifies the version tag of the base Jupyter image (e.g., `2025-10-20`)
- `UV_VERSION`: Specifies the version of the uv package manager image
- `PLUGIN_NAME`: Specifies the name of your plugin. Used for copying plugin code into the image. 
  If you want to keep the plugin code inside the image permanently, consciously comment out the cleanup line `RUN rm -rf ${HOME}/${PLUGIN_NAME}`.

We use a multi-stage build approach:
1. First stage (`uv_stage`): Copies the uv binary from the official uv image
2. Second stage (`scipy_notebook`): Builds on the Jupyter base image with uv included for environment management.

#### System Setup and Dependencies

Next, we configure the shell environment, copy the uv package manager, and install system dependencies:

```Dockerfile
# https://github.com/hadolint/hadolint/wiki/DL4006
# https://github.com/koalaman/shellcheck/wiki/SC3014
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

COPY --from=uv_stage /uv /uvx /bin/

USER root

# Define environment variables
# With pre-existing NB_USER="jovyan" and NB_UID=100, NB_GID=1000
ENV HOME=/home/${NB_USER}
ENV CONDA_DIR=/opt/conda

# Make ARG variables available as environment variables
ARG PLUGIN_NAME

RUN apt-get update \
 && apt-get install --yes --quiet --no-install-recommends \
      libmagic1 \
      file \
      build-essential \
      curl \
      zip \
      unzip \
      git

# By default scipy-notebook:2025-10-20 has node 18
# But, node > 20 needed for jupyterlab >= 4.4.10
RUN curl -fsSL https://deb.nodesource.com/setup_24.x | bash -

RUN apt-get install nodejs -y \
       && npm install -g configurable-http-proxy@^4.2.0 \
       # clean cache and logs
       && rm -rf /var/lib/apt/lists/* /var/log/* /var/tmp/* ~/.npm
```
**Key steps in this section:**

1. **Shell configuration**: Use bash with pipefail for safer script execution
2. **Copy uv binary**: Copies the uv package manager from the `uv_stage` for fast Python package installation
3. **Switch to root**: System packages require root privileges
4. **Environment variables**: Define `HOME` and `CONDA_DIR` for consistent paths
5. **System dependencies**: Install essential build tools, libraries, and utilities:
    - Build tools: `build-essential` (includes `gcc`, `g++`, `make`, and related tools)
    - Libraries: `libmagic1`
    - Utilities: `curl`, `git`, `zip`, `unzip`, `file`
6. **Node.js upgrade**: Install Node.js 24+ (required for JupyterLab >= 4.4.10, as the scipy-notebook base image typically includes Node.js 18)
7. **Cleanup**: Remove package manager cache to reduce image size

#### Python Dependencies and Final Setup

Finally, we switch back to the non-root user and install Python dependencies:

```Dockerfile
USER ${NB_USER}

# uv env
ENV UV_PROJECT_ENVIRONMENT=${CONDA_DIR} \
    UV_LINK_MODE=copy \
    UV_NO_CACHE=1 \
    # Use python from conda which is default for scipy-notebook
    # so that uv pip and pip both refer to the same python
    # If needed one can create another venv with 'uv venv'
    UV_SYSTEM_PYTHON=1 \

COPY --chown=${NB_USER}:${NB_GID} . ${HOME}/${PLUGIN_NAME}

WORKDIR ${HOME}/${PLUGIN_NAME}

# https://docs.astral.sh/uv/guides/integration/docker/#intermediate-layers
RUN --mount=type=cache,target=/root/.cache/uv \
    uv pip install . --group north

WORKDIR ${HOME}
RUN rm -rf ${HOME}/${PLUGIN_NAME}

RUN jupyter lab build --dev-build=False --minimize=False && \
    fix-permissions "/home/${NB_USER}" \ 
    && fix-permissions "${CONDA_DIR}"

WORKDIR ${HOME}

RUN touch ${HOME}/.hushlogin
```

**Key steps in this section:**

1. **Switch to non-root user**: Security best practice - run the application as `${NB_USER}` (typically `jovyan`)
2. **Configure uv**: Set environment variables for uv to work with the conda environment:
    - `UV_PROJECT_ENVIRONMENT`: Points to conda directory
    - `UV_SYSTEM_PYTHON`: Use system Python (conda's Python) instead of creating a new virtual environment
    - `UV_LINK_MODE=copy`: Copy packages instead of linking
    - `UV_NO_CACHE=1`: Disable caching to reduce image size
3. **Copy plugin code**: Copy your plugin source code into the container
4. **Install dependencies**: Use `uv pip install` to install dependencies from the `north` dependency group in `pyproject.toml`
5. **Cleanup plugin code**: Remove the plugin source code (unless you want to keep it)
6. **Build JupyterLab**: Compile JupyterLab extensions and assets
7. **Fix permissions**: Ensure proper file permissions for the user
8. **Configure startup**: Create `.hushlogin` to suppress login messages

The structure described above provides a solid foundation for Jupyter-based NORTH tools but not necessarily representing the exact Dockerfile you need. However, the concepts will help you to customize the [Dockerfile in cookiecutter-nomad-plugin](https://github.com/FAIRmat-NFDI/cookiecutter-nomad-plugin/blob/main/%7B%7Bcookiecutter.plugin_name%7D%7D/py_sources/src/north_tools/%7B%7Bcookiecutter.north_tool_name%7D%7D/Dockerfile) based on your specific requirements.

### Building the Image Locally

With such a Dockerfile, you can build the image locally for testing:

```bash
docker build -f src/<module_name>/north_tools/<tool_name>/Dockerfile \
  --build-arg PLUGIN_NAME=<plugin_name> \
  --build-arg JUPYTER_TAG=<jupyter_tag> \
  --build-arg UV_VERSION=<uv_version> \
  -t <image_name>:<tag> .
```

**Parameters:**
- `<module_name>`: Your Python module name (e.g., `nomad_example`)
- `<tool_name>`: Your NORTH tool name (e.g., `my_tool`)
- `<plugin_name>`: Your plugin name (e.g., `nomad-example-plugin`) Optionally can be left to default as code is removed after build process.
- `<jupyter_tag>`: Jupyter base image tag (e.g., `2025-10-20`) optionally can be left to default
- `<uv_version>`: UV version (e.g., `0.9`) optionally can be left to default
- `<image_name>`: Your image name (e.g., `my-jupyter-tool`)
- `<tag>`: Version tag (e.g., `latest`, `v1.0.0`)

**Example:**
```bash
docker build -f src/foobar/north_tools/my_tool/Dockerfile \
  --build-arg PLUGIN_NAME=foobar \
  --build-arg JUPYTER_TAG=2025-10-20 \
  --build-arg UV_VERSION=0.9 \
  -t ghcr.io/myusername/foobar:latest .
```

### Managing Python Dependencies

Python dependencies for your NORTH tool should be defined in the `pyproject.toml` file using dependency groups:

```toml
[dependency-groups]
north = [
    "jupyterlab",
    "ipywidgets",
    "pandas>=2.0.0",
    "matplotlib>=3.5.0",
    # Add your specific dependencies here
]
```

**Installation in Dockerfile:**

You can install these dependencies using either:

```Dockerfile
# Option 1: Install from dependency group (recommended)
RUN --mount=type=cache,target=/root/.cache/uv \
    uv pip install --group north

# Option 2: Full sync with locked dependencies
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --no-editable --extra=north --extra=nomad --inexact
```

### Adding Custom System Dependencies

If your tool requires additional system packages, add them to the `RUN apt-get install` section:

```Dockerfile
RUN apt-get update \
 && apt-get install --yes --quiet --no-install-recommends \
      # Essential packages
      libmagic1 \
      # Add your custom packages
      postgresql-client \
      graphviz \
      # Clean up
 && rm -rf /var/lib/apt/lists/* /var/log/* /var/tmp/*
```

### Adding JupyterLab Extensions

To include JupyterLab extensions, install them before building JupyterLab:

```Dockerfile
RUN uv pip install \
    jupyterlab-h5web \
    jupyterlab-git \
    # Add more extensions as needed
 && jupyter lab build --dev-build=False --minimize=False
```

### Tools requiring a Desktop environment

!!! tip "Important"

    While defining jupyter-based NORTH tools can be straightforward, desktop-based
    tools can be  more complicated. We will show a basic example here that will give
    the reader an idea on how the basic setup should look like. For more complicated cases
    (including those that need build tools, have special (local) licensing, or those that run
    software created for non-Linux environments), we refer to the existing example tools.

## Versioning and tagging `NORTH` images
When creating container images for NORTH tools, it is important to follow a consistent versioning
and tagging scheme.

### Tagging Strategy

**For local builds:** You can use any tag during development:
```bash
docker build ... -t my-tool:dev
```

**For published images:** Follow [semantic versioning (SemVer)](https://semver.org/):
- **Version tags**: `v1.0.0`, `v1.2.3`, etc. - Specific releases
- **latest tag**: Points to the most recent stable release
- **main/develop tags**: Track the main or development branch
- **PR tags**: `pr-123` for testing pull requests before merging

**GitHub Actions automatically creates:**
- `ghcr.io/<username>/<repo>:v1.0.0` - When you tag a release
- `ghcr.io/<username>/<repo>:main` - On push to main branch  
- `ghcr.io/<username>/<repo>:pr-123` - For pull request #123
- `ghcr.io/<username>/<repo>:latest` - Points to the latest tagged release  

## Testing NORTH tool
After successfully creating a Docker image for your NORTH tool, thorough testing ensures it functions 
correctly within the NOMAD environment.

### Local Testing

#### Interactive Testing

Run the container interactively with a local data mount:

```bash
docker run --rm -p 8888:8888 \
  --mount type=bind,src="/local/path/to/test/data",dst="/home/jovyan/test" \
  <image_name>:<tag>
```

**Then:**
1. Open your browser to `http://localhost:8888`
2. Navigate to the mounted test data
3. Test your analysis workflows
4. Verify all dependencies are working

#### Automated Notebook Execution

Test Jupyter notebooks non-interactively, i.e., run a container and execute a notebook inside it. Once the test is done, the container will exit and be removed.

```bash
docker run --rm -p 8888:8888 \
  --mount type=bind,src="/local/path/to/test/data",dst="/home/jovyan/test" \
  <image_name>:<tag> \
  /bin/bash -c "jupyter execute /home/jovyan/test/<path/to/notebook>.ipynb"
```

This validates that:
- All notebook cells execute without errors
- Dependencies are correctly installed
- Data can be read and processed

#### Testing with Shell Access

For debugging, run with an interactive shell:

```bash
docker run --rm -it \
  --mount type=bind,src="/local/path/to/test/data",dst="/home/jovyan/test" \
  <image_name>:<tag> \
  /bin/bash
```

Inside the container, you can check several things:

```bash
# Check installed packages
uv pip list
# or
pip list

# Verify Python version
python --version

# Test imports
python -c "import jupyterlab; print(jupyterlab.__version__)"

# Check JupyterLab
jupyter lab --version
```