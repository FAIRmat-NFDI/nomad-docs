# How to create a NORTH tool

NORTH (NOMAD Remote Tools Hub) is NOMAD's hub for running data analysis tools in isolated,
containerized environments. It enables tools to be executed reproducibly and securely while
being tightly integrated with the NOMAD data infrastructure.

This documentation shows you how to create a plugin entry point for a NORTH tool and prepare its contents.
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
   │   │   │   ├── my_tool
   │   │   │   │   ├── __init__.py
   │   │   │   │   ├── Dockerfile
   │   │   │   │   └── README.md
   │   │   │   └── __init__.py
   ├── LICENSE.txt
   ├── README.md
   ├── Dockerfile
   └── pyproject.toml
```

See the documentation on [plugin development guidelines](../plugins.md#plugin-development-guidelines)
for more details on the best development practices for plugins, including linting, testing, and documenting.

## NORTH tool entry point

The entry point defines basic information about your NORTH tool and is used to
automatically load it into a NOMAD distribution. It is an instance of a
`NORTHToolEntryPoint` or its subclass.

The `NORTHTool` instance can be used to setup the tool configuration, including which Docker image it uses.
You will learn more about creating these images in the [next section](#creating-north-images). The entry point should be defined
in `*/north_tools/my_tool/__init__.py` like this:

<!-- markdownlint-disable MD044 -->
```py
from nomad.config.models.north import NORTHTool
from nomad.config.models.plugins import NORTHToolEntryPoint

tool = NORTHTool(
    image='ghcr.io/FAIRMat-NFDI/nomad-example:latest',
    description='An example Jupyter Notebook served in NORTH',
    external_mounts=[],
    file_extensions=['ipynb'],
    icon='logo/jupyter.svg',
    image_pull_policy='Always',
    default_url='/lab',
    maintainer=[{'email': 'fairmat@physik.hu-berlin.de', 'name': 'John Doe'}],
    mount_path='/home/jovyan',
    privileged=False,
    with_path=True,
    display_name='MyTool',
)

my_north_tool = NORTHToolEntryPoint(id='my-north-tool', north_tool=tool)
```

!!! tip "Important"
    To test a Docker image in NOMAD, you do not need to publish the Docker image in a registry. You can build it locally and set `image` to a local tag (e.g., `my-tool:dev`) in the `NORTHTool` configuration. The NOMAD checks for a local image first before pulling from a registry.

Here you can see that a `NORTHTool` object called `tool` was defined. We also instantiate
the entry point object `my_north_tool` using the tool. This is the
final entry point instance in which you specify the default parameterization
and other details about the NORTH tool. In the reference you can see all of the
available configuration options for a [`NORTHToolEntryPoint`](../../../reference/plugins.md#northtoolentrypoint) and a [`NORTHTool`](../../../reference/config.md#northtool).

The entry point instance should then be added to the `[project.entry-points.'nomad.plugin']`
table in `pyproject.toml` in order for it to be automatically detected:

```toml
[project.entry-points.'nomad.plugin']
mynorthtool = "nomad_example.north_tools.my_tool:my_north_tool"
```

## Creating NORTH images

The core of a NORTH tool is the container image that contains the actual software tools, examples,
and environment needed to run the tool. In this section we will discuss how to create
such images. Docker images can be built either locally or remotely (via the GitHub or GitLab CI).

### Prerequisites

Before creating NORTH images, ensure you have:

- **Docker installed**: [Get Docker](https://www.docker.com/get-started){:target="_blank" rel="noopener"} installed on your local system. This allows you to build and test images locally before publishing.
- **Container registry access**: Access to a container registry for publishing your images if you plan to store your images remotely for long-term use.

!!! tip "Important"
    For Docker best practices, refer to the [official Docker documentation](https://docs.docker.com/develop/dev-best-practices/){:target="_blank" rel="noopener"}.

!!! tip "Important"

    NORTH tools support images from all public container registries:

    - **GitHub Container Registry (GHCR)**: `ghcr.io/<username>/<image-name>` - Recommended for GitHub-hosted projects. Integrates seamlessly with GitHub Actions.
    - **Docker Hub**: `docker.io/<username>/<image-name>` - Popular public registry with free tier for public images.
    - **Quay.io**: `quay.io/<username>/<image-name>` - Red Hat's container registry with strong security features.

!!! tip "Important"
    You are not required to push your images to FAIRmat repositories. Only FAIRmat maintainers can publish to FAIRmat registries. You can publish images to your own GitHub Container Registry (e.g., `ghcr.io/<your-username>/<your-repo>`) or any other registry you have access to.

### Jupyter-based tools

Jupyter-based NORTH tools provide users with an interactive computing environment for data analysis
and visualization.

#### Dockerfile structure

A Dockerfile for a Jupyter-based NORTH tool typically consists of several stages. Here, we will go through a typical Dockerfile splitting the discussion in several parts. You can find a full example of a Dockerfile for a Jupyter-based NORTH tool in [nomad-north-jupyter](https://github.com/FAIRmat-NFDI/nomad-north-jupyter/blob/main/src/nomad_north_jupyter/north_tools/jupyter_north_tool/Dockerfile){:target="_blank" rel="noopener"}

The build arguments at the top allow customization of the image:

```Dockerfile
ARG BASE_JUPYTER=quay.io/jupyter/scipy-notebook
ARG JUPYTER_TAG=2025-10-20
ARG UV_VERSION=0.9
ARG PLUGIN_NAME="PLUGIN"
FROM ghcr.io/astral-sh/uv:${UV_VERSION} AS uv_stage

