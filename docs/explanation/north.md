# NOMAD Remote Tools Hub (NORTH)

## Introduction

NORTH (NOMAD Remote Tools Hub) is a NOMAD service of data parsing and analysis tools
which runs in isolated containerized environments that connect to NOMAD's data storage.
These reproducible and secure functionalities are accessible via the web browser.
NORTH provides a standardized way to run heterogeneous tools that are written in different
programming languages and with different dependencies, without coupling them directly
to the NOMAD core services.

## User perspective

From a user’s perspective, NORTH can be used for running complex or tool-specific analyses
directly on data that is stored inside NOMAD, be this API-retrievable input from NOMAD entries
or data from ones uploads. Results achieved within the container can be written back
(using the [NOMAD API](../howto/manage/program/api.md)) as derived data, metadata, or artifacts.
Running a reprocessing of an upload afterwards allows for an indexing of these results obtained
with NORTH, provided that the software tools in NORTH write using data structures and schemas
that NOMAD understands.

The connection between the container and the NOMAD file system removes the need
for copying and downloading large datasets. Container images remove the need for installing
analysis software locally and assure consistent execution independent of the user's operating
system. Instead, the tools are executed remotely within the infrastructure
that a NOMAD deployment provides. These capabilities of NORTH are especially important in
collaborative research settings enabling other users to rerun the same analysis, or apply
existent parameterizations to new data. Provided a server installation and cloud configuration
is used, this also enables to spawn multiple instances of the same tool.
The central deployment of NOMAD is one example that substantiates these capabilities.

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

**TODO clarify which and then give the link to the repo behind JupyterHub service, one of these?**
https://gitlab.mpcdf.mpg.de/nomad-lab/north/jupyterhub or https://github.com/FAIRmat-NFDI/nomad-north


## Using existing tools

NORTH does not implement analysis logic itself. Instead, it executes tools that are packaged
as Docker containers and registered with NOMAD. A number of such tools, maintained by FAIRmat,
are already provided as plugins to the NOMAD ecosystem. These tools are based either on jupyter-
or on desktop-based images. Creating ones own containers and connecting these to the service
is also possible.

