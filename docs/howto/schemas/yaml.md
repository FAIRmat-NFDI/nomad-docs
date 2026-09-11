# How to write a YAML schema package

This guide explains how to write and upload NOMAD schema packages in the YAML format that can be uploaded as part of your data. This is a good way to start out experimenting with custom data structures in NOMAD, but for more advanced use cases you may need to use [Python schema packages](../plugins/types/schema_packages.md). For more information on how an archive file is composed, visit [Explanation > Data structure](../../explanation/data.md).

## Example data

Let's assume we want to describe chemical compositions using the elements they contain.
The following structured data (in this example as a `.yaml` document) could describe the composition of water.

```yaml
composition: H2O
elements:
- label: H
  density: 8.375e-05
  isotopes: [1, 2, 3]
- label: O
  density: 1.141
  isotopes: [16, 17, 18]
```

In structured data formats (such as `.yaml` or `.json`), data is put into combinations
of *primitive values* (e.g. `'H2O'`, `1.141`), *objects* (a set of *keys* and *value* pairs, where *values* can be *objects*, *lists*, or *primitive values*), and *lists* of *values*.

## Sections

In a schema package, we want to describe the structure of data, i.e. what are the allowed combinations of *objects*, *lists*, and *primitive values*.
The crucial task here is to define what *keys* certain *types of objects* can have and what possible *values* might exist for each of these keys.

