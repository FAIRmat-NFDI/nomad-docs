# Built-in ELN schemas

This page lists the built-in schemas of the **Basic ELN** category, which are
part of NOMAD itself. They are listed in the **BUILT-IN SCHEMAS** tab after you
select **NEW ENTRY** in a project. Plugins can add further built-in schemas in
other categories.

For each schema, the tables list the fields and subsections in the order in
which the GUI shows them for a new entry. Most schemas are based on a section
from [Base sections](basesections.md), where the complete definitions are
generated from the NOMAD source code.

## Values filled in automatically

When NOMAD processes an ELN entry, it fills in the following fields if they are
empty:

- **Name**, **Short name**, or **Substance name**: the filename without the
  `.archive.json` extension, with underscores replaced by spaces.
- **Datetime** or **Starting time**: the creation time of the entry.
- **ID** or **Substance ID**: an ID of the form
  `<institute>_<owner>_<date>_<name>`, created in the identifiers subsection of
  the entry, e.g., **Substance identifiers**. The institute is abbreviated from
  the affiliation of the entry's author, the owner combines the first two
  letters of the author's first and last name, the date comes from **Datetime**
  or **Starting time**, and the name comes from **Name** or **Substance name**,
  with hyphens instead of spaces and underscores. If the author's account has no
  affiliation, NOMAD creates the ID only after you enter an institute in the
  identifiers subsection.

*Basic ELN* and *ElnFileManager* have no identifiers subsection. Their **ID**
remains empty unless you enter it.

## Analysis ELN

