# How to write a schema package

Schema packages are used to define and distribute custom data definitions that can be used within NOMAD. These schema packages typically contain [schemas](../../reference/glossary.md#schema) that users can select to instantiate manually filled entries using our ELN functionality, or that parsers when organizing data they extract from files. Schema packages may also contain more abstract base classes that other schema packages use.

This documentation shows you how to write a plugin entry point for a schema package. You should read the [documentation on getting started with plugins](./plugins.md) to have a basic understanding of how plugins and plugin entry points work in the NOMAD ecosystem.

## Getting started

You can use our [template repository](https://github.com/FAIRmat-NFDI/nomad-plugin-template) to create an initial structure for a plugin containing a schema package. The relevant part of the repository layout will look something like this:

```txt
nomad-example
   ├── src
   │   ├── nomad_example
   │   │   ├── schema_packages
   │   │   │   ├── __init__.py
   │   │   │   ├── mypackage.py
   ├── LICENSE.txt
   ├── README.md
   └── pyproject.toml
```

See the documentation on [plugin development guidelines](./plugins.md#plugin-development-guidelines) for more details on the best development practices for plugins, including linting, testing and documenting.

## Schema package entry point

The entry point defines basic information about your schema package and is used to automatically load it into a NOMAD distribution. It is an instance of a `SchemaPackageEntryPoint` or its subclass and it contains a `load` method which returns a `nomad.metainfo.SchemaPackage` instance that contains section and schema definitions. You will learn more about the `SchemaPackage` class in the next sections. The entry point should be defined in `*/schema_packages/__init__.py` like this:

```python
from pydantic import Field
from nomad.config.models.plugins import SchemaPackageEntryPoint


class MySchemaPackageEntryPoint(SchemaPackageEntryPoint):

    def load(self):
        from nomad_example.schema_packages.mypackage import m_package

        return m_package


mypackage = MySchemaPackageEntryPoint(
    name = 'MyPackage',
    description = 'My custom schema package.',
)
```

Here you can see that a new subclass of `SchemaPackageEntryPoint` was defined. In this new class you can override the `load` method to determine how the `SchemaPackage` class is loaded, but you can also extend the `SchemaPackageEntryPoint` model to add new configurable parameters for this schema package as explained [here](./plugins.md#plugin-configuration).

We also instantiate an object `mypackage` from the new subclass. This is the final entry point instance in which you specify the default parameterization and other details about the schema package. In the reference you can see all of the available [configuration options for a `SchemaPackageEntryPoint`](../../reference/plugins.md#schemapackageentrypoint).

The entry point instance should then be added to the `[project.entry-points.'nomad.plugin']` table in `pyproject.toml` in order for it to be automatically detected:

```toml
[project.entry-points.'nomad.plugin']
mypackage = "nomad_example.schema_packages:mypackage"
```

## `SchemaPackage` class

The `load`-method of a schema package entry point returns an instance of a `nomad.metainfo.SchemaPackage` class. This definition should be contained in a separate file (e.g. `*/schema_packages/mypackage.py`) and could look like this:

```python
from nomad.datamodel.data import Schema
from nomad.datamodel.metainfo.annotations import ELNAnnotation, ELNComponentEnum
from nomad.metainfo import SchemaPackage, Quantity, MSection

m_package = SchemaPackage()


class System(MSection):
    '''
    A system section includes all quantities that describe a single simulated
    system (a.k.a. geometry).
    '''

    n_atoms = Quantity(
        type=int, description='''
        Defines the number of atoms in the system.
        ''')

    atom_labels = Quantity(
        type=MEnum(ase.data.chemical_symbols), shape['n_atoms'])
    atom_positions = Quantity(type=float, shape=['n_atoms', 3], unit='angstrom')
    simulation_cell = Quantity(type=float, shape=[3, 3], unit='angstrom')
    pbc = Quantity(type=bool, shape=[3])


class Simulation(Schema):
    system = SubSection(sub_section=System, repeats=True)

m_package.__init_metainfo__()
```

Schema packages typically contain one or several [schema](../../reference/glossary.md#schema) definitions, that can the be used to manually create new entries through the ELN functionality, or also by parsers to create instances of this schema fully automatically. All of the definitions contained in the package should be placed between the contructor call (`m_package = SchemaPackage()`) and the initialization (`m_package.__init_metainfo__()`).

In this basic example we defined two _sections_: `System` and `Simulation`. `System` inherits from most primitive type of section - `MSection` - whereas `Simulation` is defined as a subclass of `Schema` which makes it possible to use this as the root section of an entry. Each section can have two types of properties: _quantities_ and _subsections_. Sections and their properties are defined with Python classes and their attributes. Each _quantity_ defines a piece of data. Basic quantity attributes are `type`, `shape`, `unit`, and `description`.

_Subsections_ allow the placement of sections within each other, forming containment hierarchies. Basic subsection attributes are `sub_section`&mdash;a reference to the section definition of the subsection&mdash;and `repeats`&mdash;determines whether a subsection can be included once or multiple times.

To use the above-defined schema and create actual data, we have to instantiate the classes:

```python
run = Run()
system = run.m_create(System)
system.n_atoms = 3
system.atom_labels = ['H', 'H', 'O']

print(system.atom_labels)
print(n_atoms = 3)
```

Section _instances_ can be used like regular Python objects: quantities and subsections
can be set and accessed like any other Python attribute. Special metainfo methods, starting
with `m_` allow us to realize more complex semantics. For example `m_create` will
instantiate a subsection and add it to the _parent_ section in one step.

<!-- ? m_create is deprecated? -->

Another example for an `m_`-method is:

```python
run.m_to_json(indent=2)
```

This will convert the data into JSON:

```json
{
    "m_def" = "Run",
    "systems": [
        {
            "n_atoms" = 3,
            "atom_labels" = [
                "H",
                "H",
                "O"
            ]
        }
    ]
}
```

## Schema packages: Python vs. YAML

In this [guide](../customization/basics.md), we explain how to write and upload schema packages in the `.archive.yaml` format. Writing and uploading such YAML schema packages is a good way for NOMAD users to start exploring schemas, but it has limitations. As a NOMAD developer or Oasis administrator you can add Python schema packages to NOMAD. All built-in NOMAD schemas (e.g. for electronic structure code data) are written in Python and are part of the NOMAD sources (`nomad.datamodel.metainfo.*`).

There is a 1-1 translation between the structure in Python schema packages (written in classes) and YAML (or JSON) schema packages (written in objects). Both use the same fundamental concepts, like _section_, _quantity_, or _subsection_, introduced in [YAML schemas](../customization/basics.md). The main benefit of Python schema packages is the ability to define custom `normalize`-functions.

`normalize`-functions are attached to sections and are are called when instances of these sections are processed. All files are processed when they are uploaded or changed. To add a `normalize` function, your section has to inherit from `Schema` or `ArchiveSection` which provides the base for this functionality. Here is an example:

```python
--8<-- "examples/archive/custom_schema.py"
```

Make sure to call the `super` implementation properly to support multiple inheritance. In order to control the order by which the `normalize` calls are executed, one can define `normalizer_level` which is set to 0 by default. The normalize functions are always called for any sub section before the parent section. However, the order for any sections on the same level will be from low values of `normalizer_level` to high.

If we parse an archive like this:

```yaml
--8<-- "examples/archive/custom_data.archive.yaml"
```

we will get a final normalized archive that contains our data like this:

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

## Migration guide

By default, schema packages are identified by the full qualified path to the Python module that contains the definitions. An example of a full qualified path could be `nomad_example.schema_packages.mypackage`, where the first part is the Python package name, second part is a subpackage, and the last part is a Python module containing the definitions. This is the easiest way to prevent conflicts between different schema packages: python package names are unique (prevents clashes between packages) and paths inside a package must point to a single python module (prevents clashes within package). This does, however, mean that _if you move your schema definition in the plugin source code, any references to the old definition will break_. This becomes problematic in installations that have lot of old data processed with the old definition location, as those entries will still refer to the old location and will not work correctly.

As it might not be possible, or even wise to prevent changes in the source code layout, and reprocessing all old entries might be impractical, we do provide an alias mechanism to help with migration tasks. Imagine your schema package was contained in `nomad_example.schema_packages.mypackage`, and in a newer version of your plugin you want to move it to `nomad_example.schema_packages.mynewpackage`. The way to do this without completely breaking the old entries is to add an alias in the schema package definition:

```python
m_package = SchemaPackage(aliases=['nomad_example.schema_packages.mypackage'])
```

Note that this will only help in scenarious where you have moved the definition and not removed or modified any of them.

## Definitions

The following describes in detail the schema language for the NOMAD Metainfo and how it is expressed in Python.

### Common attributes of Metainfo Definitions

In the example, you have already seen the basic Python interface to the Metainfo. _Sections_ are
represented in Python as objects. To define a section, you write a Python class that inherits
from `MSection`. To define subsections and quantities you use Python properties. The
definitions themselves are also objects derived from classes. For subsections and
quantities, you directly instantiate `:class:SubSection` and `:class:Quantity`. For sections
there is a generated object derived from `:class:Section` and available via
`m_def` from each _section class_ and _section instance_.

<!-- TODO Either fix all cross references with :: syntax here and throughout or remove them -->

These Python classes, used to represent metainfo definitions, form an inheritance
hierarchy to share common properties

- `name`: each definition has a name. This is typically defined by the corresponding
  Python property. For example, a section class name becomes the section name; a quantity gets the name
  from the variable name used in its Python definition, etc.
- `description`: each definition should have one. Either set it directly or use _doc strings_
- `links`: a list of useful internet references.
- `more`: a dictionary of custom information. Any additional `kwargs` set when creating a definition
  are added to `more`.

### Sections

Sections are defined with Python classes that extend `MSection` (or other section classes).

- `base_sections`: automatically taken from the base classes of the Python class.
- `extends_base_section`: a boolean that determines the inheritance. If this is `False`,
  normal Python inheritance implies and this section will inherit all properties (subsections,
  quantities) from all base classes. If `True`, all definitions in this section
  will be added to the properties of the base class section. This allows the extension of existing
  sections with additional properties.

### Quantities

Quantity definitions are the main building block of metainfo schemas. Each quantity
represents a single piece of data. Quantities can be defined with the following attributes:

- `type`: can be a primitive Python type (`str`, `int`, `bool`), a numpy
  data type (`np.dtype('float64')`), an `MEnum('item1', ..., 'itemN')`, a predefined
  metainfo type (`Datetime`, `JSON`, `File`, ...), or another section or quantity to define
  a reference type.
- `shape`: defines the dimensionality of the quantity. Examples are: `[]` (number),
  `['*']` (list), `[3, 3]` (3 by 3 matrix), `['n_elements']` (a vector of length defined by
  another quantity `n_elements`).
- `unit`: a physical unit. We use [Pint](https://pint.readthedocs.io/en/stable/){:target="\_blank"} here. You can
  use unit strings that are parsed by Pint, e.g. `meter`, `m`, `m/s^2`. As a convention the
  NOMAD Metainfo uses only SI units.

### SubSection

A subsection defines a named property of a section that refers to another section. It
allows to define that a section that contains another section.

- `sub_section`: (aliases `section_def`, `sub_section_def`) defines the section that can
  be contained.
- `repeats`: a boolean that determines whether the subsection relationship allows multiple sections
  or only one.

### References and Proxies

Besides creating hierarchies with subsections (e.g. tree structures), the metainfo
also allows one to create a reference within a section that points to either another section or a quantity
value:

```python
class Calculation(MSection):
    system = Quantity(type=System.m_def)
    atom_labels = Quantity(type=System.atom_labels)

calc = Calculation()
calc.system = run.systems[-1]
calc.atom_labels = run.systems[-1]
```

To define a reference, define a normal quantity and simply use the section or quantity
you want to refer to as type. Then you can assign respective section instances
as values.

In Python memory, quantity values that reference other sections simply contain a
Python reference to the respective _section instance_. However, upon serializing/storing
metainfo data, these references have to be represented differently.

Value references work a little differently. When you read a value reference, it behaves like
the reference value. Internally, we do not store the values, but instead a reference to the
section that holds the referenced quantity is stored. Therefore, when you want to
assign a value reference, use the section with the quantity and not the value itself.

<!-- TODO Add a simply example here -->

References are serialized as URLs. There are different types of reference URLs:

- `#/run/0/calculation/1`: a reference in the same Archive
- `/run/0/calculation/1`: a reference in the same archive (legacy version)
- `../upload/archive/mainfile/{mainfile}#/run/0`: a reference into an Archive of the same upload
- `/entries/{entry_id}/archive#/run/0/calculation/1`: a reference into the Archive of a different entry on the same NOMAD installation
- `/uploads/{upload_id}/archive/{entry_id}#/run/0/calculation/1`: similar to the previous one but based on uploads
- `https://myoasis.de/api/v1/uploads/{upload_id}/archive/{entry_id}#/run/0/calculation/1`: a global reference towards a different NOMAD installation (Oasis)

The host and path parts of URLs correspond with the [NOMAD API](../programmatic/api.md). The anchors are paths from the root section of an Archive, over its subsections, to the referenced section or quantity value. Each path segment is the name of the subsection or an index in a repeatable subsection: `/system/0` or `/system/0/atom_labels`.

References are automatically serialized by `:py:meth:MSection.m_to_dict`. When de-serializing
data with `:py:meth:MSection.m_from_dict` these references are not resolved right away,
because the reference section might not yet be available. Instead references are stored
as `:class:MProxy` instances. These objects are automatically replaced by the referenced
object when a respective quantity is accessed.

If you want to define references, it might not be possible to define the referenced
section or quantity beforehand, due to the way Python definitions and imports work. In these
cases, you can use a proxy to reference the reference type. There is a special proxy
implementation for sections:

```python
class Calculation(MSection):
    system = Quantity(type=SectionProxy('System')
```

The strings given to `SectionProxy` are paths within the available definitions.
The above example works, if `System` is eventually defined in the same package.

### Categories

!!! Warning

    Categories are now deprecated.
    Their previous occurrences should be replaced
    with respective annotations.

In the old metainfo this was known as _abstract types_.

Categories are defined with Python classes that have `:class:MCategory` as base class.
Their name and description are taken from the name and docstring of the class. An example
category looks like this:

```python
class CategoryName(MCategory):
    ''' Category description '''
    m_def = Category(links=['http://further.explanation.eu'], categories=[ParentCategory])
```

## Data frames

On top of the core Metainfo concepts like `Sections`, `Quantities`, and `SubSection`, we provide a mechanism for modeling _data frames_.

A NOMAD data frame is a multi-index table with named indices (variables) and columns (fields).
All columns should match in length, as they are all parametrized by the same indices.
Both variables and fields are defined standalone using Values.
A DataFrame may contain any number of Values, though a bare minimum can be defined via the `mandatory_variables` and `mandatory_fields` respectively.

The mechanism is based on a concept called `Values` for storing arrays of numeric data to
represent a _field_ or _variable_ (or axis, dimension, etc.) and a concept called
`DataFrame` that combines _fields_ and _variables_ with matching dimensions into a data frame.
Our `DataFrame` is conceptually close to xarray datasets, pandas data frames, or the NeXus NXData group.

`Values` and `DataFrame` are usually not used directly, instead you will create
re-usable templates that allow you to use the same type of `Values` (e.g. describing
physical properties like energies, temperatures, pressures, ...) and the same type of `DataFrame` (e.g.
describing material properties at different variables like density of states or band gap).

### Illustrating example

```py
--8<-- "examples/metainfo/data_frames.py:9:31"

--8<-- "examples/metainfo/data_frames.py:41:44"


--8<-- "examples/metainfo/data_frames.py:55:63"

```

### Fields vs variables (and dimensions)

Both _fields_ and _variables_ hold values (i.e. columns) in your data frame.
While _fields_ hold the actual data, _variables_ span the data space and its dimensions (i.e. column indices).

_Variables_ and _dimensions_ are conceptually slightly different. First, _variables_ provide
the values on a certain dimension (via shared indices). Second, the number of _Variables_ often, but not necessarily,
are equal to the number of dimensions. If some _variables_ depend on each other, they might
span shared dimensions. _Fields_ on the other hand always provide values for all dimensions.

Let's compare two datasets; one dataset that you could plot in a heatmap and one that
you would plot in a scatter plot. In both cases, we have two _variables_ `Temperature` and `Pressure`,
as well as one _field_ `Energy`.

In the heatmap scenario, we vary `Temperature` and `Pressure` independently and have a
`Energy` value (i.e. heatmap color/intensity) for each `Temperature` reading at every `Pressure` reading.
For two values on each _variable_, we respectively we have 4 (2x2) _field_ values:

```py
--8<-- "examples/metainfo/data_frames.py:89:97"
```

In the scatter plot scenario, we vary `Temperature` and `Pressure` together.
We only have one _field_ value (y-axis) for each pair of temperature and pressure (two x-axes)
values.
With two combined temperature and pressure readings, we respectively only have two field values:

```py
--8<-- "examples/metainfo/data_frames.py:100:106"
```

We can use the `ValueTemplate` kwarg `spanned_dimenions` to define how `Temperature` and
`Pressure` are related. The given indices refer to the indices of the field values and
represent the logical dimension of the data space.

The first example without the `spanned_dimensions` is equivalent to this example
with `spanned_dimensions`. Here we span two independent dimensions:

```py
--8<-- "examples/metainfo/data_frames.py:109:117"
```

### Field and variables in the schema vs parsing

The templates allow you to define _mandatory_ _fields_ and _variables_ in the schema.
These _fields_ and _variables_ have to be provided by the parser when instantiating the
respective dataset. However, parser can provide additional _fields_ and _variables_.
This allows to extend what is defined in the template without requiering new definitions.

### Data representation

Each call to `ValueTemplate` and `DatasetTemplate` produces a section definition
inheriting from `Values` and `DataFrame` respectively.

`Values` sections define a single quantity `values`. The `values` quantity always holds a numpy array
based on the type and shape given in the template. The shape of the `values` quantity
is the shape given in the template plus one dimension of arbitrary length.
_Variable_ values are always a flat list of values anyways (the values themselves can have a higher shape).
_Field_ values are always flattened. You might provide them in a higher dimensional array
according to the dimensionality of the _Variables_, but they are always flattened as the
`value` quantity only provides one additional dimension, because the real number of dimensions
is only available at runtime. The original (runtime) shape of _fields_ is stored int the `original_shape` `Values` quantity.

`DataFrame` sections define repeating sub-sections for `fields` and `variables`.
The specific `DataFrame` section defined by the template, will also hold an annotation `DatasetAnnotation` that keeps the `mandatory_fields` and `mandatory_variables` for runtime validation.
The `fields` and `variables` sub-sections provide a `Values`
instances for each _field_ in `mandatory_fields` and each _variable_ in `mandatory_variables`,
but they can also hold additional _fields_ and _variables_ to accommodate more
_fields_ and _variables_ determined during parsing.

When a `ValuesTemplate` is used (e.g. `some_property = Energy()`), a quantity is created.
This quantity is a copy of the `values` quantity created by the template.
This allows to reuse templated value quantities. When a `DatasetTemplate` is used
(e.g. `some_property = BandGap()`), a sub-section is created. This sub-section targets
the `DataFrame` section defined by the template.

#### Working with xarrays and pandas

We provide utility function on `DataFrame` that you can use to translate into
respective xarray datasets and pandas data frames.

!!! Warning

    The documentation on this is still pending.

## Adding Python schemas to NOMAD

The following describes how to integrate new schema modules into the existing code according
to best practices.

### Schema super structure

You should follow the basic [developer's getting started](../develop/setup.md) to setup a development environment. This will give you all the necessary libraries and allows you
to place your modules into the NOMAD code.

The `EntryArchive` section definition sets the root of the archive for each entry in
NOMAD. It therefore defines the top level sections:

- `metadata`: all "administrative" metadata (ids, permissions, publish state, uploads, user metadata, etc.)
- `results`: a summary with copies and references to data from method specific sections. This also
  presents the [searchable metadata](../develop/search.md).
- `workflows`: all workflow metadata
- Method-specific subsections: e.g. `run`. This is were all parsers are supposed to
add the parsed data.
<!-- TODO Update!!! -->

The main NOMAD Python project includes Metainfo definitions in the following modules:

- `nomad.metainfo`: defines the Metainfo itself. This includes a self-referencing schema. E.g. there is a section `Section`, etc.
- `nomad.datamodel`: defines the section `metadata` that contains all "administrative"
  metadata. It also contains the root section `EntryArchive`.
- `nomad.datamodel.metainfo`: defines all the central, method specific (but not parser specific) definitions.
  For example the section `run` with all the simulation definitions (computational material science definitions)
  that are shared among the respective parsers.

### Extending existing sections

Parsers can provide their own definitions. By convention, these are placed into a
`metainfo` sub-module of the parser Python module. The definitions here can add properties
to existing sections (e.g. from `nomad.datamodel.metainfo`). By convention, use a `x_mycode_`
prefix. This is done with the
`extends_base_section` [Section property](#sections). Here is an example:

<!-- ? Do we want to encourage this as best practice in the future? -->

```py
from nomad.metainfo import Section
from nomad.datamodel.metainfo.workflow import Workflow

class MyCodeRun(Workflow)
    m_def = Section(extends_base_section=True)
    x_mycode_execution_mode = Quantity(
        type=MEnum('hpc', 'parallel', 'single'), description='...')
```

### Schema conventions

- Use lower snake case for section properties; use upper camel case for section definitions.
- Use a `_ref` suffix for references.
- Use subsections rather than inheritance to add specific quantities to a general section.
  E.g. the section `workflow` contains a section `geometry_optimization` for all geometry optimization specific
  workflow quantities.
- Prefix parser-specific and user-defined definitions with `x_name_`, where `name` is the
short handle of a code name or other special method prefix.
<!-- TODO add case examples to the reference pages and add corresponding links here and throughout -->

## Use Python schemas to work with data

### Access structured data via API

The [API section](../programmatic/api.md#access-processed-data-archives) demonstrates how to access an Archive, i.e.
retrieve the processed data from a NOMAD entry. This API will give you JSON data likes this:

```json title="https://nomad-lab.eu/prod/v1/api/v1/entries/--dLZstNvL_x05wDg2djQmlU_oKn/archive"
{
    "run": [
        {
            "program": {...},
            "method": [...],
            "system": [
                {...},
                {...},
                {...},
                {...},
                {
                    "type": "bulk",
                    "configuration_raw_gid": "-ZnDK8gT9P3_xtArfKlCrDOt9gba",
                    "is_representative": true,
                    "chemical_composition": "KKKGaGaGaGaGaGaGaGaGa",
                    "chemical_composition_hill": "Ga9K3",
                    "chemical_composition_reduced": "K3Ga9",
                    "atoms": {...},
                    "springer_material": [...],
                    "symmetry": [...]
                }
            ]
            "calculation": [...],
        }
    ],
    "workflow": [...],
    "metadata": {...},
    "results":{
        "material": {...},
        "method": {...},
        "properties": {...},
    }
}
```

This will show you the Archive as a hierarchy of JSON objects (each object is a section),
where each key is a property (e.g. a quantity or subsection). Of course you can use
this data in this JSON form. You can expect that the same keys (each item has a formal
definition) always provides the same type of data. However, not all keys are present in
every archive, and not all lists might have the same number of objects. This depends on the
data. For example, some _runs_ contain many systems (e.g. geometry optimizations), others
don't; typically _bulk_ systems will have _symmetry_ data, non bulk systems might not.
To learn what each key means, you need to look up its definition in the Metainfo.

{{ metainfo_data() }}

### Wrap data with Python schema classes

In Python, JSON data is typically represented as nested combinations of dictionaries
and lists. Of course, you could work with this right away. To make it easier for Python
programmers, the [NOMAD Python package](../programmatic/pythonlib.md) allows you to use this
JSON data with a higher level interface, which provides the following advantages:

- code completion in dynamic coding environments like Jupyter notebooks
- a cleaner syntax that uses attributes instead of dictionary access
- all higher dimensional numerical data is represented as numpy arrays
- allows to navigate through references
- numerical data has a Pint unit attached to it

For each section the Python package contains a Python class that corresponds to its
definition in the metainfo. You can use these classes to access `json_data` downloaded
via API:

```python
from nomad.datamodel import EntryArchive

archive = EntryArchive.m_from_dict(json_data)
calc = archive.run[0].calculation[-1]
total_energy_in_ev = calc.energy.total.value.to(units.eV).m
formula = calc.system_ref.chemical_formula_reduced
```

Archive data can also be serialized into JSON again:

```python
import json

print(json.dumps(calc.m_to_dict(), indent=2))
```

### Access structured data via the NOMAD Python package

The NOMAD Python package provides utilities to [query large amounts of
archive data](../programmatic/archive_query.md). This uses the built-in Python schema classes as
an interface to the data.

## Versioning

Eventually you will change a schema.
While we might think about schemas before and after a change as version 1 and
version 2 of the same schema, those are technically two different schemas.
We replace an existing schema for existing data with a new schema. The intention is
that the new schema also describes the existing data.
But, whether this is always the case depends on the type of changes we make and some changes
will "break" existing data.

What does it mean to "break an entry"? Either, your `*.archive.[json|yaml]`
raw files cannot be parsed anymore, or processed data (i.e. "archive" data) can not be opened
anymore. In both cases, NOMAD tries to convert JSON-style data into section definition
instances, validating the data against the current schema. If items in the data do not match
a given definitions this process will throw errors.

If every potential section instance that _followed_ a section definition in the old schema
still _follows_ the _same_ section definition in the new schema, we can safely replace the
schema. If not, we will need to _migrate_ data to implement the logical transition
we intended. Otherwise, we will _break_ existing data.

### Save changes and unsafe changes

Generally, _adding_ to a schema is safe. Adding section definition, adding new quantities,
new sub-sections. All existing data only uses definitions that still exist.

_Removing_ is generally not safe. Removing a quantity, makes NOMAD ignore values in existing
entries. Removing section definitions, "breaks" entries.

_Changing_ a definition might or might not be safe. In many cases _changing_ is like _removing_ and _adding_ something. Some examples:

- Names determine the identity of definitions and name changes are therefore literally _removing_ and _adding_
  a definition. They are not safe, unless you add an `alias`.
- Adding `base_sections` is safe, removing is not. It is as if you _add_ and _remove_ properties.
- Hoisting a property from a section into a base section is safe (you only _add_ properties).
  The reverse is not safe (you _remove_ some properties from some definitions).
- Making the type of a sub-section more generic (you _add_ properties to the sub-section) is safe,
  making it more specific (you _remove_ properties from the sub-section) is not.
- Changing quantity `type`, `shape`, or sub section `repeats` is not safe.

There are some changes that do not "break" entries, but change their semantics. If you
change a `unit` for example. NOMAD will still be able to open entires, but you will
interpret the values wrong.

Changing annotations will not "break" entries, but might have similar effects to your
users when old entries might be treated unexpectedly in tools that use these annotations.
The GUI is probably the most important "tool" here. Changing the ELN annotations for example
might prohibit users to manipulate old data in the same way they used to do.

### Python module conventions

Eventually, you reach the point were "breaking" changes are unavoidable and you will
need to create a new major version of your schema.

First, you need to keep a schema version as long as there is data following that schema.
That means two versions have to exist at the same time.
Each section instance refers to a schema by its qualified python name that includes
the respective python module with the schema package.

Therefore, breaking changes should only be introduced in new schema packages. As a convention:

- schema packages cary their major version in the name, e.g. `nomad_example.schema_packages.my_package_v2`
- schema packages are maintained in version sub-modules, e.g. `nomad_example.schema_packages.my_package.v2`

!!! note

    By convention and assuming the inevitability of breaking changes, you should already start with a `v1` module when developing a new schema package.

Note that only the major version should result in separate python modules, i.e. schema packages.
Minor and patch versions should not introduce breaking changes by definition and the module
for the respective major version can be changed safely.

### Migration strategies

!!! warning

    This is preliminary information.

What are strategies to introduce "breaking" changes and migrate existing data to
the new version of the schema.

#### Schema package aliases

In scenarious where you have moved the definition to a new module and did not create
other breaking changes you can use schema package aliases.

By default, schema packages are identified by the full qualified path to the Python module
that contains the definitions. An example of a full qualified path could be
`nomad_example.schema_packages.mypackage`, where the first part is the Python package name,
second part is a subpackage, and the last part is a Python module containing the definitions.
This is the easiest way to prevent conflicts between different schema packages: python package
names are unique (prevents clashes between packages) and paths inside a package must point
to a single python module (prevents clashes within package). This does, however, mean that
_if you move your schema definition to a new (version) module, any references to the old definition will break_.
To move the same schema to a new module, e.g. `nomad_example.schema_packages.mypackage.v2`,
and still let existing entries use it with the old module name, you can use a schema package
alias:

You
schema package definition:

```python
m_package = SchemaPackage(aliases=['nomad_example.schema_packages.mypackage'])
```

!!! note

    This can also be used, if you need to move a schema package for other reasons,
    e.g. to move schemas from one plugin to another.

#### Offer migration functionality

!!! warning

    This appoach is still tested and we might provide more dedicated functionality
    in the future.

You will not want to maintain the old version indefinitely. Eventually, you deprecate
and even remove schema package versions from future plugin releases. Here, you should
offer functionality that lets users migrate their old data following the old version to
data following the new version.

##### Processed data

In cases where your schema is instantiated via parser, processed data (i.e. entry "archives"),
can be migrated by re-processing respective uploads with a new version of the parser
following the new schema. Users "just" have to be made aware and perform the reprocessing.

##### Raw files

In cases of `*.archive.json` raw files (i.e. you use NOMAD ELNs), the raw files themselves
have to change. This is harder to achieve as mainfile immutability is baked into NOMAD.
To apply the same parser-based strategy (see section before), you can add a normalize
function to the `EntryData` section definition(s) of the old schema version. This
normalize function

- performs a transformation, i.e. creates and instance of the new
  version from the given instance of the old version
- writes the `m_to_dict` of the new version back into the mainfile
- replaces the `data` section (old version instance) with the transformed (instance of the new version)

Here is some pseudo code:

```py

from ..v2 import MyData as MyDataV2

def normalize(self, archive, logger):
  transformed = MyDataV2()

  # code that fills transformed from self

  with archive.context.raw_file(archive.metadata.mainfile, 'wt') as f:
    f.write(json.dumps(dict(data=transformed.m_to_dict())))

  archive.data = transformed
```

With such a `normalize` function in place, you can apply the re-processing strategy
to migrate.

!!! warning

    There might be issues with this approach depending on how the `normalize` functions
    are executed. This only works well, if after replacing data the `normalize` functions
    of the transformed instance are called and no `normalize` functions of the original
    instance have been called yet.

    Also this approach has risks. If the process fails in unexpected ways there might be
    raw file data being lost.

## Schema packages developed by FAIRmat

The following is a list of plugins containing schema packages developed by FAIRmat:

| Description         | Project url                                                                |
| ------------------- | -------------------------------------------------------------------------- |
| simulation run      | <https://github.com/nomad-coe/nomad-schema-plugin-run.git>                 |
| simulation data     | <https://github.com/nomad-coe/nomad-schema-plugin-simulation-data.git>     |
| simulation workflow | <https://github.com/nomad-coe/nomad-schema-plugin-simulation-workflow.git> |
| NEXUS               | <https://github.com/FAIRmat-NFDI/pynxtools.git>                            |
| synthesis           | <https://github.com/FAIRmat-NFDI/AreaA-data_modeling_and_schemas.git>      |
| material processing | <https://github.com/FAIRmat-NFDI/nomad-material-processing.git>            |
| measurements        | <https://github.com/FAIRmat-NFDI/nomad-measurements.git>                   |
