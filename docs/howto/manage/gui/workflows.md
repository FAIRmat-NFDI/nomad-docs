# How to create custom workflows

This guide shows you how to create a custom workflow Entry that connects
existing NOMAD Entries and archive sections as inputs, tasks, and outputs. It
covers Entries created from supported files or schemas, references within and
across Projects, and nested workflows. The resulting Entry contains an
interactive workflow graph for inspecting the connections and navigating to
the referenced data.

To begin, you need a Project to which you can add files. The Entries and data that the
workflow connects can already exist, or you can add their files together with
the workflow file, as in the downloadable examples in this guide.

## Recommended preparation

- [How-to guides > ... > Upload and publish data](upload.md)
- [Explanation > From files to data](../../../explanation/basics.md)
- [Explanation > Data structure](../../../explanation/data.md)

## Further resources

- [Explanation > Workflows](../../../explanation/workflows.md)
- [Tutorials > Managing workflows and projects](../../../tutorial/workflows_projects.md)

## Overview

NOMAD workflows connect archive sections through inputs, tasks, and outputs.
For supported data, NOMAD may create a workflow automatically during
[Processing](../../../explanation/processing.md). A custom workflow Entry lets
you define these connections when the workflow is not created automatically.

The examples in this guide use supported simulation files to provide reproducible task
Entries. Their scientific methods are not relevant to the workflow patterns
demonstrated here.

## Simple workflows with supported tasks

Start with a workflow containing one task, one input, and one output:

```mermaid
graph LR;
    A((Input structure)) --> B[DFT];
    B[DFT] --> C([Output calculation]);
```

