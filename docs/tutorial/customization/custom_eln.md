# Creating a custom ELN schema in NOMAD

Here, we will go through steps of creating a custom schema in NOMAD with ELN functionality. This schema will allow researchers to document and manage experiments related to polymer thin-film processing, which was discussed previously. The steps introduced here follow the **six guidelines** for building a custom schema introduced earlier.

## Step 1: Create a file with `.archive.yaml` extension

To start, we create a file, name it `polymer_processing` with the extension `.archive.yaml`

## Step 2: Define the schema

A custom schema must begin with the `definitions:` keyword, specifying a `name:` (guideline 1). In order to introduce the main section(s) of the schema, the keyword `sections:` is used.

```yaml
definitions:
  name: Processing of polymers thin-films
  sections:
```

## Step 3: Define the main section

The schema must contain at least one section. Here, we define `Experiment_Information` as the main section that will hold experiment-related metadata (guideline 2). We inherit from `nomad.datamodel.data.EntryData` to ensure compatibility with NOMAD's data model (guideline 3). 

```yaml
definitions:
  name: Processing of polymers thin-films
  sections:
    Experiment_Information:
      base_sections: 
        - nomad.datamodel.data.EntryData
```

## Step 4: Add quantities to the main section

We define four quantities: `Name`, `Researcher`, `Date`, and `Additional_Notes` (guideline 4), and define their type (guideline 5) and default values (optional).

```yaml
quantities:
  Name:
    type: str  
    default: Experiment title
  Researcher:
    type: str
    default: Name of the researcher who performed the experiment
  Date:
    type: Datetime
  Additional_Notes:
    type: str
```

## Step 5: Annotate the quantities to be treated as ELN components

Now, we need to instruct NOMAD to treat these quantities as editable components of ELN using annotations (guideline 5). 

We instruct NOMAD that the `Name` quantity (title of the experiment), is an ELN field (`m_annotations: eln`), which should provide an editable piece of short text component via `component: StringEditQuantity`:

```yaml
m_annotations:
  eln:
    component: StringEditQuantity 
```
Same annotation should be used for the `Researcher` quantity, because we want it also to be an editable piece of short text ELN component.

The `Date` quantity, is an ELN field (`m_annotations: eln`) providing an editable date/time component (`component: DateTimeEditQuantity
`) as follows:

```yaml
m_annotations:
  eln:
    component: DateTimeEditQuantity
```
The `Additional_Notes` quantity, is an ELN field (`m_annotations: eln`), providing an editable rich text field component (`component: RichTextEditQuantity`) as following:

```yaml
m_annotations:
  eln:
    component: RichTextEditQuantity
```
at this stage, our three annotated quantities which will be treated as editable eln components look like this:

```yaml
quantities:
  Name:
    type: str  
    default: Experiment title
    m_annotations:
      eln:
        component: StringEditQuantity
  Researcher:
    type: str
    default: Name of the researcher who performed the experiment
    m_annotations:
      eln:
        component: StringEditQuantity
  Date:
    type: Datetime
    m_annotations:
      eln:
        component: DateTimeEditQuantity
  Additional_Notes:
    type: str
    m_annotations:
      eln:
        component: RichTextEditQuantity
```
At this stage, our schema is complete and functional, built entirely using the six basic guidelines. Most other features build upon the same principles. You can already save the following snippet as a `.archive.yaml` file and upload it to NOMAD — it will work as a custom ELN schema.

```yaml
definitions:
  name: Processing of polymers thin-films
  sections:
    Experiment_Information:
      base_sections: 
        - nomad.datamodel.data.EntryData
      quantities:
        Name:
          type: str  
          default: Experiment title
          m_annotations:
            eln:
              component: StringEditQuantity
        Researcher:
          type: str
          default: Name of the researcher who performed the experiment
          m_annotations:
            eln:
              component: StringEditQuantity
        Date:
          type: Datetime
          m_annotations:
            eln:
              component: DateTimeEditQuantity
        Additional_Notes:
          type: str
          m_annotations:
            eln:
              component: RichTextEditQuantity
```
In the next steps, we’ll add more subsections and introduce useful patterns and tips, including links to relevant how-to guides where needed.