For an analysis activity, e.g., processing measured data. Code name
`ELNAnalysis`, based on [`Analysis`](basesections.md#analysis).

| Field | Code name | Description |
| --- | --- | --- |
| **Name** | `name` | Name of the entry. |
| **Starting time** | `datetime` | Date and time when the analysis started. |
| **ID** | `lab_id` | Human-readable ID that is unique at least within your lab. |
| **Description** | `description` | Formatted free text for information that the other fields do not capture. |
| **Method** | `method` | Short name of the applied method. Shown read-only. |
| **Location** | `location` | Where the analysis took place. |
| **Tags** | `tags` | Keywords for finding the entry in searches. |

| Subsection | Code name | Description |
| --- | --- | --- |
| **Steps** | `steps` | Ordered steps of the analysis, each with a name, start time, and comment. NOMAD shows them as tasks in the workflow of the entry. |
| **Inputs** | `inputs` | References to the input data, shown as inputs in the workflow of the entry. |
| **Outputs** | `outputs` | Results of the analysis, each with a name and formatted text, shown as outputs in the workflow of the entry. |
| **Analysis identifiers** | `analysis_identifiers` | Values from which NOMAD creates the **ID**. |

## Basic ELN

The simplest built-in schema, with general fields and no subsections. Code name
`BasicEln`, based on `ElnBaseSection`.

| Field | Code name | Description |
| --- | --- | --- |
| **Short name** | `name` | Short, descriptive name of the entry. |
| **Datetime** | `datetime` | Date and time associated with the entry. |
| **ID** | `lab_id` | Human-readable ID that is unique at least within your lab. |
| **Description** | `description` | Formatted free text for information that the other fields do not capture. |
| **Tags** | `tags` | Keywords for finding the entry in searches. |

## Collection ELN

For a group of entities that belong together, e.g., the samples of one batch.
Code name `ELNCollection`, based on
[`Collection`](basesections.md#collection).

| Field | Code name | Description |
| --- | --- | --- |
| **Name** | `name` | Name of the entry. |
| **Datetime** | `datetime` | Date and time associated with the entry. |
| **ID** | `lab_id` | Human-readable ID that is unique at least within your lab. |
| **Description** | `description` | Formatted free text for information that the other fields do not capture. |
| **Tags** | `tags` | Keywords for finding the entry in searches. |

| Subsection | Code name | Description |
| --- | --- | --- |
| **Entities** | `entities` | References to the entities in the collection, e.g., samples or substances. |
| **Collection identifiers** | `collection_identifiers` | Values from which NOMAD creates the **ID**. |

## ElnFileManager

For storing files, each with a description. Code name `ElnFileManager`, based
on `ElnBaseSection`.

| Field | Code name | Description |
| --- | --- | --- |
| **Short name** | `name` | Short, descriptive name of the entry. |
| **Datetime** | `datetime` | Date and time associated with the entry. |
| **ID** | `lab_id` | Human-readable ID that is unique at least within your lab. |
| **Description** | `description` | Formatted free text for information that the other fields do not capture. |

| Subsection | Code name | Description |
| --- | --- | --- |
| **Files** | `Files` | Files, each with a description. |

## Experiment ELN

For an experiment that combines processes, measurements, and analyses. Code
name `ELNExperiment`, based on [`Experiment`](basesections.md#experiment).

| Field | Code name | Description |
| --- | --- | --- |
| **Name** | `name` | Name of the entry. |
| **Starting time** | `datetime` | Date and time when the experiment started. |
| **ID** | `lab_id` | Human-readable ID that is unique at least within your lab. |
| **Description** | `description` | Formatted free text for information that the other fields do not capture. |
| **Method** | `method` | Short name of the applied method. Shown read-only. |
| **Location** | `location` | Where the experiment took place. |
| **Tags** | `tags` | Keywords for finding the entry in searches. |

| Subsection | Code name | Description |
| --- | --- | --- |
| **Steps** | `steps` | Ordered steps of the experiment, each with a name, start time, comment, and a reference to a process, measurement, or analysis. NOMAD shows them as tasks in the workflow of the entry. |
| **Experiment identifiers** | `experiment_identifiers` | Values from which NOMAD creates the **ID**. |

## Generic Sample ELN

For a sample, e.g., a material that consists of one or more components. Code
name `ELNSample`, based on
[`CompositeSystem`](basesections.md#compositesystem).

| Field | Code name | Description |
| --- | --- | --- |
| **Name** | `name` | Name of the entry. |
| **Datetime** | `datetime` | Date and time associated with the entry. |
| **ID** | `lab_id` | Human-readable ID that is unique at least within your lab. |
| **Description** | `description` | Formatted free text for information that the other fields do not capture. |
| **Tags** | `tags` | Keywords for finding the entry in searches. |

| Subsection | Code name | Description |
| --- | --- | --- |
| **Elemental composition** | `elemental_composition` | Elements in the sample, each with its atomic and mass fraction. |
| **Components** | `components` | Components of the sample, each with a name, mass, and mass fraction. A component can reference another entry, e.g., a substance. |
| **Sample identifiers** | `sample_identifiers` | Values from which NOMAD creates the **ID**. |

## Instrument ELN

For an instrument that is used in processes or measurements. Code name
`ELNInstrument`, based on [`Instrument`](basesections.md#instrument).

| Field | Code name | Description |
| --- | --- | --- |
| **Name** | `name` | Name of the entry. |
| **Datetime** | `datetime` | Date and time associated with the entry. |
| **ID** | `lab_id` | Human-readable ID that is unique at least within your lab. |
| **Description** | `description` | Formatted free text for information that the other fields do not capture. |
| **Tags** | `tags` | Keywords for finding the entry in searches. |

| Subsection | Code name | Description |
| --- | --- | --- |
| **Instrument identifiers** | `instrument_identifiers` | Values from which NOMAD creates the **ID**. |

## Material Processing ELN

For a process that produces or changes a material, e.g., a synthesis or a
deposition. Code name `ELNProcess`, based on
[`Process`](basesections.md#process).

| Field | Code name | Description |
| --- | --- | --- |
| **Name** | `name` | Name of the entry. |
| **Starting time** | `datetime` | Date and time when the process started. |
| **ID** | `lab_id` | Human-readable ID that is unique at least within your lab. |
| **Description** | `description` | Formatted free text for information that the other fields do not capture. |
| **Method** | `method` | Short name of the applied method. Shown read-only. |
| **Location** | `location` | Where the process took place. |
| **Ending time** | `end_time` | Date and time when the process finished. If it is empty, NOMAD can calculate it from **Starting time** and the step durations. |
| **Tags** | `tags` | Keywords for finding the entry in searches. |

| Subsection | Code name | Description |
| --- | --- | --- |
| **Steps** | `steps` | Ordered steps of the process, each with a name, start time, duration, and comment. NOMAD shows them as tasks in the workflow of the entry. |
| **Instruments** | `instruments` | References to the instruments used in the process. |
| **Samples** | `samples` | References to the samples that the process produced or changed, shown as outputs in the workflow of the entry. |
| **Process identifiers** | `process_identifiers` | Values from which NOMAD creates the **ID**. |

## Measurement ELN

For a measurement on one or more samples. Code name `ELNMeasurement`, based on
[`Measurement`](basesections.md#measurement).

| Field | Code name | Description |
| --- | --- | --- |
| **Name** | `name` | Name of the entry. |
| **Starting time** | `datetime` | Date and time when the measurement started. |
| **ID** | `lab_id` | Human-readable ID that is unique at least within your lab. |
| **Description** | `description` | Formatted free text for information that the other fields do not capture. |
| **Method** | `method` | Short name of the applied method. Shown read-only. |
| **Location** | `location` | Where the measurement took place. |
| **Tags** | `tags` | Keywords for finding the entry in searches. |

| Subsection | Code name | Description |
| --- | --- | --- |
| **Steps** | `steps` | Ordered steps of the measurement, each with a name, start time, and comment. NOMAD shows them as tasks in the workflow of the entry. |
| **Samples** | `samples` | References to the measured samples, shown as inputs in the workflow of the entry. |
| **Instruments** | `instruments` | References to the instruments used in the measurement. |
| **Results** | `results` | Results of the measurement, each with a name and formatted text, shown as outputs in the workflow of the entry. |
| **Measurement identifiers** | `measurement_identifiers` | Values from which NOMAD creates the **ID**. |

## Substance ELN

For a pure substance, e.g., a purchased chemical. Code name `ELNSubstance`,
based on [`PureSubstance`](basesections.md#puresubstance).

| Field | Code name | Description |
| --- | --- | --- |
| **Substance name** | `name` | Name of the substance. |
| **Datetime** | `datetime` | Date and time associated with the entry. |
| **Substance ID** | `lab_id` | Human-readable ID of the substance that is unique at least within your lab. |
| **Detailed substance description** | `description` | Formatted free text for information that the other fields and subsections do not capture. |
| **Tags** | `tags` | Keywords for finding the entry in searches. |

| Subsection | Code name | Description |
| --- | --- | --- |
| **Elemental composition** | `elemental_composition` | Elements in the substance, each with its atomic and mass fraction. |
| **Pure substance** | `pure_substance` | Properties of the substance, e.g., IUPAC name, molecular formula, molar mass, and CAS number. |
| **Substance identifiers** | `substance_identifiers` | Values from which NOMAD creates the **Substance ID**. |

## Related pages

- {{ nav_link("tutorial/eln/built_in_templates.md", breadcrumb=True) }}
- {{ nav_link("tutorial/eln/custom_eln_yaml.md", breadcrumb=True) }}
- {{ nav_link("howto/manage/gui/upload.md", breadcrumb=True) }}
- {{ nav_link("reference/basesections.md", breadcrumb=True) }}