<!--## How to connect and use specific NORTH tools in a NOMAD deployment
TODO move this part as part of a how-to
Relevant for a given NOMAD deployment is always the specific configuration YAML file that defines which NORTH tools are included. The starting point and example for such a configuration file is the respective [default.yaml file](https://gitlab.mpcdf.mpg.de/nomad-lab/nomad-FAIR/-/blob/develop/nomad/config/defaults.yaml) within the NOMAD main repository.-->

<!--## Defining official & community tools
TODO what the term official tool means should be documented, does official mean just something that is in any of the projects tracked by the automated plugin collection algorithm, e.g., FAIRmat-NFDI or nomad-coe, or does official mean more, i.e., demands for sophisticated documentation and maintenance strategy by NOMAD/FAIRmat officials-->


## Official base images

Using base image within the [`nomad-north-desktop-base`](https://github.com/FAIRmat-NFDI/nomad-north-desktop-base) repository is the recommended best practice to build a NORTH tool if that demands a graphical user interface. Its desktop-base image builds on the [Jupyter Docker Stacks project](https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html), offering
a [conda](https://anaconda.org) environment with a jupyter notebook and graphical user interface via a light-weight [xfce](https://www.xfce.org/) desktop environment. Ubuntu Linux is the base layer of this docker image, connecting the container to the operation system of the host computer.

<!--REMOVE WHEN REFACTORING COMPLETED
previously called [base-desktop](https://gitlab.mpcdf.mpg.de/nomad-lab/north/base-desktop/-/blob/main/Dockerfile?ref_type=heads) -->

Using the base image within the [cookiecutter-nomad-plugin](https://github.com/FAIRmat-NFDI/cookiecutter-nomad-plugin) repository is the recommended best practice to build a NORTH tool from if it does not demand a graphical user interface. Note that this repository is the template for building
NOMAD plugins.

<!--REMOVE WHEN REFACTORING COMPLETED
<!--[jupyter notebook] is the one as of 2026/01/19 shipped with nomad-FAIR. -->
<!--gitlab-registry.mpcdf.mpg.de/nomad-lab/nomad-distro/jupyter:develop -->
<!--https://gitlab.mpcdf.mpg.de/nomad-lab/nomad-distro/container_registry/1462?orderBy=NAME&sort=asc&search[]=latest -->

## Specific NORTH tools

Consult the reference section of the documentation to find details about individual NOMAD plugins and the eventual NORTH tools these provide.

<!--MOVE THESE HERE INDIVIDUAL DOCUMENTATION TO A NORTH ENTRY POINT SPECIFIC SECTION IN THE PLUGINS
### abtem

MOVE to pynxtools-em abtem
[`abTEM`](https://gitlab.mpcdf.mpg.de/nomad-lab/north/abtem) is a GUI-based NORTH tool offering software for research on electron microscopy. The tool bundles one version of [abTEM](https://abtem.readthedocs.io/en/latest/intro.html) (a software by [J. Madsen et al.](https://open-research-europe.ec.europa.eu/articles/1-24) for simulating dynamic electron diffraction using jupyter notebooks), one version of [VESTA](https://jp-minerals.org/vesta/en/) (a software by [K. Momma and F. Izumi](https://doi.org/10.1107/S0021889811038970) for generating and visualizing crystal structures within a GUI application), and one version of [GPAW](https://gpaw.readthedocs.io/) (a software package by [J. J. Mortensen, E. J. Enkovaara et al.](https://iopscience.iop.org/article/10.1088/0953-8984/22/25/253202) for scripting projector augmented-wave-based electronic structure simulations using Python). **The container is to be renamed to `nomad-north-abtem` and moved to the [pynxtools-em](https://fairmat-nfdi.github.io/pynxtools-em/) plugin.** 

### apmtools

MOVE to pynxtools-apm
[`apmtools`](https://gitlab.mpcdf.mpg.de/nomad-lab/north/apmtools) is a GUI-based NORTH tool offering software for research on atom probe microscopy. The tool bundles one version of [APTyzer](https://github.com/areichm/APTyzer) (a jupyter notebook by [A. Reichmann](https://pure.unileoben.ac.at/de/persons/alexander-reichmann/) for visually-guided composition analysis of atom-probe-reconstructed material volume), one version of [paraprobe](https://gitlab.com/paraprobe/) (a software by [M. Kühbach](https://doi.org/10.48550/arXiv.2205.13510) for Python and jupyter-notebook-based scripting of data analyses for atom probe, and one version of [apav](https://apav.readthedocs.io/en/latest/index.html) (focusing on analyses of multi-hit and mass spectra [J. Smith et al.](https://joss.theoj.org/papers/10.21105/joss.04862) via a Python and jupyter notebooks. **The container is to be renamed to `nomad-north-apmtools` and moved to the [pynxtools-apm](https://fairmat-nfdi.github.io/pynxtools-apm/) plugin.** 
A summary of the specific data analyses offered by each tool of paraprobe is provided [here](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/apm-structure.html#cc-apm-structure).

### fiji

EXTEND with other unix imaging tools (gimp, inkscape) to nomad-north-imageprocessing, GUI tool
[`fiji`](https://gitlab.mpcdf.mpg.de/nomad-lab/north/fiji) is a GUI-based NORTH tool offering, [fiji](https://fiji.sc/) a frequently used extension of the [[imagej](https://imagej.net/ij/download.html) image processing and analysis software. The electron microscopy community is a frequent user of fiji given its covering set of custom image filters. The original motivation of FAIRmat for the fiji container was reaching out to electron microscopists working with focus series reconstruction, for which the container was configured to offer specific imagej/fiji plugins. **The container should be renamed to `nomad-north-fiji` and moved to [pynxtools-em](https://fairmat-nfdi.github.io/pynxtools-em/). It could also though stay with this name alone given its multi-community user base.**

### mpes

MOVE to pynxtools-mpes, stressing here wine part, eventually multiple tools as desired by rettigl and lukaspie
[`mpes`](https://gitlab.mpcdf.mpg.de/nomad-lab/north/mpes) is GUI-based NORTH tool offering software for research on multi photoemission spectroscopy (MPES). Apart from offering tutorials of a detailed data processing pipeline for converting, binning, and analyzing MPES data, the docker image exemplifies how [Igor Pro](https://www.wavemetrics.com/), a Windows based GUI application can be configured to offer its services via the browser within in a Linux environment coupled to NOMAD using the [wine](https://www.winehq.org/). **The container is to be renamed `nomad-north-mpes` and moved to the [pynxtools-mpes](https://fairmat-nfdi.github.io/pynxtools-mpes/) plugin.**
### nexus

### nexus

DEPRECATE, pynxtools
[`nexus`](https://gitlab.mpcdf.mpg.de/nomad-lab/north/nexus) is GUI-based NORTH tool offering software for **converting data using the pynxtools parsers** and validating these against NeXus application definitions using the stand alone HDF5 file parser offered by pynxtools as well as using other software tools that are offered by the [NeXus user community](https://www.nexusformat.org/)
**The container is to be renamed `nomad-north-nexus`, I could be a good idea to move it to the [pynxtools](https://fairmat-nfdi.github.io/pynxtools/) plugin.**


### nionswift

MOVE to pynxtools-em
[`nionswift`](https://gitlab.mpcdf.mpg.de/nomad-lab/north/nionswift) is GUI-based NORTH tool offering the open-source image processing software [nionswift](https://nionswift.readthedocs.io/en/stable/) that is used especially in the research field of electron microscopy by users of [former Nion now Bruker](https://ir.bruker.com/press-releases/press-release-details/2024/Bruker-Acquires-Electron-Microscopy-Company-Nion/default.aspx) transmission electron microscopes. **The container is to be renamed `nomad-north-nionswift` and moved to the [pynxtools-em](https://fairmat-nfdi.github.io/pynxtools-em/) plugin.**

### pyiron

RENAME to nomad-north-pyiron
[`pyiron`](https://pyiron.org/) is a ? jupyter-based NORTH tool offering the pyiron software for implementing computational materials science as well as materials engineering simulation and data analysis [workflows](https://pythonworkflow.github.io/python-workflow-definition/README.html). The developed is driven and coordinated by the Department of Computational Materials Design at the [Max Planck Institute for Sustainable Materials Research](https://www.mpie.de/CM). **The container should be renamed `nomad-north-pyiron`**.

### ellips

DEPRECATED, functionality offered by generic pynxtools parsing container
[`ellips`](https://gitlab.mpcdf.mpg.de/nomad-lab/north/ellips) is a jupyter-based NORTH tool offering software for research on ellipsometry. The tool implemented an example for converting data from an ellipsometry measurement on a Woollam instrument to NeXus/HDF5. In the past, the container exemplified also a subsequent data analysis of such measurements using the open-source optical spectroscopy data analysis software [PyElli](https://pyelli.readthedocs.io/en/stable/). The example focused on building a database of dispersive materials using the contributed NeXus application definition [NXdispersive_material](https://github.com/nexusformat/definitions/blob/main/contributed_definitions/NXdispersive_material.nxdl.xml) and related base classes. The proposal of these were [heavily discussed](https://github.com/nexusformat/definitions/pull/1424) at the [NIAC2024](https://www.nexusformat.org/NIAC2024_minutes.html) with questions raised if and how the NeXus standard should allow to include explicit formulas that could raise security concerns. No consensus was reached for NXdispersive-related classes, and the work put on hold. **Like for all method-specific pynxtools plugins, the conversion of data from domain-specific measurements to specific NeXus/HDF5 files can be achieved using every jupyter or Python capable NORTH tool provided it offers pynxtools and the respective domain-specific plugin is installed. Therefore, the ellips container is considered obsolete., if renamed `nomad-north-ellipsometry`**

### spm and sts
sts is a DEPRECATED CONTAINER, REPLACED by spm, which in turn gets moved to pynxtools-spm
[`spm`](https://gitlab.mpcdf.mpg.de/nomad-lab/north/spm) and [`sts`](https://gitlab.mpcdf.mpg.de/nomad-lab/north/sts) and are two jupyter-based NORTH tools offering examples for scanning probe microscopy and scanning tunneling probe spectroscopy. **The containers  are to be renamed `nomad-north-spm` and `nomad-north-sts` respectively, currently both are functionally similar, ideal would be to add a functionality that goes beyond mere conversion, to warrant relevance, and difference, for sure the containers should be moved to the [pynxtools-spm](https://fairmat-nfdi.github.io/pynxtools-spm/) plugin.**

### voila

WILL BE STRIPPED OF HZB content and made an own image, why not in the cookiecutter template?
[`voila`](https://gitlab.mpcdf.mpg.de/nomad-lab/north/voila) is a jupyter-based NORTH tool simplying the usage of jupyter notebooks via [voila](https://github.com/voila-dashboards/voila). The tool is currently developed by the Helmholtz Zentrum Berlin (HZB) and can thus be considered a user-provided NORTH tool. **voila as a tool can be helpful, but that container needs refactoring, firstly, renaming, at all an official one, if so why does the image have HZB-specific customizations, who will maintain this.**

### xps

EITHER REPLACED by generic jupyter-based image provided by pynxtools-plugin-template or becoming an own container pynxtools-xps.
[`xps`](https://gitlab.mpcdf.mpg.de/nomad-lab/north/xps) is a jupyter-based NORTH tool offering software for research on core-level photoemission spectroscopy. The tool implemented an example for converting data from an XPS measurement to NeXus/HDF5 and perform data analyses. **Like mentioned for ellips, the container performs only the conversion, all content should be moved to the pynxtools-xps plugin, the container functionality should be extended or the container deprecated and instead generic conversion achieved with another container e.g. jupyter container. if renamed `nomad-north-xps`**
-->

Learn more about running existing NOMAD tools in the how-tos:
[How-Tos> ... > How to analyze data in NORTH](../howto/manage/gui/north.md).

## Custom user-provided tools

<!--NOMAD OASIS or NOMAD deployments-->
In addition to centrally provided tools, users can package their own tools as Docker containers
and run these via NORTH on NOMAD data. This is especially relevant for organizations and users
who run their own [NOMAD](./oasis.md) deployment. In this context, institution- or project-specific
analysis software may call for connecting proprietary or tools whose license does not allow exposing
services outside the local infrastructure. Given that the requirements of NORTH can be decoupled
from those of the NOMAD core system is a clear user benefit.

Developing a custom NORTH tool typically involves defining the tool logic and dependencies,
packaging the tool as a Docker container, and registering the container so that it can be
invoked via NOMAD. Once registered, custom tools follow the same execution and provenance model
as built-in tools.

Guidance on developing and registering custom NORTH tools is available in the how-tos:
[How to develop NORTH tools](../howto/plugins/types/north_tools.md).


## Data schema interoperability

Beyond its importance for managing the expectations as to how NOMAD reacts to and what
individual NORTH tools offer, it is important to know that using different data schemas
in a NORTH tool compared to the NOMAD deployment does not always come without challenges.

Users may face issues when reprocessing uploads when results have been stored in these
uploads from a NORTH tool analysis whose application wrote a different version of the
data schema than used for the NOMAD deployment. Eventual incompatibilities in parts or
entirely are possible. Having now individual NORTH tools as optional functionality
additions of a NOMAD plugin offload the responsibility to reduce the incompatibilities
between different schema versions to the plugin developers.

## NORTH refactoring history

**Deprecation note, remove when refactoring complete**

[Since its addition to NOMAD as a service](https://joss.theoj.org/papers/10.21105/joss.05388), the backend and docker images behind NORTH tools have been in a process of significant refactoring: Docker base images evolved, most services of NOMAD were refactored into plugins, NORTH tools that were initially based on [Webtop](https://docs.linuxserver.io/images/docker-webtop/) got based on [nomad-north-desktop-base](https://github.com/FAIRmat-NFDI/nomad-north-desktop-base). These developments took place in different repositories. This is a technical note that developers who work with NORTH tools should be aware of to avoid working with outdated container images. In summary, tool source code from the [initially used](https://gitlab.mpcdf.mpg.de/nomad-lab/nomad-remote-tools-hub) and the [subsequently used](https://gitlab.mpcdf.mpg.de/nomad-lab/north) repository locations will soon become deprecated.
Instead, users should consult the reference for the NOMAD plugins which details which plugins offer NORTH tool entry points.

