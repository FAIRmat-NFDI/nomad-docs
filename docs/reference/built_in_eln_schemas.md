# Built-in ELN schemas

This page documents the built-in schemas of the **Basic ELN** category in NOMAD.

For each schema, the tables below list the quantities and subsections in the order in
which the GUI shows them for a new entry. Most schemas inherit from NOMAD's base
sections documented in [Reference > Base sections](basesections.md).

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

**Description:** A basic electronic lab notebook for an analysis activity, e.g., processing measured data.

**Class name:** `ELNAnalysis`

**Inherits from:** [Reference > Base sections > Analysis](basesections.md#analysis)

**Quantities**

| Name | Label | Type | Description |
| --- | --- | --- | --- |
| `name` | **Name** | `str` | A short human-readable and descriptive name of the entry. |
| `datetime` | **Starting time** | `Datetime` | Date and time when the analysis started. |
| `lab_id` | **ID** | `str` | Human-readable ID that is unique at least within your lab. |
| `description` | **Description** | `str` | Any information that cannot be captured in the other fields. Supports formatted text. |
| `method` | **Method** | `str` | A short, consistent handle for the applied method. Shown read-only. |
| `location` | **Location** | `str` | Location of the analysis. |
| `tags` | **Tags** | `str` (array) | Keywords for finding the entry in searches. |

**Subsections**

| Name | Label | Type | Description |
| --- | --- | --- | --- |
| `steps` | **Steps** | [`ActivityStep`](basesections.md#activitystep) | Ordered steps of the analysis, each with a name, start time, and comment. NOMAD shows them as tasks in the workflow of the entry. |
| `inputs` | **Inputs** | [`SectionReference`](basesections.md#sectionreference) | References to the input data, shown as inputs in the workflow of the entry. |
| `outputs` | **Outputs** | `BasicAnalysisResult` | Results of the analysis, each with a name and formatted text, shown as outputs in the workflow of the entry. |
| `analysis_identifiers` | **Analysis identifiers** | [`ReadableIdentifiers`](basesections.md#readableidentifiers) | Values from which NOMAD creates the **ID**. |

## Basic ELN

**Description:** The most basic ELN to instantiate, with general fields and no subsections.

**Class name:** `BasicEln`

**Inherits from:** `ElnBaseSection`

**Quantities**

| Name | Label | Type | Description |
| --- | --- | --- | --- |
| `name` | **Short name** | `str` | A short human-readable and descriptive name of the entry. |
| `datetime` | **Datetime** | `Datetime` | Date and time associated with the entry. |
| `lab_id` | **ID** | `str` | Human-readable ID that is unique at least within your lab. |
| `description` | **Description** | `str` | Any information that cannot be captured in the other fields. Supports formatted text. |
| `tags` | **Tags** | `str` (array) | Keywords for finding the entry in searches. |

## Collection ELN

**Description:** A basic electronic lab notebook for a collection of entities, e.g., the samples of one batch.

**Class name:** `ELNCollection`

**Inherits from:** [Reference > Base sections > Collection](basesections.md#collection)

**Quantities**

| Name | Label | Type | Description |
| --- | --- | --- | --- |
| `name` | **Name** | `str` | A short human-readable and descriptive name of the entry. |
| `datetime` | **Datetime** | `Datetime` | Date and time associated with the entry. |
| `lab_id` | **ID** | `str` | Human-readable ID that is unique at least within your lab. |
| `description` | **Description** | `str` | Any information that cannot be captured in the other fields. Supports formatted text. |
| `tags` | **Tags** | `str` (array) | Keywords for finding the entry in searches. |

**Subsections**

| Name | Label | Type | Description |
| --- | --- | --- | --- |
| `entities` | **Entities** | [`EntityReference`](basesections.md#entityreference) | References to the entities in the collection, e.g., samples or substances. |
| `collection_identifiers` | **Collection identifiers** | [`ReadableIdentifiers`](basesections.md#readableidentifiers) | Values from which NOMAD creates the **ID**. |

## ElnFileManager

**Description:** A section for storing files, each with a description.

**Class name:** `ElnFileManager`

**Inherits from:** `ElnBaseSection`

**Quantities**

| Name | Label | Type | Description |
| --- | --- | --- | --- |
| `name` | **Short name** | `str` | A short human-readable and descriptive name of the entry. |
| `datetime` | **Datetime** | `Datetime` | Date and time associated with the entry. |
| `lab_id` | **ID** | `str` | Human-readable ID that is unique at least within your lab. |
| `description` | **Description** | `str` | Any information that cannot be captured in the other fields. Supports formatted text. |

**Subsections**

| Name | Label | Type | Description |
| --- | --- | --- | --- |
| `Files` | **Files** | `AnnotatedFile` | Files, each with a description. |

## Experiment ELN

**Description:** A basic electronic lab notebook for a collection of activities, e.g., the processes, measurements, and analyses of one experiment.

**Class name:** `ELNExperiment`

**Inherits from:** [Reference > Base sections > Experiment](basesections.md#experiment)

**Quantities**

| Name | Label | Type | Description |
| --- | --- | --- | --- |
| `name` | **Name** | `str` | A short human-readable and descriptive name of the entry. |
| `datetime` | **Starting time** | `Datetime` | Date and time when the experiment started. |
| `lab_id` | **ID** | `str` | Human-readable ID that is unique at least within your lab. |
| `description` | **Description** | `str` | Any information that cannot be captured in the other fields. Supports formatted text. |
| `method` | **Method** | `str` | A short, consistent handle for the applied method. Shown read-only. |
| `location` | **Location** | `str` | Location of the experiment. |
| `tags` | **Tags** | `str` (array) | Keywords for finding the entry in searches. |

**Subsections**

| Name | Label | Type | Description |
| --- | --- | --- | --- |
| `steps` | **Steps** | [`ExperimentStep`](basesections.md#experimentstep) | Ordered steps of the experiment, each with a name, start time, comment, and a reference to a process, measurement, or analysis. NOMAD shows them as tasks in the workflow of the entry. |
| `experiment_identifiers` | **Experiment identifiers** | [`ReadableIdentifiers`](basesections.md#readableidentifiers) | Values from which NOMAD creates the **ID**. |

## Generic Sample ELN

**Description:** A basic electronic lab notebook for a generic sample, e.g., a material that consists of one or more components.

**Class name:** `ELNSample`

**Inherits from:** [Reference > Base sections > CompositeSystem](basesections.md#compositesystem)

**Quantities**

| Name | Label | Type | Description |
| --- | --- | --- | --- |
| `name` | **Name** | `str` | A short human-readable and descriptive name of the entry. |
| `datetime` | **Datetime** | `Datetime` | Date and time associated with the entry. |
| `lab_id` | **ID** | `str` | Human-readable ID that is unique at least within your lab. |
| `description` | **Description** | `str` | Any information that cannot be captured in the other fields. Supports formatted text. |
| `tags` | **Tags** | `str` (array) | Keywords for finding the entry in searches. |

**Subsections**

| Name | Label | Type | Description |
| --- | --- | --- | --- |
| `elemental_composition` | **Elemental composition** | [`ElementalComposition`](basesections.md#elementalcomposition) | Elements in the sample, each with its atomic and mass fraction. |
| `components` | **Components** | [`Component`](basesections.md#component) | Components of the sample, each with a name, mass, and mass fraction. A component can reference another entry, e.g., a substance. |
| `sample_identifiers` | **Sample identifiers** | [`ReadableIdentifiers`](basesections.md#readableidentifiers) | Values from which NOMAD creates the **ID**. |

## Instrument ELN

**Description:** A basic electronic lab notebook for a generic instrument, e.g., one that is used in processes or measurements.

**Class name:** `ELNInstrument`

**Inherits from:** [Reference > Base sections > Instrument](basesections.md#instrument)

**Quantities**

| Name | Label | Type | Description |
| --- | --- | --- | --- |
| `name` | **Name** | `str` | A short human-readable and descriptive name of the entry. |
| `datetime` | **Datetime** | `Datetime` | Date and time associated with the entry. |
| `lab_id` | **ID** | `str` | Human-readable ID that is unique at least within your lab. |
| `description` | **Description** | `str` | Any information that cannot be captured in the other fields. Supports formatted text. |
| `tags` | **Tags** | `str` (array) | Keywords for finding the entry in searches. |

**Subsections**

| Name | Label | Type | Description |
| --- | --- | --- | --- |
| `instrument_identifiers` | **Instrument identifiers** | [`ReadableIdentifiers`](basesections.md#readableidentifiers) | Values from which NOMAD creates the **ID**. |

## Material Processing ELN

**Description:** A basic electronic lab notebook for a material processing activity, e.g., a synthesis or a deposition.

**Class name:** `ELNProcess`

**Inherits from:** [Reference > Base sections > Process](basesections.md#process)

**Quantities**

| Name | Label | Type | Description |
| --- | --- | --- | --- |
| `name` | **Name** | `str` | A short human-readable and descriptive name of the entry. |
| `datetime` | **Starting time** | `Datetime` | Date and time when the process started. |
| `lab_id` | **ID** | `str` | Human-readable ID that is unique at least within your lab. |
| `description` | **Description** | `str` | Any information that cannot be captured in the other fields. Supports formatted text. |
| `method` | **Method** | `str` | A short, consistent handle for the applied method. Shown read-only. |
| `location` | **Location** | `str` | Location of the process. |
| `end_time` | **Ending time** | `Datetime` | Date and time when the process finished. If it is empty, NOMAD can calculate it from **Starting time** and the step durations. |
| `tags` | **Tags** | `str` (array) | Keywords for finding the entry in searches. |

**Subsections**

| Name | Label | Type | Description |
| --- | --- | --- | --- |
| `steps` | **Steps** | [`ProcessStep`](basesections.md#processstep) | Ordered steps of the process, each with a name, start time, duration, and comment. NOMAD shows them as tasks in the workflow of the entry. |
| `instruments` | **Instruments** | [`InstrumentReference`](basesections.md#instrumentreference) | References to the instruments used in the process. |
| `samples` | **Samples** | [`CompositeSystemReference`](basesections.md#compositesystemreference) | References to the samples that the process produced or changed, shown as outputs in the workflow of the entry. |
| `process_identifiers` | **Process identifiers** | [`ReadableIdentifiers`](basesections.md#readableidentifiers) | Values from which NOMAD creates the **ID**. |

## Measurement ELN

**Description:** A basic electronic lab notebook for a measurement activity, e.g., a measurement on one or more samples.

**Class name:** `ELNMeasurement`

**Inherits from:** [Reference > Base sections > Measurement](basesections.md#measurement)

**Quantities**

| Name | Label | Type | Description |
| --- | --- | --- | --- |
| `name` | **Name** | `str` | A short human-readable and descriptive name of the entry. |
| `datetime` | **Starting time** | `Datetime` | Date and time when the measurement started. |
| `lab_id` | **ID** | `str` | Human-readable ID that is unique at least within your lab. |
| `description` | **Description** | `str` | Any information that cannot be captured in the other fields. Supports formatted text. |
| `method` | **Method** | `str` | A short, consistent handle for the applied method. Shown read-only. |
| `location` | **Location** | `str` | Location of the measurement. |
| `tags` | **Tags** | `str` (array) | Keywords for finding the entry in searches. |

**Subsections**

| Name | Label | Type | Description |
| --- | --- | --- | --- |
| `steps` | **Steps** | [`ActivityStep`](basesections.md#activitystep) | Ordered steps of the measurement, each with a name, start time, and comment. NOMAD shows them as tasks in the workflow of the entry. |
| `samples` | **Samples** | [`CompositeSystemReference`](basesections.md#compositesystemreference) | References to the measured samples, shown as inputs in the workflow of the entry. |
| `instruments` | **Instruments** | [`InstrumentReference`](basesections.md#instrumentreference) | References to the instruments used in the measurement. |
| `results` | **Results** | `BasicMeasurementResult` | Results of the measurement, each with a name and formatted text, shown as outputs in the workflow of the entry. |
| `measurement_identifiers` | **Measurement identifiers** | [`ReadableIdentifiers`](basesections.md#readableidentifiers) | Values from which NOMAD creates the **ID**. |

## Substance ELN

**Description:** A basic electronic lab notebook for a pure substance, e.g., a purchased chemical.

**Class name:** `ELNSubstance`

**Inherits from:** [Reference > Base sections > PureSubstance](basesections.md#puresubstance)

**Quantities**

| Name | Label | Type | Description |
| --- | --- | --- | --- |
| `name` | **Substance name** | `str` | Name of the substance. |
| `datetime` | **Datetime** | `Datetime` | Date and time associated with the entry. |
| `lab_id` | **Substance ID** | `str` | Human-readable ID of the substance that is unique at least within your lab. |
| `description` | **Detailed substance description** | `str` | Any information that cannot be captured in the other fields and subsections. Supports formatted text. |
| `tags` | **Tags** | `str` (array) | Keywords for finding the entry in searches. |

**Subsections**

| Name | Label | Type | Description |
| --- | --- | --- | --- |
| `elemental_composition` | **Elemental composition** | [`ElementalComposition`](basesections.md#elementalcomposition) | Elements in the substance, each with its atomic and mass fraction. |
| `pure_substance` | **Pure substance** | [`PureSubstanceSection`](basesections.md#puresubstancesection) | Properties of the substance, e.g., IUPAC name, molecular formula, molar mass, and CAS number. |
| `substance_identifiers` | **Substance identifiers** | [`ReadableIdentifiers`](basesections.md#readableidentifiers) | Values from which NOMAD creates the **Substance ID**. |

## Related pages

- {{ nav_link("tutorial/eln/built_in_templates.md", breadcrumb=True) }}
- {{ nav_link("tutorial/eln/custom_eln_yaml.md", breadcrumb=True) }}
- {{ nav_link("howto/manage/gui/upload.md", breadcrumb=True) }}
- {{ nav_link("reference/basesections.md", breadcrumb=True) }}
