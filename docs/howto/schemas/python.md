# How to write a Python schema package

A Python schema package is a `nomad.metainfo.SchemaPackage` containing section definitions written as
Python classes. Compared to [YAML schemas](./yaml.md), Python schemas can define custom `normalize`
functions, are distributed as a plugin to every installation that installs it, and can be tested and
version controlled alongside code.

This page shows how to write the definitions themselves. To package them so NOMAD loads them, see
[How-to guides > Develop plugins > Schema packages](../plugins/types/schema_packages.md).

## Define a schema package

All definitions must be placed between the `SchemaPackage()` constructor call and the
`__init_metainfo__()` initialization. Put them in their own module, e.g.
`*/schema_packages/mypackage.py`:

```python
import ase

from nomad.datamodel.data import Schema
from nomad.metainfo import MEnum, MSection, Quantity, SchemaPackage, SubSection

m_package = SchemaPackage()


class System(MSection):
    """
    A system section includes all quantities that describe a single simulated
    system (a.k.a. geometry).
    """

    n_atoms = Quantity(
        type=int,
        description="""
        Defines the number of atoms in the system.
        """,
    )

    atom_labels = Quantity(type=MEnum(ase.data.chemical_symbols), shape=['n_atoms'])
    atom_positions = Quantity(type=float, shape=['n_atoms', 3], unit='angstrom')
    simulation_cell = Quantity(type=float, shape=[3, 3], unit='angstrom')
    pbc = Quantity(type=bool, shape=[3])


class Simulation(Schema):
    system = SubSection(sub_section=System, repeats=True)


m_package.__init_metainfo__()
```

This defines two *sections*. `System` inherits from `MSection`, the most primitive section type.
`Simulation` inherits from `Schema`, which makes it usable as the root section of an entry. Use
`ArchiveSection` instead of `MSection` for any section that needs a `normalize` function.

## Add quantities

Each *quantity* defines a single piece of data. The attributes you will use most often are:

- `type` — a Python type (`str`, `int`, `bool`), a NumPy type (`np.float64`), an
  `MEnum('item1', ..., 'itemN')`, a predefined Metainfo type (`Datetime`, `JSON`, `File`, ...), or
  another section to define a reference.
- `shape` — the dimensionality: `[]` for a scalar, `['*']` for a list, `[3, 3]` for a 3-by-3 matrix,
  `['n_elements']` for a vector whose length is given by another quantity.
- `unit` — a physical unit string parsed by Pint, e.g. `meter`, `m`, `m/s**2`. The built-in NOMAD
  Metainfo uses SI units only.
- `description` — what the quantity means. This is shown in the GUI and the Metainfo browser.

For the complete list of attributes, the full type table and the naming conventions, see
{{ nav_link("reference/metainfo.md", breadcrumb=True) }}.

## Add subsections

A *subsection* nests one section inside another, forming a containment hierarchy:

- `sub_section` (aliases `section_def`, `sub_section_def`) — the section definition being contained.
- `repeats` — whether the subsection may occur once or many times.

Prefer subsections over inheritance when you want to add a specific group of quantities to a more
general section.

## Create and populate instances

Section instances behave like ordinary Python objects — quantities and subsections are set and read
as attributes:

```python
simulation = Simulation()
system = System()
system.n_atoms = 3
system.atom_labels = ['H', 'H', 'O']
simulation.system.append(system)
```

Values are converted to the declared type and unit on assignment. Methods starting with `m_` provide
the more complex semantics: `m_create` instantiates a subsection and attaches it to its parent in one
step, and `m_to_json` serializes a section:

```python
simulation.m_to_json(indent=2)
```

```json
{
  "system": [
    {
      "n_atoms": 3,
      "atom_labels": [
        "H",
        "H",
        "O"
      ]
    }
  ]
}
```

For setting and reading properties by name at runtime, see
[Advanced schema concepts](./advanced.md#populate-data-dynamically).

## Add normalize functions

A `normalize` function runs whenever an instance of its section is processed, which happens every
time a file is uploaded or changed. This is the main capability that YAML schemas do not have. The
section must inherit from `Schema` or `ArchiveSection`:

<!-- fmt: off -->
```python
--8<-- "examples/archive/custom_schema.py"
```
<!-- fmt: on -->

Always call the `super` implementation so that multiple inheritance keeps working.

Normalize functions are called for every subsection before their parent section. To control the order
among sections at the same level, set `normalizer_level` — it defaults to `0`, and sections are
processed from low values to high.

Given an archive like this:

```yaml
--8<-- "examples/archive/custom_data.archive.yaml"
```

the normalized archive contains the derived `sample_id`:

```json
{
  "data": {
    "m_def": "examples.archive.custom_schema.SampleDatabase",
    "samples": [
      {
        "added_date": "2022-06-18T00:00:00+00:00",
        "formula": "NaCl",
        "sample_id": "2022-06-18 00:00:00+00:00--NaCl"
      }
    ]
  }
}
```

Design normalize functions so that they only need information contained in their own section. Avoid
modifying data outside of the section being normalized — use `m_parent` and `m_root` to *read* from
the surrounding archive when you must.

!!! note
    A `normalize` function is not the same thing as a *normalizer*. A normalizer is a separate plugin
    entry point that operates on the whole entry. See
    {{ nav_link("howto/plugins/types/normalizers.md", breadcrumb=True) }} and
    {{ nav_link("explanation/basics.md", breadcrumb=True) }}.

## Related materials

- {{ nav_link("howto/schemas/base_sections.md", breadcrumb=True) }} — reuse and extend existing definitions.
- {{ nav_link("howto/schemas/references.md", breadcrumb=True) }} — link sections to each other.
- {{ nav_link("howto/plugins/tools/units.md", breadcrumb=True) }} — work with physical units.
- {{ nav_link("howto/plugins/tools/hdf5.md", breadcrumb=True) }} — store large arrays efficiently.
- {{ nav_link("tutorial/develop_plugin/create_schema_package.md", breadcrumb=True) }} — a guided walkthrough.
