# NOMAD Remote Tools Hub (NORTH)

## Introduction

NORTH (NOMAD Remote Tools Hub) is a NOMAD service for running tools in isolated
containerized environments that connect to NOMAD's data storage.
These reproducible and secure functionalities are accessible via the web browser.
NORTH provides a standardized way to run heterogeneous tools that are written in different
programming languages and with different dependencies, without coupling them directly
to the NOMAD core services.

## User perspective

From a user’s perspective, NORTH can be used for running complex or tool-specific analyses
directly on data that is stored inside NOMAD, be this API-retrievable input from NOMAD entries
or data from NOMAD projects. Results achieved within the container can be written back
(using the NOMAD API, see [How-to > ... > How to use the API](../howto/manage/program/api.md)) as derived data, metadata, or artifacts.
Reprocessing the project afterwards allows results obtained with NORTH to be indexed,
provided that the software tools in NORTH write using data structures and schemas
that NOMAD understands. The reprocessing can be triggered through the API or the NOMAD GUI.

The connection between the container and the NOMAD file system removes the need
for copying and downloading large datasets. Container images remove the need for installing
analysis software locally and assure consistent execution independent of the user's operating
system. Instead, the tools are executed remotely within the infrastructure
that a NOMAD deployment provides. These capabilities of NORTH are especially important in
collaborative research settings enabling other users to rerun the same analysis, or apply
existent parameterizations to new data. Provided a server installation and cloud configuration
is used, this also enables to spawn multiple instances of the same tool.

Unlike the central NOMAD services (which are optimized for data ingestion, storage, indexing,
and search), NORTH is designed for computationally intensive, tool-specific, or rapidly evolving
analyses. These include custom analysis software, post-processing steps, domain-specific
workflows, or tools with complex or conflicting dependencies that cannot reasonably be embedded
into the NOMAD core.

## Architecture

Architecturally, NORTH acts as a dedicated execution layer that is separate from the
NOMAD core services. Tools are executed as Docker containers, with each run isolated
from other tools and the NOMAD services themselves. NOMAD is responsible for launching
NORTH and configuring the tools, while NORTH is responsible for managing container startup,
execution, and teardown, all managed through its JupyterHub service.

## Using existing tools

NORTH does not implement analysis logic itself. Instead, it executes tools that are packaged
as Docker containers and registered with NOMAD. Several such tools, maintained by FAIRmat,
are already available as NOMAD plugins. These tools are based on either Jupyter- or desktop-based images.
Custom containers can also be created and connected to the service.

## How to connect and use specific NORTH tools in a NOMAD deployment

