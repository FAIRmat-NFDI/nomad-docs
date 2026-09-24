# How to analyze data in NORTH

!!! warning "Attention"

    This part of the documentation is still work in progress.

## What you will learn

- Launch interactive and non-interactive NORTH tools from the NOMAD user interface
- Run analyses directly on data stored in NOMAD without downloading it locally
- Work with NOMAD data inside a Jupyter-based NORTH environment
- Write analysis results back to NOMAD using the NOMAD API
<!-- - TODO: Understand when to use NORTH tools instead of local analysis workflows -->

## When to use NORTH for data analysis

NORTH is intended for analyses that:

- Require dedicated or complex software environments
- Should run close to the data stored in NOMAD
- Need to be reproducible and shareable with other users
- Are impractical to execute locally due to data size or dependencies

Typical examples include domain-specific analysis tools, post-processing workflows, and
interactive exploration using Jupyter notebooks.

## Launching NORTH tools from NOMAD

All NORTH tools are executed in isolated Docker containers and can be invoked from any
NOMAD dataset, independent of how the data was originally uploaded or processed.

From the graphical user interface, NORTH tools can be launched directly from:

- Upload views

- Entry views

- Dataset or search result contexts

<!-- INSERT SCREENSHOT: NOMAD UI showing available NORTH tools -->

Selecting a tool triggers the creation of a new execution environment for that tool. Depending on the tool type, this may start
an interactive Jupyter session or a remote desktop application.

The tool receives references to the selected NOMAD data as input and runs independently of the user’s local system.

## Working with data in a Jupyter-based NORTH tool

For Jupyter-based tools, launching the tool opens a notebook environment running inside a NORTH-managed container.

Within this environment, you can:

- Access NOMAD data associated with the selected dataset

- Load archives, files, or metadata programmatically

- Use standard Python libraries together with NOMAD-specific APIs

<!-- INSERT EXAMPLE: minimal notebook snippet showing data access -->

The Jupyter environment is isolated and reproducible: all dependencies are defined by the tool’s container image,
ensuring consistent behavior across users and sessions.

## Writing results back to NOMAD

Analysis results produced in NORTH can be written back to NOMAD. THis may include
derived data, additional metadata, or files and artifacts that were created during
the analysis.

As each tool runs in its own separate environment, one cannot directly access NOMAD
through the GUI. Instead, we use the NOMAD API from within the tool environment.

<!-- INSERT EXAMPLE: API call writing derived data -->

When results are written back, the analysis execution itself can be represented as a NOMAD entry, recording:

Input data references

Tool parameters and versions

Produced outputs

This establishes explicit provenance links between original data and derived results.

## Further resources

- How to create and configure NORTH tools: [How-Tos> ... > Entry point types > NORTH tools](../../../howto/plugins/types/north_tools.md)