FROM ${BASE_JUPYTER}:${JUPYTER_TAG} AS scipy_notebook
```

In this part of the Dockerfile, we define several [build variables](https://docs.docker.com/build/building/variables/){:target="_blank" rel="noopener"}. Unlike [ENV variables](https://docs.docker.com/build/building/variables/#environment-variables){:target="_blank" rel="noopener"} that are available to the container at runtime, ARG variables are [scoped](https://docs.docker.com/build/building/variables/#scoping){:target="_blank" rel="noopener"} to the build stage in which they are defined.

- `BASE_JUPYTER`: Specifies the base Jupyter image (e.g., `<image-name>` like `quay.io/jupyter/scipy-notebook`)
- `JUPYTER_TAG`: Specifies the version tag of the base Jupyter image (e.g., `2025-10-20`)
- `UV_VERSION`: Specifies the version of the [`uv` package manager](https://docs.astral.sh/uv/){:target="_blank" rel="noopener"} via Docker [image](https://docs.astral.sh/uv/guides/integration/docker/#getting-started){:target="_blank" rel="noopener"}
- `PLUGIN_NAME`: Specifies the name of your plugin. Used for copying plugin code into the image.
  If you want to keep the plugin code inside the image permanently, consciously comment out the cleanup line `RUN rm -rf ${HOME}/${PLUGIN_NAME}`.

We use a multi-stage build approach: In the first stage (`uv_stage`) copies the `uv` binary from the official `uv` image. In the second stage (`scipy_notebook`) builds on the Jupyter base image with `uv` included for environment management.

#### System setup and dependencies

Next, we configure the shell environment, copy the [`uv` package manager](https://docs.astral.sh/uv/){:target="_blank" rel="noopener"}, and install system dependencies:

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

The key steps in this stage are:

1. **Shell configuration**: Use bash with pipefail for safer script execution
2. **Copy `uv` binary**: Copies the [`uv` package manager](https://docs.astral.sh/uv/){:target="_blank" rel="noopener"} from the `uv_stage` for fast Python package installation
3. **Switch to root**: Installing system packages require root privileges
4. **Environment variables**: Define `HOME` and `CONDA_DIR` for consistent paths
5. **System dependencies**: Install essential build tools, libraries, and utilities:
    - Build tools: `build-essential` (includes `gcc`, `g++`, `make`, and related tools)
    - Libraries: `libmagic1`
    - Utilities: `curl`, `git`, `zip`, `unzip`, `file`
6. **Node.js upgrade**: Install `Node.js` 24+ (required for `JupyterLab >= 4.4.10`, as the scipy-notebook base image typically includes `Node.js` 18)
7. **Cleanup**: Remove package manager cache to reduce image size

#### Python dependencies and final setup

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
    UV_SYSTEM_PYTHON=1

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

The key steps in this section are:

1. **Switch to non-root user**: Security best practice - run the application as `${NB_USER}` (typically `jovyan`)
2. **Configure uv**: Set environment variables for `uv` to work with the conda environment:
    - `UV_PROJECT_ENVIRONMENT`: Points to conda directory
    - `UV_SYSTEM_PYTHON`: Use system Python (conda's Python) instead of creating a new virtual environment
    - `UV_LINK_MODE=copy`: Copy packages instead of linking
    - `UV_NO_CACHE=1`: Disable caching to reduce image size
3. **Copy plugin code**: Copy your plugin source code into the container
4. **Install dependencies**: Use `uv pip install` ( or `uv pip install .`, to install the NOMAD plugin as well) to install dependencies from the `north` dependency group in `pyproject.toml`
5. **Cleanup plugin code**: Remove the plugin source code (unless you want to keep it)
6. **Build JupyterLab**: Compile JupyterLab extensions and assets
7. **Fix permissions**: Ensure proper file permissions for the user
8. **Configure startup**: Create `.hushlogin` to suppress login messages

The structure described above provides a solid foundation for Jupyter-based NORTH tools but does not necessarily represent the exact Dockerfile you need. However, these building blocks will help you to customize the [Dockerfile in cookiecutter-nomad-plugin](https://github.com/FAIRmat-NFDI/cookiecutter-nomad-plugin/blob/main/%7B%7Bcookiecutter.plugin_name%7D%7D/py_sources/src/north_tools/%7B%7Bcookiecutter.north_tool_name%7D%7D/Dockerfile){:target="_blank" rel="noopener"} based on your specific requirements.

### Building the image locally

With such a Dockerfile, you can build the image locally for testing:

```bash
docker build -f src/<module_name>/north_tools/<tool_name>/Dockerfile -t <image_name>:<tag> .
```

Parameters:

- `<module_name>`: Your Python module name (e.g., `nomad_example`)
- `<tool_name>`: Your NORTH tool name (e.g., `my_tool`)
- `<image_name>`: Your image name (e.g., `my-jupyter-tool`)
- `<tag>`: Version tag (e.g., `latest`, `v1.0.0`)

The default values of all build arguments (like `PLUGIN_NAME`, `JUPYTER_TAG`, `UV_VERSION`, etc.) can be changed in the build call by passing along `--build-arg <BUILD-ARG>=<new-value>`.

Example:

```bash
 docker build -f src/foobar/north_tools/my_tool/Dockerfile \
  --build-arg PLUGIN_NAME=foobar \
  --build-arg JUPYTER_TAG=2025-10-20 \
  --build-arg UV_VERSION=0.9 \
  -t ghcr.io/myusername/foobar:latest .
