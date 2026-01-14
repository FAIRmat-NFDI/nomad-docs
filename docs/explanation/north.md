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
[How to develop NORTH tools](../../../howto/plugins/types/north_tools.md).