## Step 6: Add subsections (`Sample`, `Solution`, `Preparation`)

We introduce three subsections to our main section (`Experiment_Information`) : `Sample` and `Solution` and `Preparation`. Remember from guideline 4 that the name of the subsection we introduce should be given indented under `sub_sections:` keyword, and this name should be followed with an indented `section:` keyword. Once this is done, everything else can be written similar to what we had until now for the main section, the `Experiment_Information`.

```yaml
sub_sections:
  Sample:
    section:
      ...
  Solution:
    section:
      ...
  Preparation:
    section:
      ...
```

### Step 6.1: The `Sample` subsection

Now let's begin with the `Sample` subsection: 

```yaml
Sample:
  section:
    base_sections:
      - nomad.datamodel.metainfo.eln.Sample
    m_annotations:
      eln:
        overview: true
        hide: ['chemical_formula']
```

??? tip "About the Sample subsection definition"

    - Here, we inherit only from `nomad.datamodel.metainfo.eln.Sample` and not explicitly from `EntryData`.  
      This is because `eln.Sample` already inherits from `ElnBaseSection`, which in turn inherits from `ArchiveSection`, providing similar functionality as `EntryData`.

    - The annotation `overview: true` instructs NOMAD to display this subsection in the **OVERVIEW** tab of the ELN interface.

    - With `hide: ['chemical_formula']`, we explicitly hide the `chemical_formula` field that is originally defined in the base section `eln.Sample`. This is useful for simplifying the ELN interface by removing unnecessary fields.

### Step 6.2: The `Solution` subsection

For the `Solution` subsection as a start, we define it as follows:

```yaml
Solution:
  section:
    base_sections:
      - nomad.datamodel.metainfo.eln.Sample
    m_annotations:
      eln:
        overview: true
        hide: ['chemical_formula', 'description']
    quantities:
      Concentration:
        type: np.float64
        unit: mg/ml
        m_annotations:
          eln:
            component: NumberEditQuantity
```
??? tip "About the Solution subsection definition"

    - The `Solution` subsection inherits from `nomad.datamodel.metainfo.eln.Sample`, similar to the previous subsection (`Sample`).

    - We use `hide: ['chemical_formula', 'description']` to remove unnecessary fields (`chemical_formula` and `description`) inherited from the base section `nomad.datamodel.metainfo.eln.Sample`, thus simplifying the user interface.

    - We introduced a new `quantity` called `Concentration`, specifying:
        - `type: np.float64`: a numeric value.
        - `unit: mg/ml`: specifying units clearly for user inputs.
        - An ELN annotation (`component: NumberEditQuantity`) that creates an editable numeric input field in the ELN interface.

At this stage, our `Solution` subsection is almost complete. However, we can further detail it by specifying the `Solute` and `Solvent` nested subsections, clearly documenting the substances used in preparing the polymer solution.

Here's how we define these additional subsections of the `Solution` subsection itself:

```yaml
sub_sections:
  Solute:
    section:
      quantities:
        Substance:
          type: nomad.datamodel.metainfo.eln.ELNSubstance
          m_annotations:
            eln:
              component: ReferenceEditQuantity
        Mass:
          type: np.float64
          unit: kilogram
          m_annotations:
            eln:
              component: NumberEditQuantity
              defaultDisplayUnit: milligram
  Solvent:
    section:
      quantities:
        Substance:
          type: nomad.datamodel.metainfo.eln.ELNSubstance
          m_annotations:
            eln:
              component: ReferenceEditQuantity
        Volume:
          type: np.float64
          unit: meter ** 3
          m_annotations:
            eln:
              component: NumberEditQuantity
              defaultDisplayUnit: milliliter
```

??? tip "Details on the Solute and Solvent subsections"

    - Here, instead of inheriting from NOMAD base sections (using the keyword `base_sections:`) we defined the **type** of the subsections (`Solute` and `Solvent`) to be a reference quantity (`type: nomad.datamodel.metainfo.eln.ELNSubstance`).

    - We also used the eln annotation `component: ReferenceEditQuantity` that allows users to link directly to substances previously defined or imported into NOMAD.

    - `Mass` and `Volume` are defined as editable numeric inputs (`component: NumberEditQuantity`) with explicit units (`kilogram` for mass, `meter**3` for volume). For ease of use in the ELN interface in the GUI, convenient default display units (`milligram` and `milliliter`, respectively) are specified via the `defaultDisplayUnit` annotation.

