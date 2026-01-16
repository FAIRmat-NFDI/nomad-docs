# NOMAD Remote Tools Hub (NORTH)

## Introduction

NORTH (NOMAD Remote Tools Hub) is NOMAD's hub for running data analysis and processing tools
in isolated, containerized environments. It enables tools to be executed reproducibly and
securely while being tightly integrated with the NOMAD data infrastructure.

NORTH provides a standardized way to run heterogeneous tools, written in different languages
and with different dependencies, without coupling them directly to the NOMAD core services.
It is designed for tasks such as data parsing, post-processing, analysis workflows, and the
generation of derived data products.

## Architecture

Architecturally, NORTH acts as a dedicated execution layer that is separate from the NOMAD
core services. Tools are executed as Docker containers, with each run isolated from other
tools and from the NOMAD services themselves. NOMAD is responsible for launching NORTH and
configuring the tools, while NORTH manages container startup, execution, and teardown.

NORTH provides a JupyterHub service as an interactive execution environment as part of its
architecture, allowing users to interactively work with NOMAD data using notebooks. In addition
to Jupyter-based workflows, NORTH can also host desktop-style tools packaged as containers, such
as remote GUI applications.

## User perspective

From a user’s perspective, NORTH can be used for running complex or tool-specific analyses
directly on data stored in NOMAD. Users do not need to download large datasets or install
analysis software locally; tools are executed remotely on NOMAD-managed infrastructure in
isolated Docker environments.

Unlike the central NOMAD services (which are optimized for data ingestion, storage, indexing,
and search), NORTH is designed for computationally intensive, tool-specific, or rapidly evolving
analyses. These include custom analysis software, post-processing steps, domain-specific
workflows, or tools with complex or conflicting dependencies that cannot reasonably be embedded
into the NOMAD core.

Tools running in NORTH operate directly on NOMAD-managed data. Inputs are taken from NOMAD
entries, and results can be written back (using the [NOMAD API](../howto/manage/program/api.md))
as derived data, metadata, or artifacts. Analyses executed via NORTH can be represented as NOMAD
entries that record inputs, parameters, tool versions, and outputs, establishing explicit provenance
links between original and derived data. This makes analyses reproducible, inspectable, and
shareable within NOMAD, which is especially important in collaborative research settings. Other
users can rerun the same analysis, apply it to new data, or build further processing steps on
top of the recorded results.

Compared to running software tools locally, running them remotely on NORTH inside isolated
Docker containers has several advantages for users:

- No local setup of analysis software or dependencies

- Consistent execution independent of the user’s operating system

- The ability to run analyses on large uploads that would be impractical to handle locally

## Using existing tools

NORTH does not implement analysis logic itself. Instead, it executes tools that are packaged
as Docker containers and registered with NOMAD. A number of such tools - maintained by FAIRmat -
are already provided as part of the NOMAD ecosystem.

