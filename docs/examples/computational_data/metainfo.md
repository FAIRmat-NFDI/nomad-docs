# Guide to Computational MetaInfo

<!-- TODO replace everything below with the new schema description for data, and move to the simulation schema for data repo, then simply place a link here -->

<!-- TODO - already link to any existing DOCS for the new schema? -->

## Overview of metadata organization for computation

NOMAD stores all processed data in a well defined, structured, and machine readable format, known as the `archive`.
The schema that defines the organization of (meta)data within the archive is known as the [MetaInfo](../../reference/glossary.md#metainfo). See [Explanation > Data structure](../../explanation/data.md) for general information about data structures and schemas in NOMAD.

The following diagram is an overarching visualization of the most important archive sections for computational data:

```tree
archive
├── run
│    ├── method
│    │      ├── atom_parameters
│    │      ├── dft
│    │      ├── forcefield
│    │      └── ...
│    ├── system
│    │      ├── atoms
│    │      │     ├── positions
│    │      │     ├── lattice_vectors
│    │      │     └── ...
│    │      └── ...
│    └── calculation
│           ├── energy
│           ├── forces
│           └── ...
└── workflow2
     ├── method
     ├── inputs
     ├── tasks
     ├── outputs
     └── results
```

Entire subsections of NOMAD's schema can be browsed using the [MetaInfo Browser](https://nomad-lab.eu/prod/v1/gui/analyze/metainfo){:target="_blank"}:

- `run` base schema: [MetaInfo Browser > Entry > run](https://nomad-lab.eu/prod/v1/gui/analyze/metainfo/nomad.datamodel.datamodel.EntryArchive/run){:target="_blank"}
- `runschema` full schema for `run`: [MetaInfo Browser > runschema](https://nomad-lab.eu/prod/v1/gui/analyze/metainfo/runschema){:target="_blank"}
- `workflow2` base schema: [MetaInfo Browser > Entry > workflow2](https://nomad-lab.eu/prod/v1/gui/analyze/metainfo/nomad.datamodel.datamodel.EntryArchive/workflow2){:target="_blank"}
- `simulationworkflowschema` full computational schema for `workflow2`: [MetaInfo Browser > simulationworkflowschema](https://nomad-lab.eu/prod/v1/gui/analyze/metainfo/simulationworkflowschema){:target="_blank"}

The most important section of the archive for computational data is the `run` section, which is
divided into three main subsections: `method`, `system`, and `calculation`. `method` stores
information about the computational model used to perform the calculation.
`system` stores attributes of the atoms involved in the calculation, e.g., atom types, positions, lattice vectors, etc. `calculation` stores the output of the calculation, e.g., energy, forces, etc.
<!-- TODO Comment from ND - I would highlight the semantics of each section, since this is the main information to be communicated quickly. e.g. -->

The `workflow` section of the archive then stores information about the series of tasks performed
to accumulate the (meta)data in the run section. The relevant input parameters for the workflow are
stored in `method`, while the `results` section stores output from the workflow beyond observables
of single configurations.
For example, any ensemble-averaged quantity from a molecular dynamics
simulation would be stored under `workflow/results`. Then, the `inputs`, `outputs`, and `tasks` sections define the specifics of the workflow.
For some standard workflows, e.g., geometry optimization and molecular dynamics, the NOMAD [normalizers](../../explanation/processing.md#normalizing)
For non-standard workflows, the parser (or more appropriately the corresponding normalizer) must
populate these sections accordingly.
See [Explanation > Workflows](../../explanation/workflows.md) for more information about the general structure of the workflow section, and [How-to Guides > Customization > Define workflows](../../howto/customization/workflows.md) for instructions on how to upload custom workflows to link individual entries in NOMAD.
<!-- TODO Comment from ND - Wouldn't it be easier to say that its subsection reference other sections in run? I think this better summarizes the general rule. -->
<!-- TODO add graph showing how inputs, outputs, and tasks are connected  -->
<!-- TODO add reference page of standard computational workflows and link to the above sentence. -->
<!-- TODO Link to normalizer docs will automatically populate these specifics. The parser must only create the appropriate workflow section.  -->
<!-- TODO Should give an example somewhere -->
<!-- TODO specify which workflow sections have to be set by the parser: workflow2 or these standard workflows. -->

!!! warning "Attention"
    We are currently performing a complete refactoring of the computational MetaInfo schema. The new schema will be populated under the `data` section of the archive: [MetaInfo Browser > Entry > data](https://nomad-lab.eu/prod/v1/gui/analyze/metainfo/nomad.datamodel.datamodel.EntryArchive/data){:target="_blank"}. A preliminary version of the full schema can be browsed in [MetaInfo Browser > nomad_simulations](https://nomad-lab.eu/prod/v1/gui/analyze/metainfo/nomad_simulations){:target="_blank"}.

    Further information can be found within the schema plugin docs: [`nomad-simulations` Docs](https://nomad-coe.github.io/nomad-simulations/){:target="_blank"}.