```

### Managing Python dependencies

Python dependencies for your NORTH tool should be defined in the `pyproject.toml` file using [dependency groups](https://packaging.python.org/en/latest/specifications/dependency-groups/){:target="_blank" rel="noopener"}:

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

### Tools requiring a Desktop environment

!!! tip "Important"

    While defining Jupyter-based NORTH tools can be straightforward, desktop-based
    tools are often more complicated to build. This section shows the base setup that every
    desktop-based NORTH tool shares, the different ways existing tools install their
    application, and more complicated cases (build tools, special local licensing,
    non-Linux software).

#### Dockerfile contents

Desktop-based NORTH tools typically build `FROM` the shared
[`nomad-north-desktop-base`](https://github.com/FAIRmat-NFDI/nomad-north-desktop-base){:target="_blank" rel="noopener"}
image (see [Explanation > NORTH > Official base images](../../../explanation/north.md#official-base-images)), rather than assembling xfce/VNC from scratch. Every existing desktop-based tool follows the same skeleton:

<!-- markdownlint-disable MD044 -->
```Dockerfile
ARG IMAGE_TAG=main
ARG BASE_IMAGE=ghcr.io/fairmat-nfdi/nomad-north-desktop-base

FROM ${BASE_IMAGE}:${IMAGE_TAG} AS base

SHELL ["/bin/bash", "-o", "pipefail", "-c"]

USER root

# ... install the application here (see below) ...

# Switch back to jovyan to avoid accidental container runs as root
USER ${NB_UID}
WORKDIR "${HOME}"

