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

## Context, functionality, and status of base images for building NORTH tools

The constant refactoring that NORTH has experience brought changes to locations of docker images, brought updates on old images. Relevant for a given NOMAD deployment is always the specific YAML configuration YAML file that defines which of these and eventually other, custom NORTH tools, are bundled. The starting point and example for such a configuration file is the respective [default.yaml file from nomad-FAIR](https://gitlab.mpcdf.mpg.de/nomad-lab/nomad-FAIR/-/blob/develop/nomad/config/defaults.yaml)


### nomad-north-desktop-base

[`nomad-north-desktop-base`](https://github.com/FAIRmat-NFDI/nomad-north-desktop-base), previously [base-desktop](https://gitlab.mpcdf.mpg.de/nomad-lab/north/base-desktop/-/blob/main/Dockerfile?ref_type=heads) is the [Jupyter Docker Stacks project](https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html) base docker image that we consider as the best practice to build NORTH tools from when these should offer GUI elements.

### jupyter-notebook
<!--### nomad-north-jupyter-base-->
[jupyter notebook]
<!-- gitlab-registry.mpcdf.mpg.de/nomad-lab/nomad-distro/jupyter:develop -->
<!-- https://gitlab.mpcdf.mpg.de/nomad-lab/nomad-distro/container_registry/1462?orderBy=NAME&sort=asc&search[]=latest -->

## Context, functionality, and status of each NORTH tool

### abtem

[`abTEM`](https://gitlab.mpcdf.mpg.de/nomad-lab/north/abtem) is a GUI-based NORTH tool offering software for research on electron microscopy. The tool bundles one version of [abTEM](https://abtem.readthedocs.io/en/latest/intro.html) (a software by [J. Madsen et al.](https://open-research-europe.ec.europa.eu/articles/1-24) for simulating dynamic electron diffraction using jupyter notebooks), one version of [VESTA](https://jp-minerals.org/vesta/en/) (a software by [K. Momma and F. Izumi](https://doi.org/10.1107/S0021889811038970) for generating and visualizing crystal structures within a GUI application), and one version of [GPAW](https://gpaw.readthedocs.io/) (a software package by [J. J. Mortensen, E. J. Enkovaara et al.](https://iopscience.iop.org/article/10.1088/0953-8984/22/25/253202) for scripting projector augmented-wave-based electronic structure simulations using Python). **The container is to be renamed to nomad-north-abtem and moved to the [pynxtools-em](https://fairmat-nfdi.github.io/pynxtools-em/) plugin.** 

### apmtools

[`apmtools`](https://gitlab.mpcdf.mpg.de/nomad-lab/north/apmtools) is a GUI-based NORTH tool offering software for research on atom probe microscopy. The tool bundles one version of [APTyzer](https://github.com/areichm/APTyzer) (a jupyter notebook by [A. Reichmann](https://pure.unileoben.ac.at/de/persons/alexander-reichmann/) for visually-guided composition analysis of atom-probe-reconstructed material volume), one version of [paraprobe](https://gitlab.com/paraprobe/) (a software by [M. Kühbach](https://doi.org/10.48550/arXiv.2205.13510) for Python and jupyter-notebook-based scripting of data analyses for atom probe, and one version of [apav](https://apav.readthedocs.io/en/latest/index.html) (focusing on analyses of multi-hit and mass spectra [J. Smith et al.](https://joss.theoj.org/papers/10.21105/joss.04862) via a Python and jupyter notebooks. **The container is to be renamed to nomad-north-apmtools and moved to the [pynxtools-apm](https://fairmat-nfdi.github.io/pynxtools-apm/) plugin.** 
A summary of the specific data analyses offered by each tool of paraprobe is provided [here](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/apm-structure.html#cc-apm-structure).

### ellips

[`ellips`](https://gitlab.mpcdf.mpg.de/nomad-lab/north/ellips) is a jupyter-based NORTH tool offering software for research on ellipsometry. The tool implemented an example for converting data from an ellipsometry measurement on a Woollam instrument to NeXus/HDF5. In the past, the container exemplified also a subsequent data analysis of such measurements using the open-source optical spectroscopy data analysis software [PyElli](https://pyelli.readthedocs.io/en/stable/). The example focused on building a database of dispersive materials using the contributed NeXus application definition [NXdispersive_material](https://github.com/nexusformat/definitions/blob/main/contributed_definitions/NXdispersive_material.nxdl.xml) and related base classes. The proposal of these were [heavily discussed](https://github.com/nexusformat/definitions/pull/1424) at the [NIAC2024](https://www.nexusformat.org/NIAC2024_minutes.html) with questions raised if and how the NeXus standard should allow to include explicit formulas that could raise security concerns. No consensus was reached for NXdispersive-related classes, and the work discontinued. **Like for all method-specific pynxtools plugins, the conversion of data from domain-specific measurements to specific NeXus/HDF5 files can be achieved using every jupyter or Python capable NORTH tool provided it offers pynxtools and the respective domain-specific plugin is installed. Therefore, the ellips container is considered obsolete.**

<!-- shall we not add pynxtools to the jupyter base image?-->

### fiji

[`fiji`](https://gitlab.mpcdf.mpg.de/nomad-lab/north/fiji) is a GUI-based NORTH tool offering, [fiji](https://fiji.sc/) a frequently used extension of the [[imagej](https://imagej.net/ij/download.html) image processing and analysis software. The electron microscopy community is a frequent user of fiji given its covering set of custom image filters. The original motivation of FAIRmat for the fiji container was reaching out to electron microscopists working with focus series reconstruction, for which the container was configured to offer specific imagej/fiji plugins. **The container should be renamed to nomad-north-fiji and moved to [pynxtools-em](https://fairmat-nfdi.github.io/pynxtools-em/). It could also though stay with this name alone given its multi-community user base.**

### jupyter

**The [`jupyter`](https://gitlab.mpcdf.mpg.de/nomad-lab/north/jupyter) container should be replaced by the non-GUI jupyter image from Rubel renamed to nomad-north-jupyter ?.**

### jupyterhub

**The [`jupyterhub`](https://gitlab.mpcdf.mpg.de/nomad-lab/north/jupyterhub) container should be replaced by [nomad-north](https://github.com/FAIRmat-NFDI/nomad-north) ?**

### mpes

[`mpes`](https://gitlab.mpcdf.mpg.de/nomad-lab/north/mpes) is GUI-based NORTH tool offering software for research on multi photoemission spectroscopy (MPES). Apart from offering tutorials of a detailed data processing pipeline for converting, binning, and analyzing MPES data, the docker image exemplifies how [Igor Pro](https://www.wavemetrics.com/), a Windows based GUI application can be configured to offer its services via the browser within in a Linux environment coupled to NOMAD using the [wine](https://www.winehq.org/). **The container is to be renamed nomad-north-mpes and moved to the [pynxtools-mpes](https://fairmat-nfdi.github.io/pynxtools-mpes/) plugin.**
### nionswift

[`nionswift`](https://gitlab.mpcdf.mpg.de/nomad-lab/north/nionswift) is GUI-based NORTH tool offering the open-source image processing software [nionswift](https://nionswift.readthedocs.io/en/stable/) that is used especially in the research field of electron microscopy by users of [former Nion now Bruker](https://ir.bruker.com/press-releases/press-release-details/2024/Bruker-Acquires-Electron-Microscopy-Company-Nion/default.aspx) transmission electron microscopes. **The container is to be renamed nomad-north-nionswift and moved to the [pynxtools-em](https://fairmat-nfdi.github.io/pynxtools-em/) plugin.**

### pyiron

[`pyiron`](https://pyiron.org/) is a ? jupyter-based NORTH tool offering the pyiron software for implementing computational materials science as well as materials engineering simulation and data analysis [workflows](https://pythonworkflow.github.io/python-workflow-definition/README.html). The developed is driven and coordinated by the Department of Computational Materials Design at the [Max Planck Institute for Sustainable Materials Research](https://www.mpie.de/CM). **The container should be renamed nomad-north-pyiron**.

### spm and sts
[`spm`](https://gitlab.mpcdf.mpg.de/nomad-lab/north/spm) and [`sts`](https://gitlab.mpcdf.mpg.de/nomad-lab/north/sts) and are two jupyter-based NORTH tools offering examples for scanning probe microscopy and scanning tunneling probe spectroscopy. **The containers  are to be renamed nomad-north-spm and nomad-north-sts respectively, currently both are functionally similar, ideal would be to add a functionality that goes beyond mere conversion, to warrant relevance, and difference, for sure the containers should be moved to the [pynxtools-spm](https://fairmat-nfdi.github.io/pynxtools-spm/) plugin.**

### voila

[`voila`](https://gitlab.mpcdf.mpg.de/nomad-lab/north/voila) is a jupyter-based NORTH tool simplying the usage of jupyter notebooks via [voila](https://github.com/voila-dashboards/voila). The tool is currently developed by the Helmholtz Zentrum Berlin (HZB) and can thus be considered a user-provided NORTH tool. **voila as a tool can be helpful, but that container needs refactoring, firstly, rename to nomad-north-voila, secondly, why to keep HZB-specific customizations, key question, is that an officially supported container, I would say no right now.**

### xps

[`xps`](https://gitlab.mpcdf.mpg.de/nomad-lab/north/xps) is a jupyter-based NORTH tool offering software for research on core-level photoemission spectroscopy. The tool implemented an example for converting data from an XPS measurement to NeXus/HDF5 and perform data analyses. **Like mentioned for ellips, the container performs only the conversion, all content should be moved to the pynxtools-xps plugin, the container functionality should be extended or the container deprecated and instead generic conversion achieved with another container e.g. jupyter container.**


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
