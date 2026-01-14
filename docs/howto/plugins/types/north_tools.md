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
   │   ├── docker-publish-north.yaml
   ├── src
   │   ├── nomad_example
   │   │   ├── __init__.py
   │   │   ├── north_tools
   │   │   │   ├── __init__.py
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

### Juypter-based tools

### Tools requiring a Desktop environment

!!! tip "Important"

    While defining jupyter-based NORTH tools can be straightforward, desktop-based
    tools can be  more complicated. We will show a basic example here that will give
    the reader an idea on how the basic setup should look like. For more complicated cases
    (including those that need build tools, have special (local) licensing, or those that run
    software created for non-Linux environments), we refer to the existing example tools.

## Versioning and tagging `NORTH` images

## Testing NORTH tool

### Local testing

### Automated testing