# ... copy desktop-integration files here (see below) ...
```

Installs that need root (apt packages, writing outside `${HOME}`) happen as `USER root`;
everything that touches `${HOME}` (desktop shortcuts, extensions, application data) happens
after switching back to `USER ${NB_UID}`.

#### Installing the application

Which approach to use depends entirely on how the application that you want to install in your NORTH container is distributed. Four patterns are actively used by existing NORTH tools:

| Pattern | Use when | Example in a Dockerfile | Key steps |
| --- | --- | --- | --- |
| **apt package** | the tool is already packaged for Ubuntu | [`nomad-north-gwyddion`](https://github.com/FAIRmat-NFDI/nomad-north-gwyddion/blob/main/src/nomad_north_gwyddion/north_tools/gwyddion/Dockerfile){:target="_blank" rel="noopener"} | `apt-get install gwyddion` |
| **Downloaded archive extraction** | the tool ships as a prebuilt tarball with no package | [`nomad-north-vesta`](https://github.com/FAIRmat-NFDI/nomad-north-vesta/blob/main/src/nomad_north_vesta/north_tools/vesta/Dockerfile){:target="_blank" rel="noopener"}, [`nomad-north-fiji`](https://github.com/FAIRmat-NFDI/nomad-north-fiji/blob/main/src/nomad_north_fiji/north_tools/fiji/Dockerfile){:target="_blank" rel="noopener"} | `wget` a `.tar.bz2` + `tar -xvf` (vesta), or a `.zip` + `unzip` (fiji) |
| **AppImage extraction** | the tool is only shipped as an AppImage | [`nomad-north-nionswift`](https://github.com/FAIRmat-NFDI/nomad-north-nionswift/blob/main/src/nomad_north_nionswift/north_tools/nionswift/Dockerfile){:target="_blank" rel="noopener"} | `wget` the `.AppImage`, `--appimage-extract`, symlink `AppRun` |
| **Full mamba/conda environment** | a Python/Qt-GUI-heavy toolkit with its own complex dependency graph, not a single binary | [`nomad-north-apmtools`](https://github.com/FAIRmat-NFDI/nomad-north-apmtools/blob/main/src/nomad_north_apmtools/north_tools/apmtools/Dockerfile){:target="_blank" rel="noopener"} | `mamba env create -f environment.yml`, registered as a Jupyter kernel, auto-activated via `.bashrc` |

A native desktop application installed from a vendor's own apt repository (rather than Ubuntu's)
is a variant of pattern 1 (see the VS Code example below).

#### Desktop integration

A `.desktop` file placed in different locations means different things, and existing NORTH tools use different combinations depending on the intended user experience:

| Location | Effect | Use for |
| --- | --- | --- |
| `~/.local/share/applications/*.desktop` | Adds a menu entry; the user launches the tool manually | A secondary tool that users may only open occasionally |
| `~/.config/autostart/*.desktop` | Launches automatically every session | The main tool that the container was built for |
| `~/Desktop/*.desktop` | Places an icon on the desktop itself | Can be in addition to its autostart entry |

It is also possible to copy the *same* file into both the applications and autostart
directories: the tool auto-launches, but there's still a way to relaunch it if the user closes
it. Using autostart alone means there is no way to reopen the tool afterwards without restarting the whole container.

#### Example: adding VS Code

In order to provide a native desktop version of VS Code on top of the desktop base image, the following should be added to the Dockerfile:

```Dockerfile
# ---- VS Code (native desktop app, not code-server) ----
RUN curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > /etc/apt/trusted.gpg.d/microsoft.gpg \
 && sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list' \
 && apt-get update -y \
 && apt-get install -y code \
 && apt-get clean && rm -rf /var/lib/apt/lists/*

# after switching to USER ${NB_UID}:
# DONT_PROMPT_WSL_INSTALL suppresses the `code` CLI's interactive "install inside WSL
# anyway?" prompt, which appears when the build host's kernel identifies as WSL (e.g.
# Docker Desktop on WSL2).
ENV DONT_PROMPT_WSL_INSTALL=1
RUN /usr/bin/code --install-extension eamodio.gitlens \
 && /usr/bin/code --install-extension h5web.vscode-h5web \
 && /usr/bin/code --install-extension ms-toolsai.jupyter \
 # ... etc, pick the extensions relevant to your tool
```

The desktop icon (`code.desktop`, the file VS Code itself ships) is copied to `~/Desktop/`, and
an autostart script marks that icon's checksum as trusted so double-clicking it doesn't trigger
xfce's "untrusted launcher" prompt:

```bash
# ~/.config/autostart/autostart, run once per session via a matching autostart.desktop entry
f=/home/jovyan/Desktop/code.desktop
gio set -t string "$f" metadata::xfce-exe-checksum "$(sha256sum "$f" | awk '{print $1}')"
```

#### More complex cases

1. **Dependencies that need build tools.** Some Python dependencies ship no prebuilt wheel for
   the image's Python version and have to compile from source. The failure mode is a clear message from the installer (e.g. `error: [Errno 2] No such file or directory: 'gcc'`), not something cryptic. If you see that, the fix is almost always adding the missing apt package directly in the Dockerfile.

2. **Special (local) licensing.**
NOMAD Oasis admins may sometimes want to install proprietary tools for which only a particular research group has a licence. These tools cannot be committed to a public repository. The usual approach is to keep the Dockerfile and desktop integration in the open repository, while providing the licensed installer or other required files separately as a local build input. It should be clearly documented in that package's own `README.md` or documentation what needs to be provided, for example: “Place your licensed installer at `./vendor-tool` before running `docker build`.” The local files should also typically be added to `.gitignore`. A package built this way also **cannot** use an automatic build/publish workflow on GitHub Actions, as the the image needs to be built and distributed manually by whoever holds a license.

3. **Software built for non-Linux environments.** Windows-only tools can run via
   [Wine](https://www.winehq.org/){:target="_blank" rel="noopener"} on top of the same
   desktop-base image. Add the WineHQ apt repository and install it, as `USER root`:

    ```Dockerfile
    # ---- Wine (for Windows-only applications) ----
    RUN dpkg --add-architecture i386 \
     && mkdir -pm755 /etc/apt/keyrings \
     && wget -O /etc/apt/keyrings/winehq-archive.key https://dl.winehq.org/wine-builds/winehq.key \
     && wget -nc -P /etc/apt/sources.list.d/ \
          https://dl.winehq.org/wine-builds/ubuntu/dists/$(lsb_release -sc)/winehq-$(lsb_release -sc).sources \
     && apt-get update -y \
     && apt-get install -y --install-recommends winehq-staging \
     && apt-get clean && rm -rf /var/lib/apt/lists/*
    ```

    Treat the actual Windows application the same as the licensing case above if
    it's proprietary: `COPY` a locally-supplied Wine prefix (never committed) into
    `${HOME}/.wine`, plus a `.desktop` shortcut for it, as `USER ${NB_UID}`:

    ```Dockerfile
    USER ${NB_UID}
    COPY --chown=${NB_UID}:${NB_GID} vendor-tool-wine "${HOME}/.wine"
    COPY --chown=${NB_UID}:${NB_GID} config/VendorTool.desktop "${HOME}/Desktop/VendorTool.desktop"
    ```

## Versioning and tagging NORTH images

When creating container images for NORTH tools, it is important to follow a consistent versioning
and tagging scheme.

### Tagging strategy

For local builds, you can use any tag during development:

```bash
docker build ... -t my-tool:dev
```

For published images, you may follow [semantic versioning (SemVer)](https://semver.org/){:target="_blank" rel="noopener"}:

- **Version tags**: `v1.0.0`, `v1.2.3`, etc. - Specific releases
- **latest tag**: Points to the most recent stable release
- **main/develop tags**: Track the main or development branch

GitHub Actions automatically creates:

- `ghcr.io/<username>/<repo>:v1.0.0` - When you tag a release
- `ghcr.io/<username>/<repo>:main` - On push to main branch
- `ghcr.io/<username>/<repo>:latest` - Points to the latest tagged release

## Testing NORTH tool

After having successfully created a Docker image for your NORTH tool, thorough testing ensures it functions correctly.

### Local testing

#### Interactive testing

Run the container interactively with a local data mount:

```bash
docker run --rm -p 8888:8888 \
  --mount type=bind,src="/local/path/to/test/data",dst="/home/jovyan/test" \
  <image_name>:<tag>
```

Then,

1. Open your browser to `http://localhost:8888`
2. Navigate to the mounted test data
3. Test your analysis workflows
4. Verify all dependencies are working

#### Automated notebook execution

You can also test the container non-interactively, i.e., run the container and execute a Jupyter notebook inside it. Once the test is done, the container will exit and be removed.

```bash
docker run --rm -p 8888:8888 \
  --mount type=bind,src="/local/path/to/test/data",dst="/home/jovyan/test" \
  <image_name>:<tag> \
  /bin/bash -c "jupyter execute /home/jovyan/test/<path/to/notebook>.ipynb"
```

This validates that,

- All notebook cells execute without errors
- Dependencies are correctly installed
- Data can be read and processed