In NOMAD, we call *objects* **sections** and we define *types of objects* with **section
definitions**. Since *objects* can be nested, **sections** become like the sections and
subsections of a book or paper. Sections are a representation of data and they are
the building blocks for [**archives**](../../reference/glossary.md#archive). Section definitions form a schema package and they are
the building blocks for the [**metainfo**](../../reference/glossary.md#metainfo).

In the above example, we have two *types* of *objects*: an overaching object for the entire structure
(with *keys* for `composition` and `elements`), and an additional object which describes the internal structure of
`elements` (with *keys* for `label`, `density`, and `isotopes`). Let's start with
the *definition* for elements. This is what the *section definition* looks like in NOMAD's yaml-based schema package format:

```yaml
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
```

A *section definition* provides all the available *keys* for a *section* that instantiates
this *definition*. For each *key*, e.g. `label`, `density`, `isotopes`, it provides
more information on the possible values.

Let's have a look at the overall definition for our chemical composition:

```yaml
Composition:
  quantities:
    composition:
      type: str
  sub_sections:
    elements:
      section: Element
      repeats: true
```

Again, all possible *keys* (`composition` and `elements`) are defined. But now we see
that there are two different types of *keys*, **quantities** and **subsections**. We
say that *section definitions* can have **properties** (e.g. the *keys* they define) and
there are two distinct types of *properties*.

## Quantities

*Quantities* define possible *primitive values*. The basic properties that go into
a *quantity definition* are:

- **type**: what kind of *primitive value* can be used, e.g. `str` or `np.float64`
- **shape**: what is the shape of the value, e.g. scalar or list (`['*']`)
- **unit**: what is the physical meaning of the value

The *names* of *quantity definitions* serve as the *key*, used in respective *section objects*.

### Type

This is a list of supported quantity types.

|type|description|
|-|-|
|`string`||
|`str`||
|`float`||
|`integer`||
|`int`||
|`boolean`||
|`bool`||
|`np.int32`|Numpy based integer with 32 bits.|
|`np.int64`|Numpy based integer with 64 bits.|
|`np.float32`|Numpy based float with 32 bits.|
|`np.float64`|Numpy based float with 64 bits.|
|`Datetime`||
|`User`|A type for NOMAD users as values.|
|`Author`|A complex type for author information.|
|`{type_kind: Enum, type_data: []}`|Use `type_data` to specify enum values as list of strings.|
|`*<section name>*`|To define a quantity that is a reference to a specific section.|

### Shape

The shape of a quantity is a list of *dimensions*, where each *dimension* defines the
possible size of that *dimension*. The empty list (or no shape) describes a scalar value,
a list with one *dimension* a list or vector, a list with two *dimensions* a matrix, etc.

Dimensions can be given as:

- an integer number to define a fixed size, e.g. a 3x3 matrix would have shape `[3, 3]`.
- the string `'*'` to denote am arbitrary sized dimension, e.g. a list quantity would have shape `['*']`.
- A string that describes the name of a sibling quantity with an integer type, e.g. `['number_of_atoms', 3]`

### Unit

NOMAD manages units and data with units via the [Pint](https://pint.readthedocs.io/en/stable/){:target="_blank" rel="noopener"} Python package. A unit is given as a string that is parsed by pint. These strings can
be simple units (or their aliases) or complex expressions. Here are a few examples:
`m`, `meter`, `mm`, `millimeter`, `m/s`, `m/s**2`.

While you can use all kinds of units in your uploaded schema packages, the built-in NOMAD schema (Metainfo) uses only SI units.

## Subsections

*Subsections* define a *part-of-relationship* between two *sections*. *Subsection definitions* are *properties* of the parent *section definition* and name a child
*section definition*. In the data, we can now contain instances of the target (e.g. `Element`) in instances of the source (e.g. `Composition`). A *subsection* can be
defined as *repeating* to allow many child *sections* of the same *type*. In our example,
one `Composition` can contain many `Elements`.

The *names* of *subsection definitions* serve as the *key*, used in respective *section objects*.

## Uploading schema packages

NOMAD archive files allow you to upload data in NOMAD's native file format. An archive
file can be a .yaml or .json file. It ends with `.archive.json` or `.archive.yaml`.
Archive files are mainly used to convey data. Since YAML schema packages are also "just" data, archive
files can also be used to convey a schema package.

You can upload schema packages and data in separate files.
`schema_package.archive.yaml`

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
    Composition:
      quantities:
        composition:
          type: str
      sub_sections:
        elements:
          section: Element
          repeats: true
```

and `data.archive.yaml`

```yaml
data:
  m_def: '../upload/raw/package.archive.yaml#Composition'
  composition: 'H2O'
  elements:
    - label: H
      density: 0.00008375
      isotopes: [1, 2, 3]
    - label: O
      density: 1.141
      isotopes: [16, 17, 18]
```

Or, you can upload the schema package and data in the same file:

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
    Composition:
      quantities:
        composition:
          type: str
      sub_sections:
        elements:
          section: Element
          repeats: true

data:
  m_def: Composition
  composition: H2O
  elements:
  - label: H
    density: 8.375e-05
    isotopes: [1, 2, 3]
  - label: O
    density: 1.141
    isotopes: [16, 17, 18]
```

## References

Sections can also be linked to each other with *references*, instead of being nested with
subsections. References work across entries and uploads, and are covered on their own page:
{{ nav_link("howto/schemas/references.md", breadcrumb=True) }}.

## Base sections and inheritance

Section definitions can inherit from more abstract ones with `base_section`, and subsections can
hold any specialization of the section they declare. See
{{ nav_link("howto/schemas/base_sections.md", breadcrumb=True) }}.

### Pre-defined sections

NOMAD provides a series of built-in *section definitions*. For example, there is `EntryArchive`, a definition for the top-level object in all NOMAD archives (e.g. `.archive.yaml` files). Here is a simplified except of the *main* NOMAD schema `nomad.datamodel`:

```yaml
EntryArchive:
  sub_sections:
    metadata:
      section: EntryMetadata
    definitions:
      section: nomad.metainfo.Package
    data:
      section: EntryData
    # ... many more
EntryData:
  # empty
```

Compare this to the previous examples: we used the top-level *keys* `definitions`
and `data` without really explaining why. Here you can see why. The `EntryArchive` *property* `definitions` allows us to put a *schema package* into our archives. And the `EntryArchive` *property* `data` allows us to put *data* into archives that is a *specialization* of `Schema`. The `Schema` definition is empty. It is merely an *abstract* placeholder that allows you to add *specialized* data sections to your archive. Therefore, all *section definitions* that define a top-level data section, should correctly use `nomad.datamodel.Schema` as a base section. This would be the first "correct" example:

```yaml
definitions:
  sections:
    Greetings:
      base_section: nomad.datamodel.EntryData
      quantities:
        message:
          type: str
data:
  m_def: Greetings
  message: Hello World
```

For the list of built-in base sections you are most likely to inherit from, see
{{ nav_link("howto/schemas/base_sections.md", breadcrumb=True) }}. To link quantities to HDF5
datasets for large data, see {{ nav_link("howto/plugins/tools/hdf5.md", breadcrumb=True) }}.

## Separating data and schema package

As we saw above, a NOMAD entry can contain schema package `definitions` and `data` at the
same time. To organize your schema package and data efficiently, it is often necessary to re-use
schema packages and certain data in other entries. You can use *references* to spread your
schema packages and data over multiple entries and connect the pieces via *references*.

Here is a simple schema package, stored in a NOMAD entry with mainfile name `package.archive.yaml`:

```yaml
 definitions:
  sections:
    Composition:
      quantities:
        composition:
          type: str
        base_composition:
          type: Composition
      sub_sections:
        elements:
          section: Element
          repeats: True
    Element:
      quantities:
        label:
          type: str
    Solution:
      quantities:
        solvent:
          type: Composition
      sub_sections:
        solute:
          section: Composition
```

Now, we can re-use this schema package in many entries via *references*. Here, we extend
a schema contained in the package and instantiate definitions is a separate mainfile `data-and-package.archive.yaml`:

```yaml
 definitions:
  sections:
    SpecialElement:
      # Extending the definition from another entry
      base_section: '../upload/raw/package.archive.yaml#Element'
      quantities:
        atomic_weight:
          type: float
          unit: 'g/mol'
data:
  # Instantiating the definition from another entry
  m_def: '../upload/raw/package.archive.yaml#Composition'
  composition: 'H2O'
  elements:
    # Implicitly instantiate Element as defined for Composition.elements
    - label: H
    # Explicitly instantiate SpecialElement as a polymorph substitute
    - m_def: SpecialElement
      label: O
      atomic_weight: 15.9994
```

Here is a last example that re-uses the schema and references data from the two entries
above:

```yaml
definitions:
  sections:
    Composition:
      quantities:
        composition:
          type: str
        base_composition:
          type: Composition
      sub_sections:
        elements:
          section: Element
          repeats: True
    Element:
      quantities:
        label:
          type: str
    Solution:
      quantities:
        solvent:
          type: Composition
      sub_sections:
        solute:
          section: Composition
```

!!! warning "Attention"
    You cannot create definitions that lead to circular loading of `*.archive.yaml` files.
    Each `definitions` section in an NOMAD entry represents a *schema package*. Each *schema package* needs to be fully loaded and analyzed before it can be used by other *schema packages* in other entries. Therefore, two *schema packages* in two entries cannot reference each other.

## Related materials

- {{ nav_link("reference/metainfo.md", breadcrumb=True) }} — quantity types, attributes and naming conventions.
- {{ nav_link("howto/schemas/annotations.md", breadcrumb=True) }} — make a schema editable in the GUI.
- {{ nav_link("howto/schemas/python.md", breadcrumb=True) }} — the same concepts in Python.
- {{ nav_link("tutorial/eln/custom_eln_yaml.md", breadcrumb=True) }} — a guided walkthrough.
