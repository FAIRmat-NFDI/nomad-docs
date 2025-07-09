# How to define custom workflows

## What you will learn

- The following examples contain the basic knowledge on understanding and learning to use NOMAD workflows, and its relation with DFT and beyond-DFT (GW, BSE, DMFT, etc.) methodologies. You will use a fictitious example of a simulation workflow with the following files and folder structure:

## Recommended preparation

- Basic knowledge of NOMAD Organization + MetaInfo
-

## Further resources
- [Tutorial > Managing workflows and projects](../../tutorial/workflows_projects.md)

# New Structure

## Intro

In NOMAD, [Workflows](../../explanation/workflows.md) are directed graphs with nodes (tasks) that connect multiple [Entries](../../reference/glossary.md#entry) together in a structured way, while specifying information passed between the nodes via inputs/outputs that link to particular sections of the relevant [Archive](../../reference/glossary.md#archive).

Workflows are sometimes created automatically by NOMAD via parser [Plugins](../../explanation/plugin_system.md), for certain supported uploads. Users can also create their own workflow entries by uploading an appropriately formatted workflow YAML. This How-to guide will cover the specifics of this process.

!!! Note
    In the following, various supported raw data files will be used to form concrete examples that can be reproduced. The nature of these files or their underlying methods of production is irrelevant for the purpose of this How-to.

## Simple workflows with supported tasks

We start with the simplest possible workflow structure&mdash;a single task with one input and one output:

```mermaid
graph LR;
    A((Input structure)) --> B[DFT];
    B[DFT] --> C([Output calculation]);
```

The file associated with this task, `dft.xml`, is a standard DFT calculation that is supported by NOMAD's simulation parsers, i.e., upon upload it will be automatically recognized and parsed to create an entry. Actually, the parser for this file will automically create a "Single Point" workflow within the same entry, which specifies the standard input and outputs for simulation data in NOMAD:

![NOMAD workflow schema](images/single-point-nomad-workflow-graph.png){.screenshot}

Here, we will reproduce, and customize, this workflow graph in a separate entry, using the YAML-based approach.

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

This file is constructed according to NOMAD's [General Workflow Schema](../../explanation/workflows.md#the-built-in-abstract-workflow-schema). The `workflow2` section of the archive has 3 possible subsections: `inputs`, `outputs`, and `tasks`:

**`inputs`**: a list of references to the global inputs of the workflow, with `name` and `section` attributes. `section` corresponds to a path for linking to the relevant archive section. In this case, the relative section path is `run[0].system[-1]`, linked to the entry defined by the mainfile `dft.xml`. The prefix is discussed under "Considerations for archive path specification" below.

**`outputs`**: identical to the inputs list, representing the global outputs of the workflow, with the relative section path `run[0].calculation[-1]` in this case.

**`tasks`**: a list of references to the tasks/steps of the workflow. Each task contains `m_def`, `task`, `inputs`, and `outputs` attributes. `inputs`/`outputs` are task-specific versions of the lists defined above. `task` is the path for linking to the relevant archive section, analogous to the `section` attribute for `inputs`/`outputs`. `m_def` defines the type of task according to NOMAD's MetaInfo scehma, in this case a `TaskReference` to the archive `workflow2` section.  The use of `TaskReference` will be clarified in the
<!-- TODO add example section  -->
example below.

Considerations for archive path specification:

- In general, the archive path can be represented as `<prefix>/<entry identifier>/<relative archive path>`.

- The prefix for the archive path is given by: 1. `../upload/archive/mainfile` for entries that are contained within the same upload as the workflow YAML, or 2. `../uploads/<upload_id>/archive/` for entries contained in distinct uploads as the workflow YAML, where `<upload_id>` is a placeholders for the upload id, which can be obtained from the Overview page of any entry.

- The entry identifier is `<entry_id>#` (placeholder for the entry id, also found on the Overview page) for case 1, and `<path to mainfile>/<mainfile name>#` for case 2. `<path to mainfile>` is the path from the root of the original upload directory structure.

- The relative archive path is the relative path to the archive section to be linked. The archive structure can be investigated using NOMAD's [MetaInfo Browser](https://nomad-lab.eu/prod/v1/gui/analyze/metainfo/nomad.datamodel.datamodel.EntryArchive){:target="_blank"}.

With a basic understanding in hand, you can now download the example data and upload the obtained `.zip` file to NOMAD:

[Download simple_workflow.zip](data/simple_workflow.zip){ .md-button .nomad-button }

file structure of `simple_workflow.zip`:
```
.
├── dft.xml
├── dft.workflow.archive.yaml
```

Upon upload to NOMAD, the above zip will produce 2 entries:

1. A single point entry with mainfile `dft.xml`

2. a workflow entry with mainfile `dft.workflow.archive.yaml`. The workflow entry will contain the following workflow graph on the Overview page:

![NOMAD workflow schema](images/single-point-custom-nomad-workflow-graph.png){.screenshot}


??? Tip "Adding more workflow metadata"

    You could extend the workflow metadata by adding the metholodogical input parameters. These are stored in the archive with path `run[0].method[-1]`. The new `single_point.archive.yaml` will then be:

    ```yaml
    workflow2:
      name: DFT SinglePoint
      inputs:
        - name: Input system
          section: '../upload/archive/mainfile/dft.xml#/run/0/system/-1'
        - name: Input methodology parameters
          section: '../upload/archive/mainfile/pressure1/dft_p1.xml#/run/0/method/-1'
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
            - name: Input methodology parameters
              section: '../upload/archive/mainfile/dft.xml#/run/0/method/-1'
          outputs:
            - name: Output calculation
              section: '../upload/archive/mainfile/dft.xml#/run/0/calculation/-1'
    ```

    When uploaded with `dft.xml` as before, this will generate a similar workflow graph, but with an extra input node.

## Referencing Tasks in different uploads

As already mentioned above, your workflow YAML can reference entries that you have previously uploaded to NOMAD. In this case, you should replace the path prefix `../upload/archive/mainfile/<mainfile_name>` with `../uploads/<upload_id>/archive/<entry_id>`.

??? Tip "Corresponding `dft.workflow.archive.yaml` from above example"

    ```yaml
    workflow2:
      name: DFT SinglePoint
      inputs:
        - name: Input system
          section: '../upload/<upload_id>/archive/<entry_id>#/run/0/system/-1'
      outputs:
        - name: Output calculation
          section: '../upload/<upload_id>/archive/<entry_id>#/run/0/calculation/-1'
      tasks:
        - m_def: nomad.datamodel.metainfo.workflow.TaskReference
          task: '../upload/<upload_id>/archive/<entry_id>#/workflow2'
          name: DFT
          inputs:
            - name: Input structure
              section: '../upload/<upload_id>/archive/<entry_id>#/run/0/system/-1'
          outputs:
            - name: Output calculation
              section: '../upload/<upload_id>/archive/<entry_id>#/run/0/calculation/-1'
    ```


## Nested Workflows in a single entry

- it is possible to do this, but it's not the intuitive way for me at least, might want to motivate under what conditions this makes sense

Since a `Workflow` instance is also a `Tasks` instance due to inheritance, we can nest
workflows. Here we detailed the `GeometryOpt` as a *nested* workflow:

```yaml
workflow2:
  inputs:
    - name: input system
      section: '../upload/raw/geom_opt.archive.yaml#/run/0/system/0'
  outputs:
    - name: relaxed system
      section: '../upload/raw/geom_opt.archive.yaml#/run/0/system/-1'
    - name: ground state calculation of relaxed system
      section: '../upload/raw/ground_state.archive.yaml#/run/0/calculations/0'
  tasks:
    - name: GeometryOpt
      m_def: nomad.datamodel.metainfo.workflow.Workflow
      inputs:
        - name: input system
          section: '../upload/raw/geom_opt.archive.yaml#/run/0/system/0'
      outputs:
        - name: relaxed system
          section: '../upload/raw/geom_opt.archive.yaml#/run/0/system/-1'
      tasks:
        - inputs:
            - section: '../upload/raw/geom_opt.archive.yaml#/run/0/system/0'
          outputs:
            - section: '../upload/raw/geom_opt.archive.yaml#/run/0/system/1'
            - section: '../upload/raw/geom_opt.archive.yaml#/run/0/calculation/0'
        - inputs:
            - section: '../upload/raw/geom_opt.archive.yaml#/run/0/system/1'
          outputs:
            - section: '../upload/raw/geom_opt.archive.yaml#/run/0/system/2'
            - section: '../upload/raw/geom_opt.archive.yaml#/run/0/calculation/1'
        - inputs:
            - section: '../upload/raw/geom_opt.archive.yaml#/run/0/system/2'
          outputs:
            - section: '../upload/raw/geom_opt.archive.yaml#/run/0/system/3'
            - section: '../upload/raw/geom_opt.archive.yaml#/run/0/calculation/2'
    - name: GroundStateCalculation
      inputs:
        - name: input system
          section: '../upload/raw/geom_opt.archive.yaml#/run/0/system/-1'
      outputs:
        - name: ground state
          section: '../upload/raw/ground_state.archive.yaml#/run/0/calculations/0'
```

## Nested Workflows in multiple entries

- this actually applies to any reference of a simulation, but maybe we should build upon the previous example, i.e., using a yaml for the underlying workflow entry for clarity.

Whenever a workflow task corresponds to an existing entry that itself is a workflow, with the `workflow2` section of the archive populated, **best practice** is to link directly to this `workflow2` section, i.e., `task: <prefix>/<entry identifier>#/workflow2`. We have already seen this case in [Simple Workflows with Support Tasks](#simple-workflows-with-supported-tasks), as every simulation in NOMAD is implemented with its own `workflow2` section. In this case, and in general, one must then set `m_def: nomad.datamodel.metainfo.workflow.TaskReference`. This is because `Workflow` instances can only contain `Task` instances and not reference them (see [General Workflow Schema](../../explanation/workflows.md#the-built-in-abstract-workflow-schema)).

## Workflows with custom tasks

### Creating ELN entries from YAML files

- Basic example
- ELNFileManager

### Referencing ELN entries created with the GUI

- what is the mainfile?

### Creating workflow graphs directly from the GUI

- who can provide instructions?

## Best practices for workflow file management within a single upload?

Automatic workflows - from Chema:

There are some cases where the NOMAD infrastructure is able to recognize certain workflows automatically when processing the uploaded files. The simplest example is any `SinglePoint` calculation, as explained above. Other examples include `GeometryOptimization`, `Phonons`, `GW`, and `MolecularDynamics`. Automated workflow detection may require your folder structure to fulfill certain conditions.

Here are some general guidelines for preparing your upload folder in order to make it easier for the _automatic workflow recognition_ to work:

- Always organize your files in an **top-down structure**, i.e., the initial _tasks_ should be upper in the directory tree, while the later _tasks_ lower on it.
- Avoid having to go up and down between folders if some properties are derived between these files. These situations are very complicated to predict for the current NOMAD infrastructure.
- Avoid duplication of files in subfolders. If initially you do a calculation A from which a later calculation B is derived and you want to store B in a subfolder, there is no need to copy the A files inside the subfolder B.

The folder structure used throughout this part is a good example of a clean upload which is friendly and easy to work with when defining NOMAD workflows.

# **Example - Chema** - Standard and Custom Computational Workflows in NOMAD

# Standard and Custom Computational Workflows in NOMAD

<!-- TODO - Update this and link to utilities and tutorials -->

The following examples contain the basic knowledge on understanding and learning to use NOMAD workflows, and its relation with DFT and beyond-DFT (GW, BSE, DMFT, etc.) methodologies. You will use a fictitious example of a simulation workflow with the following files and folder structure:
```
.
├── pressure1
│   ├── temperature1
│   │   ├── dmft_p1_t1.hdf5
│   │   └── ...extra auxiliary files
│   ├── temperature2
│   │   ├── dmft_p1_t2.hdf5
│   │   └── ...extra auxiliary files
│   ├── dft_p1.xml
│   ├── tb_p1.wout
│   └── ...extra auxiliary files
└── pressure2
    ├── temperature1
    │   ├── dmft_p2_t1.hdf5
    │   └── ...extra auxiliary files
    ├── temperature2
    │   ├── dmft_p2_t2.hdf5
    │   └── ...extra auxiliary files
    ├── dft_p2.xml
    ├── tb_p2.wout
    └── ...extra auxiliary files
```

which can be downloaded here:
<!-- <center> -->
[Download example_files.zip](data/example_files.zip){ .md-button .nomad-button }
<!-- </center> -->

Each of the _mainfiles_ represent an electronic-structure calculation (either [DFT](https://en.wikipedia.org/wiki/Density_functional_theory){:target="_blank"}, [TB](https://en.wikipedia.org/wiki/Tight_binding){:target="_blank"}, or [DMFT](https://en.wikipedia.org/wiki/Dynamical_mean-field_theory){:target="_blank"}) which in turn is then parsed into a singular _entry_ in NOMAD. When dragged into the [NOMAD Upload page](https://nomad-lab.eu/prod/v1/staging/gui/user/uploads){:target="_blank"}, these files should generate 8 entries in total. This folder structure presents a typical workflow calculation which can be represented as a provenance graph:
```mermaid
graph LR;
    A2((Inputs)) --> B2[DFT];
    A1((Inputs)) --> B1[DFT];
    subgraph pressure P2
    B2[DFT] --> C2[TB];
    C2[TB] --> D21[DMFT at T1];
    C2[TB] --> D22[DMFT at T2];
    end
    D21[DMFT at T1] --> E21([Output calculation P2, T1])
    D22[DMFT at T2] --> E22([Output calculation P2, T2])
    subgraph pressure P1
    B1[DFT] --> C1[TB];
    C1[TB] --> D11[DMFT at T1];
    C1[TB] --> D12[DMFT at T2];
    end
    D11[DMFT at T1] --> E11([Output calculation P1, T1])
    D12[DMFT at T2] --> E12([Output calculation P1, T2])
```
Here, "Input" refers to the all _input_ information given to perform the calculation (e.g., atom positions, model parameters, experimental initial conditions, etc.). "DFT", "TB" and "DMFT" refer to individual _tasks_ of the workflow, which each correspond to a _SinglePoint_ entry in NOMAD. "Output calculation" refers to the _output_ data of each of the final DMFT tasks.

The goal of this part is to set up the following workflows:

1. A `SinglePoint` workflow for one of the calculations (e.g., the DFT one) in the `pressure1` subfolder.
2. An overarching workflow entry for each pressure P<sub>i=1,2</sub>, grouping all `SinglePoint` "DFT", "TB", "DMFT at T<sub>1</sub>", and "DMFT at T<sub>2</sub>" tasks.
3. A top level workflow entry, grouping together all pressure calculations.

The files for all these cases can be downloaded here:
<center>
[Download worfklowyaml_files.zip](data/workflowyaml_files.zip){ .md-button .nomad-button }
</center>

 You can try writing these files yourself first, and then compare them with the tested files.


## Starting example: SinglePoint workflow

NOMAD is able to recognize certain workflows in an automatic way, such as the `SinglePoint` case mentioned above. However, to showcase how to the use workflows in NOMAD, you will learn how to "manually" construct the SinglePoint workflow, represented by the following provenance graph:
```mermaid
graph LR;
    A((Inputs)) --> B[DFT];
    B[DFT] --> C([Output calculation]);
```
To define a workflow manually in NOMAD, you must add a YAML file to the upload folder that contains the relevant input, output, and task information. This file should be named `<filename>.archive.yaml`. In this case, you should include the file `single_point.archive.yaml` with the following content:

```yaml
workflow2:
  name: SinglePoint
  inputs:
    - name: Input structure
      section: '../upload/archive/mainfile/pressure1/dft_p1.xml#/run/0/system/-1'
  outputs:
    - name: Output calculation
      section: '../upload/archive/mainfile/pressure1/dft_p1.xml#/run/0/calculation/-1'
  tasks:
    - m_def: nomad.datamodel.metainfo.workflow.TaskReference
      task: '../upload/archive/mainfile/pressure1/dft_p1.xml#/workflow2'
      name: DFT at Pressure P1
      inputs:
        - name: Input structure
          section: '../upload/archive/mainfile/pressure1/dft_p1.xml#/run/0/system/-1'
      outputs:
        - name: Output calculation
          section: '../upload/archive/mainfile/pressure1/dft_p1.xml#/run/0/calculation/-1'
```

Note several things about the content of this file:

1. **`name`** keys are optional.
2. The root path of the upload can be referenced with `../upload/archive/mainfile/`. Starting from there, the original directory tree structure of the upload is maintained.
3. **`inputs`** reference the section containing inputs of the whole workflow. In this case this is the section `run[0].system[-1]` parsed from the mainfile in the path `pressure1/dft_p1.xml`.
4. **`outputs`** reference the section containing outputs of the whole workflow. In this case this is the section `run[0].calculation[-1]` parsed from the mainfile in the path `pressure1/dft_p1.xml`.
5. **`tasks`** reference the section containing tasks of each step in the workflow. These must also contain `inputs` and `outputs` properly referencing the corresponding sections; this will then _link_ inputs/outputs/tasks in the NOMAD Archive. In this case this is a `TaskReference` to the section `workflow2` parsed from the mainfile in the path `pressure1/dft_p1.xml`.
6. **`section`** reference to the uploaded mainfile specific section. The left side of the `#` symbol contains the path to the _mainfile_, while the right contains the path to the _section_.

This will produce an extra entry with the following Overview content:

![NOMAD workflow schema](images/singlepoint.png){.screenshot}

Note that you are referencing sections which are lists. Thus, in each case you should be careful to reference the correct section for inputs and outputs (example: a `GeometryOptimization` workflow calculation will have the "Input structure" as `run[0].system[0]`, while the "Output calculation" would also contain `run[0].system[-1]`, and all intermediate steps must input/output the corresponding section system).

!!! note "NOMAD workflow filename"
    The NOMAD workflow YAML file name, i.e., `<filename>` in the explanation above, can be any custom name defined by the user, but the file **must** keep the extension `.archive.yaml` at the end. This is done in order for NOMAD to recognize this file as a _custom schema_. Custom schemas are widely used in experimental parsing, and you can learn more about them in the [FAIRmat tutorial 8](https://www.fairmat-nfdi.eu/events/fairmat-tutorial-8/tutorial-8-home).

You can extend the workflow meta-information by adding the metholodogical input parameters. These are stored in NOMAD in the section path `run[0].method[-1]`. The new `single_point.archive.yaml` will be:

```yaml
workflow2:
  name: SinglePoint
  inputs:
    - name: Input structure
      section: '../upload/archive/mainfile/pressure1/dft_p1.xml#/run/0/system/-1'
    - name: Input methodology parameters
      section: '../upload/archive/mainfile/pressure1/dft_p1.xml#/run/0/method/-1'
  outputs:
    - name: Output calculation
      section: '../upload/archive/mainfile/pressure1/dft_p1.xml#/run/0/calculation/-1'
  tasks:
    - m_def: nomad.datamodel.metainfo.workflow.TaskReference
      task: '../upload/archive/mainfile/pressure1/dft_p1.xml#/workflow2'
      name: DFT at Pressure P1
      inputs:
        - name: Input structure
          section: '../upload/archive/mainfile/pressure1/dft_p1.xml#/run/0/system/-1'
        - name: Input methodology parameters
          section: '../upload/archive/mainfile/pressure1/dft_p1.xml#/run/0/method/-1'
      outputs:
        - name: Output calculation
          section: '../upload/archive/mainfile/pressure1/dft_p1.xml#/run/0/calculation/-1'
```

which in turn produces a similar workflow than before, but with an extra input node:

![SinglePoint workflow visualizer with Method added](images/singlepoint_methodadded.png){.screenshot}


## Pressure workflows

Now that you know the basics of the workflow YAML schema, let's try to define an overarching workflow for each of the pressures. For this section, you will learn how to create the workflow YAML schema for the P<sub>1</sub> case; the extension for P<sub>2</sub> is then a matter of changing names and paths in the YAML files. For simplicity, you can skip referencing to methodologies.

Thus, the `inputs` can be defined as:
```yaml
workflow2:
  name: DFT+TB+DMFT at P1
  inputs:
    - name: Input structure
      section: '../upload/archive/mainfile/pressure1/dft_p1.xml#/run/0/system/-1'
```
and there are two `outputs`, one for each of the DMFT calculations at distinct temperatures:
```yaml
  outputs:
    - name: Output DMFT at P1, T1 calculation
      section: '../upload/archive/mainfile/pressure1/temperature1/dmft_p1_t1.hdf5#/run/0/calculation/-1'
    - name: Output DMFT at P1, T2 calculation
      section: '../upload/archive/mainfile/pressure1/temperature2/dmft_p1_t2.hdf5#/run/0/calculation/-1'
```
Now, `tasks` are defined for each of the methodologies performed (each corresponding to an underlying SinglePoint workflow). To define a valid workflow, each task must contain an input that corresponds to one of the outputs of the previous task. Moreover, the first task should take as input the overall input of the workflow, and the final task should also have as an output the overall workflow output.
Then:
```yaml
  tasks:
    - m_def: nomad.datamodel.metainfo.workflow.TaskReference
      task: '../upload/archive/mainfile/pressure1/dft_p1.xml#/workflow2'
      name: DFT at P1
      inputs:
        - name: Input structure
          section: '../upload/archive/mainfile/pressure1/dft_p1.xml#/run/0/system/-1'
      outputs:
        - name: Output DFT at P1 calculation
          section: '../upload/archive/mainfile/pressure1/dft_p1.xml#/run/0/calculation/-1'
    - m_def: nomad.datamodel.metainfo.workflow.TaskReference
      task: '../upload/archive/mainfile/pressure1/tb_p1.wout#/workflow2'
      name: TB at P1
      inputs:
        - name: Input DFT at P1 calculation
          section: '../upload/archive/mainfile/pressure1/dft_p1.xml#/run/0/calculation/-1'
      outputs:
        - name: Output TB at P1 calculation
          section: '../upload/archive/mainfile/pressure1/tb_p1.wout#/run/0/calculation/-1'
    - m_def: nomad.datamodel.metainfo.workflow.TaskReference
      task: '../upload/archive/mainfile/pressure1/temperature1/dmft_p1_t1.hdf5#/workflow2'
      name: DMFT at P1 and T1
      inputs:
        - name: Input TB at P1 calculation
          section: '../upload/archive/mainfile/pressure1/tb_p1.wout#/run/0/calculation/-1'
      outputs:
        - name: Output DMFT at P1, T1 calculation
          section: '../upload/archive/mainfile/pressure1/temperature1/dmft_p1_t1.hdf5#/run/0/calculation/-1'
    - m_def: nomad.datamodel.metainfo.workflow.TaskReference
      task: '../upload/archive/mainfile/pressure1/temperature1/dmft_p1_t1.hdf5#/workflow2'
      name: DMFT at P1 and T2
      inputs:
        - name: Input TB at P1 calculation
          section: '../upload/archive/mainfile/pressure1/tb_p1.wout#/run/0/calculation/-1'
      outputs:
        - name: Output DMFT at P1, T2 calculation
          section: '../upload/archive/mainfile/pressure1/temperature2/dmft_p1_t2.hdf5#/run/0/calculation/-1'
```
Note here:

- The `inputs` for each subsequent step are the `outputs` of the previous step.
- The final two `outputs` coincide with the `workflow2` `outputs`.

This workflow (`pressure1.archive.yaml`) file will then produce an entry with the following Overview page:

![Pressure P1 workflow visualizer](images/pressure1.png){.screenshot}

Similarly, for P<sub>2</sub> you can upload a new `pressure2.archive.yaml` file with the same content, except when substituting 'pressure1' and 'p1' by their counterparts. This will produce a similar graph than the one showed before but for "P2".


## The top-level workflow

After adding the workflow YAML files, Your upload folder directory now looks like:
```
.
├── pressure1
│   │   ├── dmft_p1_t1.hdf5
│   │   └── ...extra auxiliary files
│   ├── temperature2
│   │   ├── dmft_p1_t2.hdf5
│   │   └── ...extra auxiliary files
│   ├── dft_p1.xml
│   ├── tb_p1.wout
│   └── ...extra auxiliary files
├── pressure1.archive.yaml
├── pressure2
│   ├── temperature1
│   │   ├── dmft_p2_t1.hdf5
│   │   └── ...extra auxiliary files
│   ├── temperature2
│   │   ├── dmft_p2_t2.hdf5
│   │   └── ...extra auxiliary files
│   ├── dft_p2.xml
│   ├── tb_p2.wout
│   └── ...extra auxiliary files
├── pressure2.archive.yaml
└── single_point.archive.yaml
```
In order to define the general workflow that groups all pressure calculations, YOU can reference directly the previous `pressureX.archive.yaml` files as tasks. Still, `inputs` and `outputs` must be referenced to their corresponding mainfile and section paths.

Create a new `fullworkflow.archive.yaml` file with the `inputs`:
```yaml
workflow2:
  name: Full calculation at different pressures for SrVO3
  inputs:
    - name: Input structure at P1
      section: '../upload/archive/mainfile/pressure1/dft_p1.xml#/run/0/system/-1'
    - name: Input structure at P2
      section: '../upload/archive/mainfile/pressure2/dft_p2.xml#/run/0/system/-1'
```
And `outputs`:
```yaml
  outputs:
    - name: Output DMFT at P1, T1 calculation
      section: '../upload/archive/mainfile/pressure1/temperature1/dmft_p1_t1.hdf5#/run/0/calculation/-1'
    - name: Output DMFT at P1, T2 calculation
      section: '../upload/archive/mainfile/pressure1/temperature2/dmft_p1_t2.hdf5#/run/0/calculation/-1'
    - name: Output DMFT at P2, T1 calculation
      section: '../upload/archive/mainfile/pressure2/temperature1/dmft_p2_t1.hdf5#/run/0/calculation/-1'
    - name: Output DMFT at P2, T2 calculation
      section: '../upload/archive/mainfile/pressure2/temperature2/dmft_p2_t2.hdf5#/run/0/calculation/-1'
```
Finally, `tasks` references the previous YAML schemas as follows:
```yaml
  tasks:
    - m_def: nomad.datamodel.metainfo.workflow.TaskReference
      task: '../upload/archive/mainfile/pressure1.archive.yaml#/workflow2'
      name: DFT+TB+DMFT at P1
      inputs:
        - name: Input structure at P1
          section: '../upload/archive/mainfile/pressure1/dft_p1.xml#/run/0/system/-1'
      outputs:
        - name: Output DMFT at P1, T1 calculation
          section: '../upload/archive/mainfile/pressure1/temperature1/dmft_p1_t1.hdf5#/run/0/calculation/-1'
        - name: Output DMFT at P1, T2 calculation
          section: '../upload/archive/mainfile/pressure1/temperature2/dmft_p1_t2.hdf5#/run/0/calculation/-1'
    - m_def: nomad.datamodel.metainfo.workflow.TaskReference
      task: '../upload/archive/mainfile/pressure2.archive.yaml#/workflow2'
      name: DFT+TB+DMFT at P2
      inputs:
        - name: Input structure at P2
          section: '../upload/archive/mainfile/pressure2/dft_p2.xml#/run/0/system/-1'
      outputs:
        - name: Output DMFT at P2, T1 calculation
          section: '../upload/archive/mainfile/pressure2/temperature1/dmft_p2_t1.hdf5#/run/0/calculation/-1'
        - name: Output DMFT at P2, T2 calculation
          section: '../upload/archive/mainfile/pressure2/temperature2/dmft_p2_t2.hdf5#/run/0/calculation/-1'
```

This will produce the following entry and its Overview page:

![Full workflow visualizer](images/fullworkflow.png){.screenshot}



# **Example - Alvin**


### Nested Workflows in multiple entries

Typically, we want to colocate our individual workflows with their inputs and outputs.
In the case of the geometry optimization, we might want to put this into the archive of
the geometry optimization code run. So the `geom_opt.archive.yaml` might contain its
own section `workflow2` that only contains the `GeometryOpt` workflow and uses local
references to its inputs and outputs:

```yaml
workflow2:
  name: GeometryOpt
  inputs:
    - name: input system
      section: '#/run/0/system/0'
  outputs:
    - name: relaxed system
      section: '#/run/0/system/-1'
  tasks:
    - inputs:
        - section: '#/run/0/system/0'
      outputs:
        - section: '#/run/0/system/1'
        - section: '#/run/0/calculation/0'
    - inputs:
        - section: '#/run/0/system/1'
      outputs:
        - section: '#/run/0/system/2'
        - section: '#/run/0/calculation/1'
    - inputs:
        - section: '#/run/0/system/2'
      outputs:
        - section: '#/run/0/system/3'
        - section: '#/run/0/calculation/2'
run:
  - program:
      name: 'VASP'
    system: [{}, {}, {}]
    calculation: [{}, {}, {}]
```

When we want to detail the complex workflow, we now need to refer to a nested workflow in
a different entry. This cannot be done directly, because `Workflow` instances can only contain `Task` instances and not reference them. Therefore, we added a `TaskReference` section definition that can be used to create proxy instances for tasks and workflows:

```yaml
workflow2:
  inputs:
    - name: input system
      section: '../upload/raw/geom_opt.archive.yaml#/run/0/system/0'
  outputs:
    - name: relaxed system
      section: '../upload/raw/geom_opt.archive.yaml#/run/0/system/-1'
    - name: ground state calculation of relaxed system
      section: '../upload/raw/ground_state.archive.yaml#/run/0/calculations/0'
  tasks:
    - m_def: nomad.datamodel.metainfo.workflow.TaskReference
      task: '../upload/raw/geom_opt.archive.yaml#/workflow2'
    - name: GroundStateCalculation
      inputs:
        - name: input system
          section: '../upload/raw/geom_opt.archive.yaml#/run/0/system/-1'
      outputs:
        - name: ground state
          section: '../upload/raw/ground_state.archive.yaml#/run/0/calculations/0'
```

### Instantiating a workflow from YAML using a standardized workflow class

## Extending the workflow schema

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

# How to use the workflow visualizer
The entry overview page will show an interactive graph of the `workflow2` section if defined.
In the following example, a workflow containing three tasks `Single Point`, `Geometry Optimization`
and `Phonon` is shown.

![workflow visualizer](images/workflow-graph-usage.gif)

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


<!-- TODO - Add ../upload/raw/ prefix -->