The task is represented by `dft.xml`, the mainfile of a VASP calculation. In
this example, the VASP parser provided by the
[electronic-parsers plugin](https://github.com/nomad-coe/electronic-parsers){:target="_blank" rel="noopener"}
creates an Entry with a `workflow2` section representing the single-point
calculation. This behavior is specific to the parser and is not a general
feature of all parser-supported mainfiles.

The parser-generated workflow has the following graph:

![Parser-generated single-point workflow graph in the light theme](images/single-point-nomad-workflow-card-light.png#only-light){:.screenshot}
![Parser-generated single-point workflow graph in the dark theme](images/single-point-nomad-workflow-card-dark.png#only-dark){:.screenshot}

To demonstrate the creation of a custom workflow entry, the example below recreates the central input-task-output path of this
`SinglePoint` workflow graph in a separate custom workflow Entry defined with a
YAML file. The custom workflow references the parser-generated `workflow2` section
as its task and explicitly uses the same system and final calculation sections
as its input and output.

<!-- TODO(#363): After PR #363 is merged, link "YAML file" to the relevant new schema how-to. -->
<!-- TODO: Explain why the parser-generated workflow graph has three outputs while the custom workflow graph has one. -->

To define the initial workflow, create a file `dft.workflow.archive.yaml` with the following content:

```yaml
workflow2:
  name: DFT SinglePoint
  inputs:
    - name: Input system
      section: '../upload/archive/mainfile/dft.xml#/run/0/system/-1'
  outputs:
    - name: Output calculation
      section: '../upload/archive/mainfile/dft.xml#/run/0/calculation/-1'
  tasks:
    - m_def: nomad.datamodel.metainfo.workflow.TaskReference
      task: '../upload/archive/mainfile/dft.xml#/workflow2'
      name: DFT
      inputs:
        - name: Input structure
          section: '../upload/archive/mainfile/dft.xml#/run/0/system/-1'
      outputs:
        - name: Output calculation
          section: '../upload/archive/mainfile/dft.xml#/run/0/calculation/-1'
```

!!! Warning "Important"
    For the creation of workflow entries using YAMLs, the file must have the extension `archive.yaml`.

This file is constructed according to NOMAD's schemas for [Archive Files](../../../explanation/data.md#archives) and [General Workflows](../../../explanation/workflows.md#the-built-in-abstract-workflow-schema). The `workflow2` section of the archive has 3 possible subsections: `inputs`, `outputs`, and `tasks`:

**`inputs`**: a list of references to the global inputs of the workflow, with `name` and `section` attributes. `section` corresponds to a path for linking to the relevant archive section. In this case, the relative section path is `run[0].system[-1]`, linked to the Entry defined by the mainfile `dft.xml`. The prefix is discussed under [Considerations for archive path specification](#path-specification).

**`outputs`**: identical to the inputs list, representing the global outputs of the workflow, with the relative section path `run[0].calculation[-1]` in this case.

**`tasks`**: a list of references to the tasks/steps of the workflow. Each task contains `m_def`, `task`, `inputs`, and `outputs` attributes. `inputs`/`outputs` are task-specific versions of the lists defined above.

`task` is the path for linking to the relevant archive section, analogous to the `section` attribute for `inputs`/`outputs`. However, this path **must** reference a task, which in all practical cases corresponds to a `workflow2` section

`m_def` defines the type of task according to NOMAD's MetaInfo schema, in this case a `TaskReference` to the archive `workflow2` section.  The use of `TaskReference` will be clarified in the [Nested workflows > In multiple entries](#in-multiple-entries) example below.

<a id="path-specification"></a>
### Archive path specification

In general, an archive reference can be represented as
`<prefix>/<entry_locator>#/<relative_archive_path>`:

- `<relative_archive_path>` identifies the section within the target Entry. Open the Entry's **ARCHIVE** page and navigate to the section you want to reference.
- **Entry in the same Project:**
    - `<prefix>` is `../upload/archive/mainfile`
    - `<entry_locator>` is the path to the Entry's mainfile from the Project root
- **Entry in another Project:**
    - `<prefix>` is `../uploads/<upload_id>/archive`
    - `<entry_locator>` is `<entry_id>`

In archive-reference paths, `upload` and `uploads` are backend terms for Projects, and `upload_id` is equivalent to the Project ID.

<!-- TODO(#363): After PR #363 is merged, link this syntax summary to the relevant schema-reference documentation. -->

### Download and reproduce the example

[Download simple_workflow.zip](data/simple_workflow.zip){:.md-button .nomad-button}

The compressed file contains:

```tree
.
├── dft.xml
├── dft.workflow.archive.yaml
```

To reproduce the example in a new Project:

1. Open **PROJECTS** and select **NEW PROJECT**.
1. Enter a Project name, select **ADD FILES**, and add
   `simple_workflow.zip`.
1. Select **CREATE**.
1. After processing completes, open **ENTRIES** and confirm that NOMAD created two successfully processed Entries:
     - a single-point Entry with the mainfile `dft.xml`; and
     - a custom workflow Entry with the mainfile
     `dft.workflow.archive.yaml`.

1. Open the custom workflow Entry. Its **Overview** page contains this graph:

![Custom single-point workflow graph in the light theme](images/single-point-custom-nomad-workflow-card-light.png#only-light){:.screenshot}
![Custom single-point workflow graph in the dark theme](images/single-point-custom-nomad-workflow-card-dark.png#only-dark){:.screenshot}

??? tip "Add the methodology as a workflow input"

    You can also represent the calculation's methodological parameters as an
    input. They are stored at `run[0].method[-1]` in the `dft.xml` Entry. Add
    the following item to both `workflow2.inputs` and
    `workflow2.tasks[0].inputs` in `dft.workflow.archive.yaml`:

    ```yaml
    - name: Input methodology parameters
      section: '../upload/archive/mainfile/dft.xml#/run/0/method/-1'
    ```

    Reprocessing the updated file adds another input node to the custom
    workflow graph.

## Reference an Entry in another Project

A workflow Entry can reference tasks or data in another Project on the same
NOMAD deployment. For these references, use
`../uploads/<upload_id>/archive/<entry_id>#/<relative_archive_path>` as
described under [Archive path specification](#path-specification).

To find the required identifiers:

1. Open the target Project, select **SETTINGS**, and copy its **Project ID**.
   This value equals `archive.metadata.upload_id`; use it as `<upload_id>`.
1. Open the target Entry, select **ARCHIVE**, and navigate to
   `metadata` > `entry_id`. Copy this value and use it as `<entry_id>`.
   Alternatively, copy the value immediately after `/entries/` in the Entry's
   URL.

For example, adapt the `dft.workflow.archive.yaml` file from the previous
section as follows:

??? example "Reference the `dft.xml` Entry from another Project"
    ```yaml
    workflow2:
      name: DFT SinglePoint
      inputs:
        - name: Input system
          section: '../uploads/<upload_id>/archive/<entry_id>#/run/0/system/-1'
      outputs:
        - name: Output calculation
          section: '../uploads/<upload_id>/archive/<entry_id>#/run/0/calculation/-1'
      tasks:
        - m_def: nomad.datamodel.metainfo.workflow.TaskReference
          task: '../uploads/<upload_id>/archive/<entry_id>#/workflow2'
          name: DFT
          inputs:
            - name: Input structure
              section: '../uploads/<upload_id>/archive/<entry_id>#/run/0/system/-1'
          outputs:
            - name: Output calculation
              section: '../uploads/<upload_id>/archive/<entry_id>#/run/0/calculation/-1'
    ```

To test the cross-Project references:

1. Create a file named `dft-cross-project.workflow.archive.yaml` using the
   contents shown above. Replace `<upload_id>` and `<entry_id>` with the
   identifiers for the Project and Entry containing `dft.xml`.
1. Create another Project and add only the new
   `dft-cross-project.workflow.archive.yaml` file.
1. After processing completes, open the resulting workflow Entry and confirm
   that its graph contains the referenced DFT task from the original Project.

## Nested workflows

Nested, or hierarchical, workflows correspond to workflow graphs containing task nodes that themselves can be represented as a directed graph, i.e., a sub-workflow. The [General Workflow Schema](../../../explanation/workflows.md#the-built-in-abstract-workflow-schema) allows for nested workflows through an inheritance relationship from the `Task` class to the `Workflow` class.

### In multiple entries

The most common way to construct a nested workflow is by creating separate entries for each (sub-)workflow. In this case, each sub-workflow archive will contain a populated `workflow2` section. Thus, to add a sub-workflow to your workflow YAML, the **best practice** is to directly link to this `workflow2` section, i.e., `task: <prefix>/<entry identifier>/workflow2`.

!!! Warning "Important"
    When `task` is linked to a `workflow2` section of a different upload, this sub-workflow task **must** be defined as a `TaskReference` by setting `m_def: nomad.datamodel.metainfo.workflow.TaskReference`. This is necessary to overwrite the default class for `workflow2.task`, `nomad.datamodel.metainfo.workflow.Task`, which is only allowed to contain a `Task` instance directly, but not allowed to reference one (see [General Workflow Schema](../../../explanation/workflows.md#the-built-in-abstract-workflow-schema)).

We have already seen this case in [Simple Workflows with Support Tasks](#simple-workflows-with-supported-tasks). Actually, there is a convention in NOMAD that all simulation entries contain a workflow representation, even for single-step workflows. Thus, any workflow containing simulation tasks will be a nested workflow.

### In a single entry

Since a `Workflow` instance is also a `Task` instance due to inheritance, we can directly nest workflows within a single entry. Here we illustrate the concept using a concrete computational workflow, represented schematically as:

```mermaid
graph LR;
    A2((Inputs)) --> B2[DFT];
    B2 --> C2[TB];
    C2 --> D21[DMFT at T1];
    C2 --> D22[DMFT at T2];

    subgraph DMFT
        D21;
        D22;
    end

    D21 --> E21([Output calculation T1])
    D22 --> E22([Output calculation T2])
```

This workflow contains a series of electronic structure calculations: a DFT and a TB calculation performed in serial, followed by two DMFT calculations performed in parallel at two different temperatures. The DMFT workflow task is considered as a sub-workflow.

The mainfiles for these calculations are organized in the following file structure, stored with `nested_workflow_one-entry.zip`:

```tree
.
├── DFT
│   └── dft.xml
├── TB
│   ├── tb.wout
│   └── ...extra auxiliary files
├── DMFT
    ├── T1
    │    └── dmft_t1.hdf5
    └── T2
        └── dmft_t2.hdf5
```

We construct the YAML, `nested_workflow_one-entry.archive.yaml` in parts for clarity:

The overall `workflow2` section and global workflow `inputs`:

```yaml
workflow2:
  name: DFT+TB+DMFT
  inputs:
    - name: Input structure
      section: '../upload/archive/mainfile/DFT/dft.xml#/run/0/system/-1'
```

The global workflow outputs `outputs`:

```yaml
  outputs:
    - name: Output DMFT at T1 calculation
      section: '../upload/archive/mainfile/DMFT/T1/dmft_t1.hdf5#/run/0/calculation/-1'
    - name: Output DMFT at T2 calculation
      section: '../upload/archive/mainfile/DMFT/T2/dmft_t2.hdf5#/run/0/calculation/-1'
```

The workflow `tasks`:

```yaml
  tasks:
    - m_def: nomad.datamodel.metainfo.workflow.TaskReference
      task: '../upload/archive/mainfile/DFT/dft.xml#/workflow2'
      name: DFT
      inputs:
        - name: Input structure
          section: '../upload/archive/mainfile/DFT/dft.xml#/run/0/system/-1'
      outputs:
        - name: Output DFT calculation
          section: '../upload/archive/mainfile/DFT/dft.xml#/run/0/calculation/-1'
    - m_def: nomad.datamodel.metainfo.workflow.TaskReference
      task: '../upload/archive/mainfile/TB/tb.wout#/workflow2'
      name: TB
      inputs:
        - name: Input DFT calculation
          section: '../upload/archive/mainfile/DFT/dft.xml#/run/0/calculation/-1'
      outputs:
        - name: Output TB calculation
          section: '../upload/archive/mainfile/TB/tb.wout#/run/0/calculation/-1'
    - m_def: nomad.datamodel.metainfo.workflow.Workflow
      name: DMFT
      inputs:
        - name: input TB calculation
          section: '../upload/archive/mainfile/TB/tb.wout#/run/0/calculation/-1'
      outputs:
        - name: Output DMFT at T1 calculation
          section: '../upload/archive/mainfile/DMFT/T1/dmft_t1.hdf5#/run/0/calculation/-1'
        - name: Output DMFT at T2 calculation
          section: '../upload/archive/mainfile/DMFT/T2/dmft_t2.hdf5#/run/0/calculation/-1'
      tasks:
        - m_def: nomad.datamodel.metainfo.workflow.TaskReference
          task: '../upload/archive/mainfile/DMFT/T1/dmft_t1.hdf5#/workflow2'
          name: DMFT at T1
          inputs:
            - name: Input TB calculation
              section: '../upload/archive/mainfile/TB/tb.wout#/run/0/calculation/-1'
          outputs:
            - name: Output DMFT at T1 calculation
              section: '../upload/archive/mainfile/DMFT/T1/dmft_t1.hdf5#/run/0/calculation/-1'
        - m_def: nomad.datamodel.metainfo.workflow.TaskReference
          task: '../upload/archive/mainfile/DMFT/T2/dmft_t2.hdf5#/workflow2'
          name: DMFT at T2
          inputs:
            - name: Input TB calculation
              section: '../upload/archive/mainfile/TB/tb.wout#/run/0/calculation/-1'
          outputs:
            - name: Output DMFT at T2 calculation
              section: '../upload/archive/mainfile/DMFT/T2/dmft_t2.hdf5#/run/0/calculation/-1'
```

Most importantly for this example: In contrast to [Nested workflows > In multiple files](#in-multiple-entries), where `TaskReference` was used to define sub-workflows, the task named `DMFT` is defined directly as type `Workflow`.

When uploaded with the example data, this workflow file produces an Entry whose
**Overview** page initially shows the complete `DFT+TB+DMFT` workflow:

![Top-level nested workflow graph in the light theme](images/nested-workflow-parent-card-light.png#only-light){:.screenshot}
![Top-level nested workflow graph in the dark theme](images/nested-workflow-parent-card-dark.png#only-dark){:.screenshot}

Select the `DMFT` task to enter the sub-workflow. The graph then shows the
`DMFT at T1` and `DMFT at T2` tasks and their connections to the TB input and
the two DMFT outputs. Use the back arrow in the workflow toolbar to return to
the parent graph.

<!-- TODO: Regenerate both child images without --allow-missing-nested-tasks
after the GUI displays the nested DMFT tasks. The current captures show the
reported "No tasks to show" defect. -->

![DMFT sub-workflow graph in the light theme](images/nested-workflow-dmft-subworkflow-card-light.png#only-light){:.screenshot}
![DMFT sub-workflow graph in the dark theme](images/nested-workflow-dmft-subworkflow-card-dark.png#only-dark){:.screenshot}

You can reproduce this example by downloading the example data (with workflow YAML included at the root level), and uploading to NOMAD yourself:

[Download nested_workflow_one-entry.zip](data/nested_workflow_one-entry.zip){:.md-button .nomad-button}

## Workflows with custom tasks

A custom task is a task whose raw files NOMAD does not automatically recognize,
or a task that has no associated raw files. The task must still be represented by
an Entry before a workflow can reference it. One option is to create that Entry
from a built-in or custom ELN schema. See [Enter data with ELNs](eln.md) for
creating schema-based Entries and [Write a YAML schema package](yaml.md) for the
general schema concepts.

<!-- TODO(#363): Recheck the ELN and schema links after PR #363 is merged. -->

### Represent files with `ElnFileManager`

`ElnFileManager` is a built-in schema for referencing and annotating files in an
ELN Entry. To instantiate this schema from YAML, set `data.m_def` to its full
section-definition path. See [Schema package references](yaml.md#schema-package-references)
for the general purpose and syntax of `m_def`.

For example, the following file defines an Entry that describes the creation of
a force-field file:

<h4><code>create_force_field.archive.yaml</code></h4>
```yaml
data:
  m_def: 'nomad.datamodel.metainfo.eln.ElnFileManager'
  name: 'Create force field'
  description: 'The force field is defined for input to the MD simulation engine.'
  Files:
  - file: 'water.top'
    description: 'The force field file for simulation input.'
```

Upload the YAML file together with `water.top` so that the file reference can be
resolved during processing.

### Example workflow with ELN tasks

For a concrete example, consider a workflow consisting of three tasks for
setting up a molecular dynamics simulation. Each task receives parameters or an
execution script and produces a file.

Use `ElnFileManager` to create Entries for each task and the execution scripts.
The workflow parameters use the more general `ElnBaseSection` schema:

??? success "`create_force_field.archive.yaml`"

    ```yaml
    data:
      m_def: 'nomad.datamodel.metainfo.eln.ElnFileManager'
      name: 'Create force field'
      description: 'The force field is defined for input to the MD simulation engine.'
      Files:
      - file: 'Custom_ELN_Entries/water.top'
        description: 'The force field file for simulation input.'
    ```

??? success "`create_box.archive.yaml`"

    ```yaml
    data:
      m_def: 'nomad.datamodel.metainfo.eln.ElnFileManager'
      name: 'Create box'
      description: 'The initial simulation box is created.'
      Files:
      - file: 'Custom_ELN_Entries/box.gro'
        description: 'An empty structure file with the box vectors.'
    ```

??? success "`insert_water.archive.yaml`"

    ```yaml
    data:
      m_def: 'nomad.datamodel.metainfo.eln.ElnFileManager'
      name: 'Insert water'
      description: 'Water is inserted into the simulation box, creating the structure file for simulation input.'
      Files:
      - file: 'Custom_ELN_Entries/water.gro'
        description: 'The structure file for simulation input.'
    ```

??? success "`workflow_parameters.archive.yaml`"

    ```yaml
    data:
      m_def: nomad.datamodel.metainfo.eln.ElnBaseSection
      name: 'Workflow Parameters'
      description: 'This is a description of the overall workflow parameters, or alternatively standard workflow specification...'
    ```

??? success "`workflow_scripts.archive.yaml`"

    ```yaml
    data:
      m_def: 'nomad.datamodel.metainfo.eln.ElnFileManager'
      name: 'Workflow Scripts'
      description: 'All the scripts run during setup of the MD simulation.'
      Files:
      - file: 'Custom_ELN_Entries/workflow_script_1.py'
        description: 'Creates the simulation box and inserts water molecules.'
      - file: 'Custom_ELN_Entries/workflow_script_2.py'
        description: 'Creates the appropriate force field files for the simulation engine.'
    ```

Now we construct the workflow YAML, `setup_workflow.archive.yaml`, as in the examples above:

??? success "`setup_workflow.archive.yaml`"

    ```yaml
    workflow2:
      name: 'MD Setup workflow'
      inputs:
      - name: 'workflow parameters'
        section: '../upload/archive/mainfile/Custom_ELN_Entries/workflow_parameters.archive.yaml#/data'
      - name: 'workflow scripts'
        section: '../upload/archive/mainfile/Custom_ELN_Entries/workflow_scripts.archive.yaml#/data/Files'
      outputs:
      - name: 'structure file'
        section: '../upload/archive/mainfile/Custom_ELN_Entries/insert_water.archive.yaml#/data/Files/0/file'
      - name: 'force field file'
        section: '../upload/archive/mainfile/Custom_ELN_Entries/create_force_field.archive.yaml#/data/Files/0/file'
      tasks:
      - m_def: 'nomad.datamodel.metainfo.workflow.TaskReference'
        name: 'create box'
        task: '../upload/archive/mainfile/Custom_ELN_Entries/create_box.archive.yaml#/data'
        inputs:
        - name: 'workflow parameters'
          section: '../upload/archive/mainfile/Custom_ELN_Entries/workflow_parameters.archive.yaml#/data'
        - name: 'workflow script 1'
          section: '../upload/archive/mainfile/Custom_ELN_Entries/workflow_scripts.archive.yaml#/data/Files/0/file'
        outputs:
        - name: 'initial box'
          section: '../upload/archive/mainfile/Custom_ELN_Entries/create_box.archive.yaml#/data/Files/0/file'
      - m_def: 'nomad.datamodel.metainfo.workflow.TaskReference'
        name: 'insert water'
        task: '../upload/archive/mainfile/Custom_ELN_Entries/insert_water.archive.yaml#/data'
        inputs:
        - name: 'initial box'
          section: '../upload/archive/mainfile/Custom_ELN_Entries/create_box.archive.yaml#/data/Files/0/file'
        - name: 'workflow script 1'
          section: '../upload/archive/mainfile/Custom_ELN_Entries/workflow_scripts.archive.yaml#/data/Files/0/file'
        outputs:
        - name: 'structure file'
          section: '../upload/archive/mainfile/Custom_ELN_Entries/insert_water.archive.yaml#/data/Files/0/file'
      - m_def: 'nomad.datamodel.metainfo.workflow.TaskReference'
        name: 'create force field'
        task: '../upload/archive/mainfile/Custom_ELN_Entries/create_force_field.archive.yaml#/data'
        inputs:
        - name: 'workflow parameters'
          section: '../upload/archive/mainfile/Custom_ELN_Entries/workflow_parameters.archive.yaml#/data'
        - name: 'workflow script 2'
          section: '../upload/archive/mainfile/Custom_ELN_Entries/workflow_scripts.archive.yaml#/data/Files/1/file'
        outputs:
        - name: 'force field file'
          section: '../upload/archive/mainfile/Custom_ELN_Entries/create_force_field.archive.yaml#/data/Files/0/file'
    ```

After processing, the workflow Entry contains the following graph:

![Custom-task workflow graph in the light theme](images/custom-task-workflow-card-light.png#only-light){:.screenshot}
![Custom-task workflow graph in the dark theme](images/custom-task-workflow-card-dark.png#only-dark){:.screenshot}

To reproduce the example, download the bundle and add it to a Project. It
contains the referenced files, the Entry YAML files, and the workflow YAML shown
above.

[Download Custom_ELN_Entries.zip](data/Custom_ELN_Entries.zip){:.md-button .nomad-button}

## Referencing ELN entries created with the GUI

To reference ELN entries created using the NOMAD GUI, use the upload and entry ids for the archive path specification, as detailed in [Reference an Entry in another Project](#reference-an-entry-in-another-project) above.

## Creating workflow graphs with the GUI using the ELN interface

<!-- TODO - Add example, possibly from Tutorial 16? -->

!!! Warning

    Coming soon ...

<!-- TODO - also ensuring connections in the workflow visualizer! Somewhere -->
## Using the workflow visualizer

As we have seen above, when a workflow is defined within an entry, The Overview page will show an interactive graph of the `workflow2` section defined.
The following video demonstrates the basic navigation functionalities of these interactive workflow graphs:

<video controls autoplay loop muted playsinline class="screenshot">
  <source src="images/workflow-graph-usage.webm" type="video/webm">
</video>

The nodes (inputs, tasks and outputs) are shown from left to right for the current workflow layer.
The edges (arrows) from (to) a node denotes an input (output) to a section in the target node.
One can see the description for the nodes and edges by hovering over them. When the
inputs and outputs are clicked, the linked section is shown in the archive browser. By clicking
on a task, the graph zooms into the nested workflow layer. By clicking on the arrows,
only the relevant linked nodes are shown. One can go back to the previous view by clicking on
the current workflow node.

A number of controls are also provided on top of the graph. The first enables a filtering
of the nodes following a python-like syntax i.e., list (comma-separated) or range (colon-separated).
Negative index and percent are also supported. By default, the task nodes can be filtered
but can be changed to inputs or outputs by clicking on one of the respective nodes. By clicking
on the `play` button, a force-directed layout of the task nodes is enabled. The other tools
enable to toggle the legend, go back to a previous view and reset the view.

You can also use the graph to navigate to the referenced data, by clicking the labels above any task node or input/output, as shown in the following video:

<video width="100%" controls>
  <source src="./images/ELNFileManager.webm" alt="" type="video/webm">
</video>

Once you leave the workflow entry, you can use either the browser back button or, more generally, the "Entry References" section of the Overview page to navigate back to the workflow entry:

<!-- TODO Add a video of navigating via the references at the bottom of the page. -->

!!! Warning

    Illustrative video coming soon ...

!!! Tip "Proper creation of workflow entries"

    <!-- ! add tips for creating the visualization properly -->

    To ensure that the workflow visualizer functions correctly:

      - To create a graph edge, at least one `input` of the in-node must match exactly an `output` of the out-node.
<!-- TODO Add more tips -->

## Advanced Topics

### Instantiating a workflow from YAML using a standardized workflow class

!!! Warning

    Coming soon ...

### Extending the workflow schema

<!-- TODO Possibly update this example, and maybe define the scope of usage -->

The abstract workflow schema above allows us to build generalized tools for workflows,
like workflow searches, navigation in workflow, graphical representations of workflows, etc. But, you can still augment the given section definitions with more information through
inheritance. These information can be specialized references to denote inputs and outputs,
can be additional workflow or task parameters, and much more.

In this example, we created a special workflow section definition `GeometryOptimization`
that defines a parameter `threshold` and an additional reference to the final
calculation of the optimization:

```yaml
definitions:
  sections:
    GeometryOptimizationWorkflow:
      base_section: nomad.datamodel.metainfo.workflow.Workflow
      quantities:
        threshold:
          type: float
          unit: eV
        final_calculation:
          type: runschema.calculation.Calculation

workflow2:
  m_def: GeometryOptimizationWorkflow
  final_calculation: '#/run/0/calculation/-1'
  threshold: 0.029
  name: GeometryOpt
  inputs:
    ...
```
