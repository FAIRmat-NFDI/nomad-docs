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
or data from NOMAD uploads. Results achieved within the container can be written back
(using the [NOMAD API](../howto/manage/program/api.md)) as derived data, metadata, or artifacts.
Running a reprocessing of an upload afterwards allows for an indexing of these results obtained
with NORTH, provided that the software tools in NORTH write using data structures and schemas
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

<!--EXPOSE THE REPO BEHIND THE JUPYTER SERVICE IN THE DOCS ? https://github.com/FAIRmat-NFDI/nomad-north -->

## Using existing tools

NORTH does not implement analysis logic itself. Instead, it executes tools that are packaged
as Docker containers and registered with NOMAD. Several such tools, maintained by FAIRmat,
are already available as NOMAD plugins. These tools are based on either Jupyter- or desktop-based images.
Custom containers can also be created and connected to the service.

<!--## How to connect and use specific NORTH tools in a NOMAD deployment
TODO: move this part as part of a how-to
Relevant for a given NOMAD deployment is always the specific configuration YAML file that defines which NORTH tools are included. The starting point and example for such a configuration file is the respective [default.yaml file](https://gitlab.mpcdf.mpg.de/nomad-lab/nomad-FAIR/-/blob/develop/nomad/config/defaults.yaml){:target="_blank" rel="noopener"} within the NOMAD main repository.-->

<!--## Defining official & community tools
TODO: what the term official tool means should be documented, does official mean just something that is in any of the projects tracked by the automated plugin collection algorithm, e.g., FAIRmat-NFDI or nomad-coe, or does official mean more, i.e., demands for sophisticated documentation and maintenance strategy by NOMAD/FAIRmat officials-->

## Official base images

Using the base image within the [`nomad-north-desktop-base`](https://github.com/FAIRmat-NFDI/nomad-north-desktop-base){:target="_blank" rel="noopener"} repository is the recommended best practice to build a NORTH tool if that demands a graphical user interface. Its desktop-base image builds on the [Jupyter Docker Stacks project](https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html){:target="_blank" rel="noopener"}, offering
a [conda](https://anaconda.org){:target="_blank" rel="noopener"} environment with a Jupyter Notebook and graphical user interface via a light-weight [xfce](https://www.xfce.org/){:target="_blank" rel="noopener"} desktop environment. Ubuntu Linux is the base layer of this docker image, connecting the container to the operation system of the host computer.

<!--REMOVE WHEN REFACTORING COMPLETED
previously called [base-desktop](https://gitlab.mpcdf.mpg.de/nomad-lab/north/base-desktop/-/blob/main/Dockerfile?ref_type=heads){:target="_blank" rel="noopener"} -->

Using the base image within the [nomad-plugin-template](https://github.com/FAIRmat-NFDI/nomad-plugin-template){:target="_blank" rel="noopener"} repository is the recommended best practice to build a NORTH tool from if it does not demand a graphical user interface. Note that this repository is the template for building
NOMAD plugins.

A how-to for building from these images is available [How-tos > ... > How to create a NORTH tool](../howto/plugins/types/north_tools.md).

<!--TODO: REMOVE WHEN REFACTORING COMPLETED
<!--[Jupyter Notebook] is the one as of 2026/01/19 shipped with nomad-FAIR. -->
<!--gitlab-registry.mpcdf.mpg.de/nomad-lab/nomad-distro/jupyter:develop -->
<!--https://gitlab.mpcdf.mpg.de/nomad-lab/nomad-distro/container_registry/1462?orderBy=NAME&sort=asc&search[]=latest -->

## Specific NORTH tools

Consult the reference section of the documentation to find details about individual NOMAD plugins and the eventual NORTH tools these provide.

<!-- markdownlint-disable MD044 -->
<!--TODO: MOVE THESE HERE INDIVIDUAL DOCUMENTATION TO A NORTH ENTRY POINT SPECIFIC SECTION IN THE PLUGINS
### abtem

TODO: MOVE to pynxtools-em abtem
[`abTEM`](https://gitlab.mpcdf.mpg.de/nomad-lab/north/abtem){:target="_blank" rel="noopener"} is a GUI-based NORTH tool offering software for research on electron microscopy. The tool bundles one version of [abTEM](https://abtem.readthedocs.io/en/latest/intro.html){:target="_blank" rel="noopener"} (a software by [J. Madsen et al.](https://open-research-europe.ec.europa.eu/articles/1-24){:target="_blank" rel="noopener"} for simulating dynamic electron diffraction using Jupyter Notebooks), one version of [VESTA](https://jp-minerals.org/vesta/en/){:target="_blank" rel="noopener"} (a software by [K. Momma and F. Izumi](https://doi.org/10.1107/S0021889811038970){:target="_blank" rel="noopener"} for generating and visualizing crystal structures within a GUI application), and one version of [GPAW](https://gpaw.readthedocs.io/){:target="_blank" rel="noopener"} (a software package by [J. J. Mortensen, E. J. Enkovaara et al.](https://iopscience.iop.org/article/10.1088/0953-8984/22/25/253202){:target="_blank" rel="noopener"} for scripting projector augmented-wave-based electronic structure simulations using Python). **The container is to be renamed to `nomad-north-abtem` and moved to the [pynxtools-em](https://fairmat-nfdi.github.io/pynxtools-em/){:target="_blank" rel="noopener"} plugin.** 

### apmtools

TODO: MOVE to pynxtools-apm
[`apmtools`](https://gitlab.mpcdf.mpg.de/nomad-lab/north/apmtools){:target="_blank" rel="noopener"} is a GUI-based NORTH tool offering software for research on atom probe microscopy. The tool bundles one version of [APTyzer](https://github.com/areichm/APTyzer){:target="_blank" rel="noopener"} (a Jupyter Notebook by [A. Reichmann](https://pure.unileoben.ac.at/de/persons/alexander-reichmann/){:target="_blank" rel="noopener"} for visually-guided composition analysis of atom-probe-reconstructed material volume), one version of [paraprobe](https://gitlab.com/paraprobe/){:target="_blank" rel="noopener"} (a software by [M. Kühbach](https://doi.org/10.48550/arXiv.2205.13510){:target="_blank" rel="noopener"} for Python and Jupyter-Notebook-based scripting of data analyses for atom probe, and one version of [apav](https://apav.readthedocs.io/en/latest/index.html){:target="_blank" rel="noopener"} (focusing on analyses of multi-hit and mass spectra [J. Smith et al.](https://joss.theoj.org/papers/10.21105/joss.04862){:target="_blank" rel="noopener"} via a Python and Jupyter Notebooks. **The container is to be renamed to `nomad-north-apmtools` and moved to the [pynxtools-apm](https://fairmat-nfdi.github.io/pynxtools-apm/){:target="_blank" rel="noopener"} plugin.** 
A summary of the specific data analyses offered by each tool of paraprobe is provided [here](https://fairmat-nfdi.github.io/nexus_definitions/classes/contributed_definitions/apm-structure.html#cc-apm-structure){:target="_blank" rel="noopener"}.

### fiji

TODO: EXTEND with other unix imaging tools (gimp, inkscape) to nomad-north-imageprocessing, GUI tool
[`fiji`](https://gitlab.mpcdf.mpg.de/nomad-lab/north/fiji){:target="_blank" rel="noopener"} is a GUI-based NORTH tool offering, [fiji](https://fiji.sc/){:target="_blank" rel="noopener"} a frequently used extension of the [[imagej](https://imagej.net/ij/download.html){:target="_blank" rel="noopener"} image processing and analysis software. The electron microscopy community is a frequent user of fiji given its covering set of custom image filters. The original motivation of FAIRmat for the fiji container was reaching out to electron microscopists working with focus series reconstruction, for which the container was configured to offer specific imagej/fiji plugins. **The container should be renamed to `nomad-north-fiji` and moved to [pynxtools-em](https://fairmat-nfdi.github.io/pynxtools-em/){:target="_blank" rel="noopener"}. It could also though stay with this name alone given its multi-community user base.**

### mpes

TODO: MOVE to pynxtools-mpes, stressing here wine part, eventually multiple tools as desired by rettigl and lukaspie
[`mpes`](https://gitlab.mpcdf.mpg.de/nomad-lab/north/mpes){:target="_blank" rel="noopener"} is GUI-based NORTH tool offering software for research on multi photoemission spectroscopy (MPES). Apart from offering tutorials of a detailed data processing pipeline for converting, binning, and analyzing MPES data, the docker image exemplifies how [Igor Pro](https://www.wavemetrics.com/){:target="_blank" rel="noopener"}, a Windows based GUI application can be configured to offer its services via the browser within in a Linux environment coupled to NOMAD using the [wine](https://www.winehq.org/){:target="_blank" rel="noopener"}. **The container is to be renamed `nomad-north-mpes` and moved to the [pynxtools-mpes](https://fairmat-nfdi.github.io/pynxtools-mpes/){:target="_blank" rel="noopener"} plugin.**
### nexus

### nexus

TODO: DEPRECATE, pynxtools
[`nexus`](https://gitlab.mpcdf.mpg.de/nomad-lab/north/nexus){:target="_blank" rel="noopener"} is GUI-based NORTH tool offering software for **converting data using the pynxtools parsers** and validating these against NeXus application definitions using the stand alone HDF5 file parser offered by pynxtools as well as using other software tools that are offered by the [NeXus user community](https://www.nexusformat.org/){:target="_blank" rel="noopener"}
**The container is to be renamed `nomad-north-nexus`, I could be a good idea to move it to the [pynxtools](https://fairmat-nfdi.github.io/pynxtools/){:target="_blank" rel="noopener"} plugin.**

### nionswift

TODO: MOVE to pynxtools-em
[`nionswift`](https://gitlab.mpcdf.mpg.de/nomad-lab/north/nionswift){:target="_blank" rel="noopener"} is GUI-based NORTH tool offering the open-source image processing software [nionswift](https://nionswift.readthedocs.io/en/stable/){:target="_blank" rel="noopener"} that is used especially in the research field of electron microscopy by users of [former Nion now Bruker](https://ir.bruker.com/press-releases/press-release-details/2024/Bruker-Acquires-Electron-Microscopy-Company-Nion/default.aspx){:target="_blank" rel="noopener"} transmission electron microscopes. **The container is to be renamed `nomad-north-nionswift` and moved to the [pynxtools-em](https://fairmat-nfdi.github.io/pynxtools-em/){:target="_blank" rel="noopener"} plugin.**

### pyiron

TODO: RENAME to nomad-north-pyiron
[`pyiron`](https://pyiron.org/){:target="_blank" rel="noopener"} is a ? Jupyter-based NORTH tool offering the pyiron software for implementing computational materials science as well as materials engineering simulation and data analysis [workflows](https://pythonworkflow.github.io/python-workflow-definition/README.html){:target="_blank" rel="noopener"}. The developed is driven and coordinated by the Department of Computational Materials Design at the [Max Planck Institute for Sustainable Materials Research](https://www.mpie.de/CM){:target="_blank" rel="noopener"}. **The container should be renamed `nomad-north-pyiron`**.

### ellips

TODO: DEPRECATED, functionality offered by generic pynxtools parsing container
[`ellips`](https://gitlab.mpcdf.mpg.de/nomad-lab/north/ellips){:target="_blank" rel="noopener"} is a Jupyter-based NORTH tool offering software for research on ellipsometry. The tool implemented an example for converting data from an ellipsometry measurement on a Woollam instrument to NeXus/HDF5. In the past, the container exemplified also a subsequent data analysis of such measurements using the open-source optical spectroscopy data analysis software [PyElli](https://pyelli.readthedocs.io/en/stable/){:target="_blank" rel="noopener"}. The example focused on building a database of dispersive materials using the contributed NeXus application definition [NXdispersive_material](https://github.com/nexusformat/definitions/blob/main/contributed_definitions/NXdispersive_material.nxdl.xml){:target="_blank" rel="noopener"} and related base classes. The proposal of these were [heavily discussed](https://github.com/nexusformat/definitions/pull/1424){:target="_blank" rel="noopener"} at the [NIAC2024](https://www.nexusformat.org/NIAC2024_minutes.html){:target="_blank" rel="noopener"} with questions raised if and how the NeXus standard should allow to include explicit formulas that could raise security concerns. No consensus was reached for NXdispersive-related classes, and the work put on hold. **Like for all method-specific pynxtools plugins, the conversion of data from domain-specific measurements to specific NeXus/HDF5 files can be achieved using every Jupyter or Python capable NORTH tool provided it offers pynxtools and the respective domain-specific plugin is installed. Therefore, the ellips container is considered obsolete., if renamed `nomad-north-ellipsometry`**

### spm and sts
TODO: REMOVE
sts is a DEPRECATED CONTAINER, REPLACED by spm, which in turn gets moved to pynxtools-spm
[`spm`](https://gitlab.mpcdf.mpg.de/nomad-lab/north/spm){:target="_blank" rel="noopener"} and [`sts`](https://gitlab.mpcdf.mpg.de/nomad-lab/north/sts){:target="_blank" rel="noopener"} and are two Jupyter-based NORTH tools offering examples for scanning probe microscopy and scanning tunneling probe spectroscopy. **The containers  are to be renamed `nomad-north-spm` and `nomad-north-sts` respectively, currently both are functionally similar, ideal would be to add a functionality that goes beyond mere conversion, to warrant relevance, and difference, for sure the containers should be moved to the [pynxtools-spm](https://fairmat-nfdi.github.io/pynxtools-spm/){:target="_blank" rel="noopener"} plugin.**

### voila

TODO: WILL BE STRIPPED OF HZB content and made an own image, why not in the cookiecutter template?
[`voila`](https://gitlab.mpcdf.mpg.de/nomad-lab/north/voila){:target="_blank" rel="noopener"} is a Jupyter-based NORTH tool simplying the usage of Jupyter Notebooks via [voila](https://github.com/voila-dashboards/voila){:target="_blank" rel="noopener"}. The tool is currently developed by the Helmholtz Zentrum Berlin (HZB) and can thus be considered a user-provided NORTH tool. **voila as a tool can be helpful, but that container needs refactoring, firstly, renaming, at all an official one, if so why does the image have HZB-specific customizations, who will maintain this.**

### xps

TODO: EITHER REPLACED by generic Jupyter-based image provided by pynxtools-plugin-template or becoming an own container pynxtools-xps.
[`xps`](https://gitlab.mpcdf.mpg.de/nomad-lab/north/xps){:target="_blank" rel="noopener"} is a Jupyter-based NORTH tool offering software for research on core-level photoemission spectroscopy. The tool implemented an example for converting data from an XPS measurement to NeXus/HDF5 and perform data analyses. **Like mentioned for ellips, the container performs only the conversion, all content should be moved to the pynxtools-xps plugin, the container functionality should be extended or the container deprecated and instead generic conversion achieved with another container e.g. Jupyter container. if renamed `nomad-north-xps`**
-->

Learn more about running existing NOMAD tools in the how-tos: [How-tos > ... > How to analyze data in NORTH](../howto/manage/gui/north.md).

## Custom user-provided tools

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

Users may encounter issues when reprocessing uploads that contain results from a NORTH tool
analysis, if the tool wrote data using a schema version different from the one used in the
NOMAD deployment. This can lead to partial or complete incompatibilities. By providing
individual NORTH tools as optional extensions of a NOMAD plugin, the responsibility
for minimizing schema incompatibilities is shifted to the plugin developers.

<!-- TODO: This is a deprecation warning, we should remove it when refactoring complete-->

??? warning "NORTH refactoring history"

    [Since its addition to NOMAD as a service](https://joss.theoj.org/papers/10.21105/joss.05388){:target="_blank" rel="noopener"}, the backend and docker images
    behind NORTH tools have been in a process of significant refactoring. Docker base images evolved,
    most services of NOMAD were refactored into plugins, NORTH tools that were initially based on
    [Webtop](https://docs.linuxserver.io/images/docker-webtop/){:target="_blank" rel="noopener"} got based on [nomad-north-desktop-base](https://github.com/FAIRmat-NFDI/nomad-north-desktop-base){:target="_blank" rel="noopener"}.

    These developments took place in different repositories. This is a technical note that developers
    who work with NORTH tools should be aware of to avoid working with outdated container images.
    In summary, tool source code from the [initially used](https://gitlab.mpcdf.mpg.de/nomad-lab/nomad-remote-tools-hub){:target="_blank" rel="noopener"}
    and the [subsequently used](https://gitlab.mpcdf.mpg.de/nomad-lab/north){:target="_blank" rel="noopener"} repository locations
    will soon become deprecated.

<!-- ADD WHEN PR186 MERGED Instead, users should consult the [NOMAD plugin registry](../examples/plugin_registry.md) which details which plugins offer NORTH tool entry points.-->