### Step 6.3: The `Preparation` subsection

The `Preparation` subsection documents the processing steps involved in preparing polymer thin-films:

```yaml
Preparation:
  section:
    base_sections:
      - nomad.datamodel.metainfo.eln.Process  
    m_annotations:
      eln:
        overview: true
```
## Step 7: Final check for correct indentations

Indentation in YAML is quite important, as incorrect indentation will result in errors when loading your schema into NOMAD. As a rule of thumb:


- All sections or quantities at the same hierarchical level should share the same indentation (obviously!). For example, in this custom schema, the subsections `Sample`, `Solution`, and `Preparation` are all at the same hierarchical level and thus share the same indentation.
- Attributes defining a section (`base_sections`, `quantities`, `sub_sections`, `m_annotations`, etc.) must be indented exactly **one additional level (2 spaces)** relative to their parent section.
- Similarly, attributes defining a quantity (`type`, `unit`, `default`, `m_annotations`, etc.) must be indented exactly **one additional level (2 spaces)** relative to the quantity itself.

An IDE (e.g., VS Code) can significantly simplify working with YAML files. It provides syntax highlighting, automatic indentation checks, and error highlighting, helping you visualize and ensure correctness in your schema file.

Below is the overview of YAML structure demonstrating correct indentation for the schema we wrote:

```yaml
definitions:
  name: Processing of polymers thin-films
  sections:
    Experiment_Information:
      base_sections: ...
      quantities: ...
      sub_sections:
        Sample:
          section: ...
        Solution:
          section: ...
          sub_sections:
            Solute:
              section: ...
            Solvent:
              section: ...
        Preparation:
          section: ...
```


Finally, the complete YAML schema file incorporating all previous definitions is provided below. You can directly copy it into a `.archive.yaml` file and upload it to NOMAD as a functional custom ELN schema.

```yaml
definitions:
  name: Processing of polymers thin-films
  sections:
    Experiment_Information:
      base_sections: 
        - nomad.datamodel.data.EntryData
      quantities:
        Name:
          type: str  
          default: Experiment title
          m_annotations:
            eln:
              component: StringEditQuantity
        Researcher:
          type: str
          default: Name of the researcher who performed the experiment
          m_annotations:
            eln:
              component: StringEditQuantity
        Date:
          type: Datetime
          m_annotations:
            eln:
              component: DateTimeEditQuantity
        Additional_Notes:
          type: str
          m_annotations:
            eln:
              component: RichTextEditQuantity
      sub_sections:
        Sample:
          section:
            base_sections:
              - nomad.datamodel.metainfo.eln.Sample
            m_annotations:
              eln:
                overview: true
                hide: ['chemical_formula']
        Solution:
          section:
            base_sections:
              - nomad.datamodel.metainfo.eln.Sample
            m_annotations:
              eln:
                overview: true
                hide: ['chemical_formula', 'description']
            quantities:
              Concentration:
                type: np.float64
                unit: mg/ml
                m_annotations:
                  eln:
                    component: NumberEditQuantity
            sub_sections:
              Solute:
                section:
                  quantities:
                    Substance:
                      type: nomad.datamodel.metainfo.eln.ELNSubstance
                      m_annotations:
                        eln:
                          component: ReferenceEditQuantity
                    Mass:
                      type: np.float64
                      unit: kilogram
                      m_annotations:
                        eln:
                          component: NumberEditQuantity
                          defaultDisplayUnit: milligram
              Solvent:
                section:
                  quantities:
                    Substance:
                      type: nomad.datamodel.metainfo.eln.ELNSubstance
                      m_annotations:
                        eln:
                          component: ReferenceEditQuantity
                    Volume:
                      type: np.float64
                      unit: meter ** 3
                      m_annotations:
                        eln:
                          component: NumberEditQuantity
                          defaultDisplayUnit: milliliter
        Preparation:
          section:
            base_sections:
              - nomad.datamodel.metainfo.eln.Process  
            m_annotations:
              eln:
                overview: true
```





