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
   |   │   │   │   ├── examples
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

The `NORTHTool` instance can be used to define which docker image the NORTH tools is to run.
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

Here you can see that a `NORTHTool` object called `tool` was defined. We also instantiate
the entry point object `my_north_tool` using the tool. This is the
final entry point instance in which you specify the default parameterization
and other details about the NORTH tools. In the reference you can see all of the
available configuration options for a [`NorthToolEntryPoint`](../../../reference/plugins.
md#northtoolentrypoint) and a [`NorthTool`](../../../reference/config.md#northtool).

The entry point instance should then be added to the `[project.entry-points.'nomad.plugin']`
table in `pyproject.toml` in order for it to be automatically
detected:

```toml
[project.entry-points.'nomad.plugin']
mynorthtool = "nomad_example.north_tools:my_north_tool"
```

## Creating `NORTH` images
The core of a NORTH tool is the container image that contains the actual software tools, examples,
and enviornment needed and so on to run the tool. In this section we will discuss how to create
such images. As a requirement, one needs to have [Docker](https://www.docker.com/get-started){:target="_blank" rel="noopener"}
installed on the local system. Which allows to build and test the images locally before publishing them
to a container registry. Otherways to create container images in an automated way (e.g., using CI/CD pipelines)
are also possible and which is our goal to do it and keep the images up to date automatically along with developments
of the nomad-plugin containing the NORTH tool.

- What to include in the discussion
   - Basic requreirements for NORTH images e.g., Docker installation, Find the a slim base image
   - Add a reference to the best practices for creating a Docker image from Docker docs
   - Docker registries (GHCR, DockerHub, Bitbucket etc)
   - TODO: Give links of the docker where one can read the documentation for corresponding docker commands.

### Juypter-based tools
The purpose of having Jupyter image based NORTH tools is to provide users with an interactive
environment for data analysis and visualization on the data that is generated and stored
using the plugins that is hosting this NORTH tool. Docker file should start with some arguments and the arguments can be used
to customize the image build. Here, you can customize the image according to your needs by adding
more dependencies, tools, and configurations. Then the variables are followed by the base image.

```Dockerfile
# Part from docker/Dockerfile.jupyter

# Global ARG variables
# ARG are accessible until the next FROM instruction
ARG BASE_JUPYTER=quay.io/jupyter/scipy-notebook
ARG JUPYTER_TAG=2025-10-20
ARG UV_VERSION=0.9
ARG PLUGIN_NAME="PLUGIN"
FROM ghcr.io/astral-sh/uv:${UV_VERSION} AS uv_stage

FROM ${BASE_JUPYTER}:${JUPYTER_TAG} AS scipy_notebook
```

In this part of the Dockerfile, we define several global (ARG are accessible  until the FROM instruction) arguments  
- `BASE_JUPYTER` specifies the base Jupyter image
- `JUPYTER_TAG` specifies the tag of the Jupyter base image
- `UV_VERSION` specifies the version of the UV image
- `PLUGIN_NAME` specifies the name of the plugin if someone wants to keep the entire plugin code inside the image 
    In this case conciously comment out the line `RUN rm -rf ${HOME}/${PLUGIN_NAME}` in dockerfile

Next we specify the shell environment, copy built uv files from uv stage to the current stage, make global ARG variables available as environment variables,
setup environment variables, and install required dependencies.

```Dockerfile
# Part from docker/Dockerfile.jupyter

# https://github.com/hadolint/hadolint/wiki/DL4006
# https://github.com/koalaman/shellcheck/wiki/SC3014
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

COPY --from=uv_stage /uv /uvx /bin/

USER root

# Define environment variables
# With pre-exinsting NB_USER="jovyan" and NB_UID=100, NB_GID=1000
ENV HOME=/home/${NB_USER}
ENV CONDA_DIR=/opt/conda

# Make ARG variables available as environment variables
ARG PLUGIN_NAME

RUN apt-get update \
 && apt-get install --yes --quiet --no-install-recommends \
      libgomp1 \
      libmagic1 \
      file \
      gcc \
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
 By coping the build uv files from the pre-built uv stage, we ensure that the necessary uv components are included in the final image and
 using uv as package manager.

Finally, we switch to the non-root user, setup uv environment variables, copy the plugin code into the image,
install dependencies using uv, build jupyter lab, clean up, and copy example files.

```Dockerfile
# Part from docker/Dockerfile.jupyter

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
# Install dependencies
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --no-editable --extra=north --extra=nomad --inexact

WORKDIR ${HOME}
RUN rm -rf ${HOME}/${PLUGIN_NAME}

RUN jupyter lab build --dev-build=False --minimize=False && \
    fix-permissions "/home/${NB_USER}" \ 
    && fix-permissions "${CONDA_DIR}"

WORKDIR ${HOME}

RUN touch ${HOME}/.hushlogin
```

The parts described above provide a basic structure for Dockerfiles used to create Jupyter-based docker images for NORTH tools.
Developers or users can customize these Dockerfiles further based on their specific requirements,
such as adding more dependencies, tools, and configurations.

With such a Dockerfile, one can build the image locally using the following command:

```bash
docker build -f src/<module_name>/north_tools/Dockerfile.jupyter --build-arg PLUGIN_NAME=<plugin_name> --build-arg \
--build-arg EXAMPLES_DIR=<examples_dir> -t <image_name>:<tag> .
```

The script `scripts/get_git_version.sh` is a simple script that extracts the current git version or tag of the plugin which comes with [template repository](https://github.com/FAIRmat-NFDI/nomad-plugin-template){:target="_blank" rel="noopener"} or one can write the following script in a file.

```bash
#!/bin/bash

# Find tagged version or construct dynamic version from latest tag, number of commits since tag and git hash
set -euo pipefail

git_semver() {
  # Tagged version
  if git describe --tags --exact-match >/dev/null 2>&1; then
    git describe --tags --exact-match | sed 's/^v//'
    return
  fi
  # Declare local variable for tag, commits, and hash
  local tag commits hash

  tag=$(git describe --tags --abbrev=0 2>/dev/null || echo "0.0.0")
  commits=$(git rev-list "${tag}"..HEAD --count 2>/dev/null || echo "0")
  hash=$(git rev-parse --short HEAD 2>/dev/null || echo "unknown")

  # Strip leading "v" if present
  tag=${tag#v}

  echo "${tag}+${commits}.g${hash}"
}

git_semver || echo "0.0.0+0.gunknown"
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
and tagging scheme. This helps users identify the correct version of the tool they need and
ensures compatibility with the NOMAD platform. For locally built image one can give any tag
in the build command as shown in the previous section. 
However, when publishing the images to a container registry, it is recommended to use semantic versioning (SemVer) for tagging the images and add an additinal
`latest` tag for the most recent stable release. Image with a tag according to the pull request can also be created for testing purposes before merging the pull request.  

## Testing NORTH tool
After successfully creating a docker image for your NORTH tool, it is crucial to test it thoroughly
to ensure that it functions as expected within the NOMAD environment. One can test the image by cteating
containers from the image either locally or using automated testing in a CI/CD pipeline.

### Local testing
For local testing, one needs to run corresponding image container by mounting the test data directory to the container. And then access the tool via a web browser. Here is an example command to run a Jupyter-based NORTH tool container locally:

```bash
docker run -p 8888:8888 --mount type=bind,src="/local/path/to/test/data",dst="/home/jovyan/work/test" <image_name>:<tag>
```
Or, Run a command that starts the image container and runs the command inside the container:

```bash
docker run --rm -p 8888:8888 --mount type=bind,src="/local/path/to/test/data",dst="/home/jovyan/test" <image_name>:<tag>  /bin/bash -c "jupyter execute /home/jovyan/test/<path/to/notebook>"
```

### Automated testing
To make the testing process developer amicable and to ensure that the Jupyter-based NORTH tools
work as expected after adding new features or version compatibility of the analysis software we recommend to set up automated testing using CI/CD pipelines. 