A NORTH tool becomes available in a deployment simply by adding its plugin package as a
dependency (e.g. in `pyproject.toml`). NOMAD automatically discovers the `NORTHToolEntryPoint` it defines and lists it in the NORTH tools registry. To reconfigure an already-installed tool in a deployment (for example, swapping in a custom image instead of the plugin's default one), override its entry point in your `nomad.yaml`:

```yaml
plugins:
  entry_points:
    options:
      nomad_north_jupyter.north_tools:jupyter:
        north_tool:
          image: ghcr.io/fairmat-nfdi/nomad-north-jupyter:<another_tag>
```

The NORTH hub reads the tool configuration from NOMAD when it starts. After changing a tool in `nomad.yaml`, restart both the `app` and the `north` services.

### Using a locally built image

By default, NORTH tools use `image_pull_policy: Always`: the NORTH hub pulls the image from its registry every time a tool is started. This keeps moving tags such as `latest` up to date, but it also means that:

- an image that only exists locally (e.g. `my-tool:dev`) cannot be started. The hub fails with an error like `pull access denied for my-tool, repository does not exist`.
- a local build that reuses the tag of a published image (e.g. `ghcr.io/fairmat-nfdi/nomad-north-jupyter:latest`) is replaced by the published image every time the tool starts.

To run a locally built image, set `image_pull_policy` to `IfNotPresent` (pull only if the image is missing) or `Never` (never pull, only use local images):

```yaml
plugins:
  entry_points:
    options:
      nomad_north_jupyter.north_tools:jupyter:
        north_tool:
          image: my-tool:dev
          image_pull_policy: IfNotPresent
```

The image has to be available to the Docker daemon that runs the tool containers, which in a Docker Compose deployment is the Docker daemon of the host.

!!! tip

    In [`nomad-distro-template`](https://github.com/FAIRmat-NFDI/nomad-distro-template){:target="_blank" rel="noopener"}, the `jupyterlab_image` service in `docker-compose.yaml` only exists to pre-pull the default Jupyter image and uses `pull_policy: always`. If you point `JUPYTER_IMAGE` to a local image, change its `pull_policy` to `missing`, otherwise `docker compose up` fails trying to pull it.

### Mounting additional host directories

Use `external_mounts` to make additional directories, for example a shared data or software folder, available in every container of a tool:

```yaml
plugins:
  entry_points:
    options:
      nomad_north_jupyter.north_tools:jupyter:
        north_tool:
          external_mounts:
            - host_path: /data/shared
              bind: shared
              mode: ro
```

- `host_path` is an absolute path **on the host** that runs the tool containers. The tool containers are started by the host's Docker daemon (or Kubernetes node), so this is not a path inside the NOMAD or NORTH containers, and relative paths are not supported.
- `bind` is the target path in the tool container. A relative path is resolved against the `mount_path` of the tool. For the Jupyter tool, the example above becomes `/home/jovyan/shared`. An absolute path is used as is.
- `mode` is either `ro` (read-only, the default) or `rw` (writable). The same directory is mounted for every user of the tool, so only use `rw` for data that all users can share. For writable mounts, make sure the container user (`jovyan`, UID `1000`, for Jupyter-based tools) has write permissions on the host directory.

!!! warning

    The NORTH hub image `nomad-north:2.0.1` fails to start when a tool defines `external_mounts`, with the error `PydanticUserError: NORTHExternalMount is not fully defined; you should define ReadMode`. Use a later version of the hub image.

## Official base images

Using the base image within the [`nomad-north-desktop-base`](https://github.com/FAIRmat-NFDI/nomad-north-desktop-base){:target="_blank" rel="noopener"} repository is the recommended best practice to build a NORTH tool if that demands a graphical user interface. Its desktop-base image builds on the [Jupyter Docker Stacks project](https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html){:target="_blank" rel="noopener"}, offering a [conda](https://anaconda.org){:target="_blank" rel="noopener"} environment with a Jupyter Notebook and graphical user interface via a light-weight [`xfce`](https://www.xfce.org/){:target="_blank" rel="noopener"} desktop environment. Ubuntu Linux is the base layer of this docker image, connecting the container to the operation system of the host computer.

Using the base image within the [nomad-plugin-template](https://github.com/FAIRmat-NFDI/nomad-plugin-template){:target="_blank" rel="noopener"} repository is the recommended best practice to build a NORTH tool from if it does not demand a graphical user interface. Note that this repository is the template for building NOMAD plugins.

[How-to guides > ... > How to create a NORTH tool](../howto/plugins/types/north_tools.md) provides instructions for building from these images.

## Specific NORTH tools

Consult the reference section of the documentation to find details about individual NOMAD plugins and the eventual NORTH tools these provide.

<!-- TODO: once there is a nomad-registry on the homepage (https://gitlab.mpcdf.mpg.de/nomad-lab/nomad-lab-homepage/-/work_items/12), change the sentence above to
Users should consult the [NOMAD plugin registry](<add-link>>) which details which plugins offer NORTH tool entry points.-->

## Custom user-provided tools

In addition to centrally provided tools, users can package their own tools as Docker containers
and run these via NORTH on NOMAD data. This is especially relevant for organizations and users
who run their own [NOMAD Oasis](./oasis.md) deployment. In this context, institution- or project-specific analysis software may call for connecting proprietary or tools whose license does not allow exposing services outside the local infrastructure. Given that the requirements of NORTH can be decoupled from those of the NOMAD core system is a clear user benefit.

Developing a custom NORTH tool typically involves defining the tool logic and dependencies,
packaging the tool as a Docker container, and registering the container so that it can be
invoked via NOMAD. Once registered, custom tools follow the same execution and provenance model
as built-in tools.

Guidance on developing and registering custom NORTH tools is available in
[How to > Plugins > Develop a NORTH tool](../howto/plugins/types/north_tools.md).

## Data schema interoperability

Beyond its importance for managing the expectations as to how NOMAD reacts to and what
individual NORTH tools offer, it is important to know that using different data schemas
in a NORTH tool compared to the NOMAD deployment does not always come without challenges.

Users may encounter issues when reprocessing projects that contain results from a NORTH tool
analysis, if the tool wrote data using a schema version different from the one used in the
NOMAD deployment. This can lead to partial or complete incompatibilities. By providing
individual NORTH tools as optional extensions of a NOMAD plugin, the responsibility
for minimizing schema incompatibilities is shifted to the plugin developers.

All FAIRmat NORTH tools use the NOMAD plugin mechanism to provide the tools *via* a `NORTHToolEntryPoint`. It is recommended for NOMAD Oasis admins to use these plugins in their deployments (rather than older NORTH tool description using other mechanisms). Developers of existing or new external tools are also encouraged to use the plugin entry point mechanism.
