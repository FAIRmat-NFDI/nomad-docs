# How to link data with references

Subsections express a *part-of* relationship: a section contains another section. When your data is
more inter-linked than that — a measurement pointing at the sample it measured, a composition
pointing at elements defined elsewhere — use a *reference*.

A reference is a uni-directional link from a *source* section to a *target* section. You define it as
a quantity on the source whose `type` is the target's section definition.

## Define a reference quantity

In YAML, use the target section definition as the quantity's `type`:

```yaml
Composition:
  quantities:
    composition:
      type: str
    elements:
      type: Element
      shape: ['*']
```

Here `type: Element` refers to the section definition `Element`, much like `section: Element` does in
a subsection. The `shape` describes the dimensionality of the *references* themselves — a single
reference versus an array of them — not the shape of the referenced data.

In Python, use the section or quantity you want to point at as the type:

```python
class Calculation(MSection):
    system = Quantity(type=System.m_def)
    atom_labels = Quantity(type=System.atom_labels)


calc = Calculation()
calc.system = run.systems[-1]
calc.atom_labels = run.systems[-1]
```

In memory, a reference quantity simply holds a Python reference to the target section instance.

!!! note
    *Value references* — where the type is a quantity rather than a section, as with `atom_labels`
    above — behave differently. Reading one gives you the referenced *value*, but internally NOMAD
    stores a reference to the section holding that quantity. So when assigning, assign the
    **section**, not the value.

## How references are serialized

Where subsections serialize as nested objects, references serialize as strings. A reference is a path
of `/`-separated keys starting from the archive root, where list items are addressed by index:

```yaml
composition: H2O
elements: ['#/data/periodic_table/elements/0', '#/data/periodic_table/elements/1']
```

Given the full archive:

```yaml
data:
 periodic_table:
   elements:
   - label: H
     density: 8.375e-05
     isotopes: [1, 2, 3]
   - label: O
     density: 1.141
     isotopes: [16, 17, 18]
 compositions:
 - composition: H2O
   elements: ['#/data/periodic_table/elements/0', '#/data/periodic_table/elements/1']
```

following the keys `data`, `periodic_table`, `elements`, `0` reaches the section representing
hydrogen.

### Different forms of references

An inter-entry reference has two parts, `<entry>#<section>`: a path or URL denoting the target entry,
and a path within that entry's subsection hierarchy. The host and path parts correspond to the
[NOMAD API](../manage/program/api.md).

| Example reference | Meaning |
| --- | --- |
| `#/data/periodic_table/elements/0` | A section within the same archive. |
| `/run/0/calculation/1` | A section within the same archive (legacy form). |
| `Element` | A *section definition* in the same archive. Targets section definitions only. |
| `nomad.datamodel.metainfo.workflow` | A *section definition* written in Python as part of the NOMAD code. Targets section definitions only. |
| `../upload/raw/data.archive.yaml#/data` | A section in a different `.archive.yaml` file of the same upload. |
| `../upload/archive/mainfile/data.archive.yaml#/data` | A section in a processed archive, given by the entry *mainfile*. |
| `../upload/archive/zxhS43h2kqHsVDqMboiP9cULrS_v#/data` | A section in a processed archive, given by entry id. |
| `../uploads/zxhS43h2kqHsVDqMboiP9cULrS_v/raw/data.archive.yaml#/data` | A section in an entry of a different upload. |
| `/entries/{entry_id}/archive#/run/0/calculation/1` | A section in a different entry on the same NOMAD installation. |
| `/uploads/{upload_id}/archive/{entry_id}#/run/0/calculation/1` | The same, addressed by upload. |
| `https://mylab.eu/oasis/api/v1/uploads/{upload_id}/raw/data.archive.yaml#/data` | A section in a different NOMAD installation. |

### Schema package references

Schema packages contain references too. Writing `type: Element` or `section: Element` is a reference
to a *section definition* — a convenience form standing in for the otherwise cryptic
`#/definitions/sections/0`.

This is also what `m_def` is for. Whenever the section definition cannot be determined from context —
from the subsection key that contains it — `m_def` carries a reference to the definition explicitly.

## Reference across entries

A reference in one entry's archive can point into another entry's archive. These two files show the
pattern:

**periodic_table.archive.yaml**

```yaml
definitions:
  sections:
    Element:
      quantities:
        label:
          type: str
        density:
          type: np.float64
          unit: g/cm**3
        isotopes:
          type: int
          shape: ['*']
    PeriodicTable:
      sub_sections:
        elements:
          repeats: true
          section: Element
data:
  m_def: PeriodicTable
  elements:
  - label: H
    density: 0.00008375
    isotopes: [1, 2, 3]
  - label: O
    density: 1.141
    isotopes: [16, 17, 18]
```

**composition.archive.yaml**

```yaml
definitions:
  sections:
    Composition:
      quantities:
        composition:
          type: str
        elements:
          type: ../upload/raw/periodic_table.archive.yaml#Element
          shape: ['*']
data:
  m_def: Composition
  composition: 'H2O'
  elements:
    - ../upload/raw/periodic_table.archive.yaml#data/elements/0
    - ../upload/raw/periodic_table.archive.yaml#data/elements/1
```

Note that this splits the *schema package* across files as well: one file defines and holds the
periodic table, the other defines and holds the composition that uses it.

## Resolve references lazily with proxies

References are serialized automatically by `m_to_dict`. On deserialization with `m_from_dict` they
are **not** resolved immediately, because the target section may not be loaded yet. Instead they are
stored as `MProxy` instances, which are transparently replaced by the real section the first time the
quantity is accessed.

When the target is not yet defined at the point where you need it — a circular dependency, or simply
Python import order — use `SectionProxy` with the name of the definition:

```python
class Calculation(MSection):
    system = Quantity(type=SectionProxy('System'))
```

The string is a path within the available definitions, so this works as long as `System` is
eventually defined in the same package.

## Related materials

- {{ nav_link("howto/schemas/base_sections.md", breadcrumb=True) }} — reference targets can be polymorphic.
- {{ nav_link("howto/manage/gui/workflows.md", breadcrumb=True) }} — references between workflow tasks.
- {{ nav_link("reference/metainfo.md", breadcrumb=True) }} — reference types in the type table.
