# How to use base sections

A *base section* is a section definition that other definitions inherit from. Inheriting instead of
redefining aligns your schema with other schemas, and lets NOMAD's built-in tooling — search,
workflow visualization, ELN components — recognize your data.

For what the available base sections mean and why they are shaped the way they are, see
{{ nav_link("explanation/base_sections.md", breadcrumb=True) }}. For the generated per-class
reference, see {{ nav_link("reference/basesections.md", breadcrumb=True) }}.

## Inherit from a base section

Inheritance lets you create a *specialized* definition from a more *abstract* one. The specialized
definition inherits all properties of its base and can add more.

In YAML, use `base_section`:

```yaml
definitions:
  sections:
    Process:
      quantities:
        time:
          type: Datetime
    Evaporation:
      base_section: Process
      quantities:
        pressure:
          type: np.float64
          unit: Pa
    Annealing:
      base_section: Process
      quantities:
        temperature:
          type: np.float64
          unit: K
```

`Annealing` and `Evaporation` both inherit `time`, so it does not need to be repeated. An
`Evaporation` instance uses both the inherited and the added quantity:

```yaml
data:
  m_def: Evaporation
  time: '2022-10-13 12:00:00'
  pressure: 100
```

In Python, inheritance is ordinary class inheritance:

```python
from nomad.datamodel.data import ArchiveSection, EntryData
from nomad.metainfo import Datetime, Quantity


class Process(ArchiveSection):
    time = Quantity(type=Datetime)


class Evaporation(Process, EntryData):
    pressure = Quantity(type=np.float64, unit='Pa')
```

Sections support multiple inheritance, which is how a section becomes both a specialized concept and
an entry root section at the same time — `Evaporation` above is both a `Process` and an `EntryData`.

## Choose the right base section

- Inherit from the **most specialized** base section that still fits your data. The more specific the
  base, the more built-in functionality applies to your entries.
- Add `nomad.datamodel.data.EntryData` to any section that should be usable as the root section of an
  entry. `EntryData` is an abstract placeholder — it is what makes your section appear under an
  entry's `data`.
- Use `nomad.datamodel.data.ArchiveSection` for any section that needs a `normalize` function.

## Commonly used built-in base sections

| Section definition or package | Purpose |
| --- | --- |
| `nomad.datamodel.EntryArchive` | The root object of all NOMAD entries. |
| `nomad.datamodel.EntryMetadata` | Standard NOMAD metadata: ids, upload, processing and author information. |
| `nomad.datamodel.EntryData` | The abstract section definition for an entry's `data` section. |
| `nomad.datamodel.ArchiveSection` | Adds support for `normalize` functions. |
| `nomad.datamodel.metainfo.basesections.*` | The entity–activity base sections: samples, instruments, processes, measurements, analyses. |
| `nomad.datamodel.metainfo.eln.*` | Commonly used ELN quantities. These are indexed, so specializations can use the NOMAD search. |
| `nomad.datamodel.metainfo.workflow.*` | The definitions NOMAD uses to model workflows. |
| `nomad.metainfo.*` | The schema language itself. See {{ nav_link("reference/metainfo.md", breadcrumb=True) }}. |
| `nomad.parsing.tabular.TableData` | Inherit parsing of `.csv` and `.xls` files. See [Parse tabular data](./tabular.md). |
| `nomad.datamodel.metainfo.basesections.HDF5Normalizer` | Link quantities to HDF5 datasets for large data. See {{ nav_link("howto/plugins/tools/hdf5.md", breadcrumb=True) }}. |

## Rely on polymorphism

When a subsection or reference declares an abstract section, any *specialization* of that section is
a valid value. This is what lets one schema define a relationship and another schema extend what can
fill it.

Define the relationship against the abstract definition:

**abstract.archive.yaml**

```yaml
definitions:
  sections:
    Process:
      quantities:
        time:
          type: Datetime
    Sample:
      sub_sections:
        processes:
          section: Process
          repeats: true
```

Then specialize it elsewhere:

**specialized.archive.yaml**

```yaml
definitions:
  sections:
    Evaporation:
      base_section: ../upload/raw/abstract.archive.yaml#Process
      quantities:
        pressure:
          type: np.float64
          unit: Pa
    Annealing:
      base_section: ../upload/raw/abstract.archive.yaml#Process
      quantities:
        temperature:
          type: np.float64
          unit: K
```

The section declared in the `processes` subsection defines what a contained section must be *at
least*, so both specializations fit:

```yaml
definitions:
  # see above
data:
  m_def: ../upload/raw/abstract.archive.yaml#Sample
  processes:
  - m_def: Evaporation
    time: '2022-10-13'
    pressure: 100
  - m_def: Annealing
    time: '2022-10-13'
    temperature: 342
```

Polymorphism works the same way in Python: iterating a subsection yields instances of whichever
subclass was actually stored, and their specialized properties are available on each one.

## Compose readable identifiers

Some base sections are designed to be *composed* into your section rather than inherited. For
example, `ReadableIdentifiers` generates a human-readable `lab_id` from the surrounding context:

```python
class MySample(CompositeSystem, EntryData):
    """
    A custom sample section.
    """

    m_def = Section(
        a_template=dict(
            sample_identifiers=dict(),
        ),
    )
    sample_identifiers = SubSection(
        section_def=ReadableIdentifiers,
    )
```

## Extend an existing section

Sometimes you need to add properties to a section you do not own — typically a parser adding
code-specific quantities to a shared definition. Use `extends_base_section` together with an
`x_<name>_` prefix on every added property:

```python
from nomad.metainfo import MEnum, Quantity, Section
from nomad.datamodel.metainfo.workflow import Workflow


class MyCodeRun(Workflow):
    m_def = Section(extends_base_section=True)
    x_mycode_execution_mode = Quantity(
        type=MEnum('hpc', 'parallel', 'single'), description='...'
    )
```

Unlike normal inheritance, this modifies the base section itself, so every entry using `Workflow`
gains the new property. Use it sparingly and only for parser-specific additions; prefer a subsection
or a normal specialization where you can.

## Related materials

- {{ nav_link("howto/schemas/references.md", breadcrumb=True) }} — link to sections across entries.
- {{ nav_link("reference/basesections.md", breadcrumb=True) }} — the generated base section reference.
- {{ nav_link("tutorial/eln/built_in_templates.md", breadcrumb=True) }} — the built-in base sections in the GUI.