<!--TODO: add exisiting tools here-->
<!--This section is intentionally left open to document which tools are currently available, where their
container images are maintained, and how they can be enabled in a given NOMAD deployment.-->
Our official recommendation is that desktop-based NORTH tools should be built on top of the `nomad-north-desktop-base` [docker image] (https://github.com/FAIRmat-NFDI/nomad-north-desktop-base). This image provides a [jupyter notebook](jupyter notebook) and graphical user interface that is provided via a light-weight [xfce]() desktop environment. Ubuntu Linux is the base layer of this docker image that connects thereby to the operation system of the host computer.


[the GitLab repositories of current NORTH tools](https://gitlab.mpcdf.mpg.de/nomad-lab/north)

## NORTH tool source code location

[Since its addition to NOMAD as a service](https://joss.theoj.org/papers/10.21105/joss.05388), the backend and docker images behind NORTH saw significant refactoring. Not only did the docker base images evolve substantially but also most services of NOMAD were refactored into plugins. NORTH tools with demands for a graphical user interface that were initially based on [Webtop](https://docs.linuxserver.io/images/docker-webtop/) are becoming replaced by one that is based on an image from the [Jupyter Docker Stacks project](https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html).

In this process, the storage location of the code that FAIRmat developed for NORTH changed. The [initial](https://gitlab.mpcdf.mpg.de/nomad-lab/nomad-remote-tools-hub) location is deprecated. The content in the location that was used [subsequently](https://gitlab.mpcdf.mpg.de/nomad-lab/north) is also in a process of refactoring that moves individual NORTH tools to a service that is anchored at the specific NOMAD parsers that fit best thematically and functionality-wise.

## Context, functionality, and status of each NORTH tool

### abtem

`abTEM` is a GUI-based NORTH tool offering software for research on electron microscopy. The tool bundles one version of [abTEM](https://abtem.readthedocs.io/en/latest/intro.html) (a software by [J. Madsen et al.](https://open-research-europe.ec.europa.eu/articles/1-24) for simulating dynamic electron diffraction using jupyter notebooks), one version of [VESTA](https://jp-minerals.org/vesta/en/) (a software by [K. Momma and F. Izumi](https://doi.org/10.1107/S0021889811038970), a stand-alone GUI application for generating and visualizing crystal structures), and one version of [GPAW](https://gpaw.readthedocs.io/) (a software package by [J. J. Mortensen, E. J. Enkovaara et al.](https://iopscience.iop.org/article/10.1088/0953-8984/22/25/253202) for command-line-based scripting of projector augmented-wave-based electronic structure simulations). **The container is to be moved to the [pynxtools-em](https://fairmat-nfdi.github.io/pynxtools-em/) plugin.** 

### apmtools

`apmtools` is a GUI-based NORTH tool offering software for research on atom probe microscopy. The tool bundles one version of [APTyzer](https://github.com/areichm/APTyzer) (a jupyter notebook by [A. Reichmann](https://pure.unileoben.ac.at/de/persons/alexander-reichmann/) for visually-guided composition analysis of atom-probe-reconstructed material volume), one version of [paraprobe](https://gitlab.com/paraprobe/) (a software by [M. Kühbach](https://doi.org/10.48550/arXiv.2205.13510) for Python and jupyter notebook-based scripting of data analyses for atom probe, and one version of [apav](https://apav.readthedocs.io/en/latest/index.html) (a Python and jupyter notebook-scripting focusing on analyses of multi-hit and mass spectra [J. Smith et al.](https://joss.theoj.org/papers/10.21105/joss.04862). **The container is to be moved to the [pynxtools-apm](https://fairmat-nfdi.github.io/pynxtools-apm/) plugin.** 
A summary of the specific data analyses offered by each tool of paraprobe is provided [here](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/apm-structure.html#cc-apm-structure).

base-desktop
ellips
fiji
jupyter
jupyterhub
mpes
nexus
nionswift
spm
sts
voila
xps


Learn more about running existing NOMAD tools in the how-tos:
[How-Tos> ... > How to analyze data in NORTH](../howto/manage/gui/north.md).

## Customization and user-provided tools

In addition to centrally provided tools, NORTH supports user-defined analysis software. Users
can package their own tools as Docker containers and run them via NORTH on NOMAD data.

This is especially relevant for [NOMAD Oasis](./oasis.md) deployments, where organizations operate
their own NOMAD instances. In this context, institution- or project-specific analysis software can
be integrated, including proprietary or licensed tools. Because execution happens within the
controlled environment of the Oasis deployment, such software does not need to be installed
on the NOMAD core system or exposed outside the local infrastructure.

### Writing and customizing containers

Developing a custom NORTH tool typically involves defining the tool logic and dependencies,
packaging the tool as a Docker container, and registering the container so that it can be
invoked via NOMAD. Once registered, custom tools follow the same execution and provenance model
as built-in tools.

Guidance on developing and registering custom NORTH tools is available in the how-tos:
[How to develop NORTH tools](../howto/plugins/types/north_tools.md).
