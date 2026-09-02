# The NOMAD Schema --- Definition and Data

## Introduction

The NOMAD Schema (Metainfo) system is a robust, structured data modelling framework designed to represent complex, hierarchical scientific data.
It provides a strictly typed, object-oriented ecosystem for defining schemas, validating inputs, and serializing data across diverse formats.
By leveraging Python classes and descriptors (as well as YAML files), developers can define schemas and the corresponding data.

The architecture revolves around three fundamental building blocks: `Section`s, `Quantity`s, and `Subsection`s.
Using file system analogy, quantities are similar to files, storing a single field; sections are similar to folders that organize a few quantities together.
Subsections are a special thin wrapper around sections that add additional metadata to them.

This documentation provides a comprehensive guide on designing schemas, managing data lifecycles, and programmatically querying schema definitions on demand.
Every schema element is meticulously tracked, ensuring that data provenance and structural integrity are maintained throughout the normalization pipeline.
It provides built-in mechanisms for physical unit management, array shape validation, and automated conversions.
Developers can dynamically modify or inspect these schemas at runtime to build flexible data ingestion pipelines.

## Core Components

### Abstract Section (`MSection`)

The `MSection` is an abstract class that serves as the base class and class factory for all derived classes.
The design is based on [reflection](https://en.wikipedia.org/wiki/Reflective_programming){:target="_blank" rel="noopener"}, which can sometimes be quite difficult to comprehend.

Every `MSection` instanced automatically generates a corresponding schema definition object, accessible via the `m_def` attribute.
This applies to not only the data instances, in which `m_def` points to the schema object, but also schema objects themselves, in which case `m_def` points to ***the schema of the schema***.

As an abstract class, normal development typically do not need to touch it.

### Sections (`Section`)

Sections are the primary structural nodes.
They are defined by subclassing the `Definition` base class provided by the `nomad.metainfo` module.
A `Section` acts as a container that groups related data and nested structures into a cohesive logical unit.
It can contain arbitrary number of quantities and subsections.
Sections support multiple inheritance, allowing you to compose complex data models from reusable, modular base classes.

### Quantities (`Quantity`)

Quantities define the actual data fields that reside within a section.
They are defined as class attributes on an `Section` subclass using the `Quantity` descriptor.
Each Quantity must specify a data type, which dictates how values are parsed, validated, and serialized.
These types can range from simple primitives like integers and strings to complex multi-dimensional NumPy arrays with physical units.
Quantities enforce strict validation rules through parameters like `shape`, which defines the expected dimensions of an array.
Physical properties are handled seamlessly by specifying a `unit` parameter, allowing the system to automatically extract and convert magnitudes.
You can attach extensive metadata to quantities, including descriptions, default values, and other attributes for UI rendering.

### Subsections (`SubSection`)

Subsections establish the hierarchical relationships between different sections.
They are defined as class attributes using the `SubSection` descriptor, pointing from a parent section to a child section definition.
This relationship forms a directed acyclic graph, organizing data into a strict tree structure.
Subsections can be defined as single instances or lists of instances using the `repeats` boolean flag.
When a subsection is set to repeat, the parent section can hold an unbounded number of child section instances under the same key/name.
This mechanism is essential for representing lists of entities, such as multiple atoms within a molecular system or iterative calculation steps.

## Defining Schemas and Organizing Data

### Basic Schema Definition

Defining a schema involves creating Python classes that inherit from `Section`.
Inside these classes, you declare your properties using `Quantity` and `SubSection`.
The declarative syntax closely mirrors standard Python `dataclass`es.
Here is a comprehensive example demonstrating a basic schema definition.

```python
from nomad.metainfo import Quantity, Section, SubSection

class Atom(Section):
    """Represents a single atom within a system."""

    element = Quantity(
        type=str,
        description="The chemical symbol of the atom."
    )

    position = Quantity(
        type=float,
        shape=['*'],
        unit='angstrom',
        description="The 3D coordinates of the atom."
    )

class System(Section):
    """Represents a physical system composed of atoms."""

    system_type = Quantity(
        type=str,
        default="molecule",
        description="The type of the physical system."
    )

    atoms = SubSection(
        sub_section=Atom,
        repeats=True,
        description="The list of atoms comprising this system."
    )
```

In this example, the `System` class acts as the root node.
It contains a repeated Subsection pointing to the `Atom` class.
The `Atom` class defines specific quantities with explicit types and shapes, ensuring that positions are always arrays of floats.

The type of quantities is further explained in [this page](./schema_type_system.md).

### Inheritance and Polymorphism

The object-oriented inheritance principles is fully supported.
You can create abstract base sections to define common properties shared across multiple concrete implementations.
This drastically reduces boilerplate code and enforces consistency across large scientific datasets.

```python
class BaseCalculation(Section):
    """An abstract base class for all calculation types."""

    energy = Quantity(
        type=np.float64,
        unit='joule',
        description="The total energy calculated."
    )

class DFTCalculation(BaseCalculation):
    """A concrete implementation for Density Functional Theory calculations."""

    xc_functional = Quantity(
        type=str,
        description="The exchange-correlation functional used."
    )
```

When iterating over data, you can query for instances of `BaseCalculation`, and the system will natively resolve all polymorphic subclasses like `DFTCalculation`.

## Creating Data Instances and Populating Data

### Instantiating Sections

Once the schema is defined, creating data instances is as simple as instantiating the Python classes.
The constructor accepts keyword arguments corresponding to the defined quantities/subsections.
If a quantity that has a default value is omitted, the instance will automatically use that default.

```python
# Instantiate an atom using keyword arguments.
carbon_atom = Atom(element='C', position=[0.0, 0.0, 0.0])

# Instantiate another atom and assign values manually.
oxygen_atom = Atom()
oxygen_atom.element = 'O'
# At this point, oxygen_atom.position is None.
oxygen_atom.position = [1.2, 0.0, 0.0]
```

### Populating Subsections

Subsections are populated differently depending on whether they are singular or repeated.
For a non-repeating subsection, you assign the child instance directly to the attribute.
For a repeating subsection, the attribute acts as a list, and you must use the `append` or `extend` methods to add child instances.

```python
# Create the parent system.
my_molecule = System(system_type="molecule")

# Append child sections to the repeated subsection list.
my_molecule.atoms.append(carbon_atom)
my_molecule.atoms.append(oxygen_atom)
```

It is possible to directly assigned a list to a repeated subsection.

```python
my_molecule.atoms = [carbon_atom, oxygen_atom]
```

### Uniform Setter

When the attributes are known in advance, directly assigning values to those attributes are convenient.
More often, one wants to dynamically populate data, there is a general method `m_set` to be used to populate any values to the target section.

The signature reads:

```python
def m_set(
    self,
    def_or_name: Property | str,
    value,
    *,
    hint: str | None = None,
    skip_virtual: bool = False,
    index: int | None = None,
    context: Context | None = None,
    **kwargs,
):
    """
    Set the given value for the given property.

    Parameters:
        def_or_name: The definition of the target property.
            It can also be the name/alias of the property.
        value: The value to set.
            A None value in `overwrite` mode will unset the property.
        hint: Only used for quantities that have variadic names.
            The hint is the name of one of the attributes defined in the target quantity.
            This will be used to help identify which quantity to set.
        skip_virtual: If true, skip setting virtual properties.
        index: Only used for repeating subsections in 'overwrite' mode.
            No effect in 'append' mode.
        context: The context to use when deserializing the value.
            This is used in setting sections, while the value is given as a serialized dictionary.
        kwargs: Additional keyword arguments to pass to the property setter.
    """
    pass
```

By using strings as `def_or_name`, it can be used to set both quantities and subsections.

```python
new_atom = Atom(element='C')
# Set a quantity
new_atom.m_set('position', [1, 2, 3])
# Set/add a new section at the target position
my_molecule.m_set('atoms', new_atom, index=4)
```

**It must be noted that `m_set` a repeating subsection with a list will append to the existing data.**

```python
# !!! THIS DOES NOT OVERWRITE EXISTING DATA
my_molecule.m_set('atoms', [Atom(element='C', position=[0.0, 1.0, 0.0])])
```

A closely related method `m_append` can also be used to populate data to existing sections/quantities.
The difference is `m_append` only appends to list-like data such as array quantities and repeating subsections.

### Uniform Getter

The counterpart of a setter is a getter.
One can use `m_get` to access data.

```python
def m_get(
    self,
    def_or_name: Property | str | list[Property | str],
    *,
    full: bool = False,
    hint: str | None = None,
    index: int | slice | str | None = None,
    as_list: bool = False,
):
    """
    Retrieve the given property of the current section.

    Parameters:
        def_or_name: The definition of the target property.
            It can also be the name/alias of the property.
            A list of names or definitions can be provided to get multiple properties at once.
        full: Only used for quantities that use full storage.
            If True, the MQuantity object instead of the value will be returned.
        hint: Only used for quantities that have variadic names.
            The hint is the name of one of the attributes defined in the target quantity.
            This will be used to help identify which quantity to use.
        index: Only used if the property is a list.
            It can be an integer, a slice, for both quantities and subsections.
            It can also be a string, for subsections only.
        as_list: If True, return the value wrapped in a list.

    Returns:
        The value of the property.
    """
    pass
```

For example,

```python
# a single Atom section
print(my_molecule.m_get('atoms', index=1))
# a list containing a single Atom section
print(my_molecule.m_get('atoms', index=1, as_list=True))
```

### Assigning Arrays and Physical Quantities

When assigning data to Quantities with specific shapes and units, the system leverages Pint and NumPy for validation.
If you assign a standard Python list to an array quantity, it is seamlessly coerced into a NumPy array.
If you assign a Pint `Quantity` object, the system automatically extracts the magnitude and converts it to the declared target unit.

!!! note
    The rule used by the system is simple.
    If the `type` of a quantity is a `numpy` type, for example, `numpy.int32`, the array quantity will be converted into a NumPy array.
    If the `type` of a quantity is a Python type, for example, `float`, `int`, the array quantity will be converted into a Python (nested) list.

## Data Manipulation, Validation, and Normalization

### The Normalization Lifecycle

Data within the schema system is not static; it often undergoes a normalization lifecycle.
Normalization is the process of computing derived quantities, standardizing inputs, and enforcing cross-field constraints.
Every section can define a `normalize` method that is invoked recursively by the system.
This method takes an archive context and an optional logger object to track warnings and errors.

```python
class NormalizedAtom(Section):
    element = Quantity(type=str)
    mass = Quantity(type=np.float64, unit='amu')
    
    def normalize(self, archive, logger):
        super().normalize(archive, logger)
        if self.element == 'C' and self.mass is None:
            self.mass = 12.011
        elif self.element == 'O' and self.mass is None:
            self.mass = 15.999
```

When you trigger normalization on a root section, it walks down the tree, invoking the `normalize` method on every child section from the bottom up.
This ensures that parent sections can safely rely on the normalized data of their children.

In principle, sections shall be designed in such a way that logically related data shall be defined in the same section.
A good criterion is that, when normalizing a section, no information external to that section is required.

This is however the ideal case.
In practice, often it is very difficult, if not impossible, to achieve.
It is possible to access the external via `self.m_parent` to access the parent section and/or `self.m_root` to access to the root section.

!!! warning
    It is strongly discouraged to change data external to the current section during normalization process.

## Serializing and Deserializing Data

### Serializing to Dictionaries (JSON)

To interface with external systems, APIs, or databases, sections must be converted into standard data formats.
The `m_to_dict` method exports the entire hierarchical Section, including all populated quantities and subsections, into a nested Python dictionary.
This dictionary is strictly composed of JSON-serializable primitives.
NumPy arrays are converted to nested Python lists.

The signature reads:

```python
def m_to_dict(
    self,
    with_meta: bool = False,
    with_root_def: bool = False,
    with_out_meta: bool = False,
    with_def_id: bool = False,
    with_index: bool = False,
    include_defaults: bool = False,
    include_derived: bool = False,
    resolve_references: bool = False,
    stable_references: bool = False,
    categories: list[Category | type[MCategory]] | None = None,
    include: TypingCallable[[Definition, MSection], bool] | None = None,
    exclude: TypingCallable[[Definition, MSection], bool] | None = None,
    transform: TypingCallable[[Definition, MSection, Any, str], Any] | None = None,
    subsection_as_dict: bool = False,
    return_as_generator: bool = False,
) -> dict:
    """
    Returns the data of this section as a (json serializable) dictionary.

    With its default configuration, it is the opposite to :func:`MSection.m_from_dict`.

    There are a lot of ways to customize the behavior, e.g. to generate JSON for
    databases, search engines, etc.

    Arguments:
        with_meta: Include information about the section definition, the sections
            position in its parent, and annotations. For Definition instances this
            information will be included regardless; the section definition will
            always be included if the subsection definition references a base section
            and the concrete subsection is derived from this base section.
        with_out_meta: Exclude information `with_meta` information, even from
            Definition instances.
        with_root_def: Include the m_def for the top-level section. This allows to
            identify the used "schema" based on the root section definition.
        with_def_id: Include the definition id for the top-level section. This
            allows detection different versions of section definition used.
        with_index: Include index for subsections.
        include_defaults: Include default values of unset quantities.
        include_derived: Include values of derived quantities.
        resolve_references:
            Treat references as the sections and values they represent. References
            must not create circles; there is no check and danger of endless looping.
        categories: A list of category classes or category definitions that is used
            to filter the included quantities and subsections. Only applied to
            properties of this section, not on subsections. Is overwritten
            by partial.
        include: A function that determines if a property (quantity or subsection) will
            be included in the results. It takes the property definition and the current
            section as arguments. The function returns true for including and false for
            excluding the property. Include is applied recursively on subsections.
            Overrides categories.
        exclude: A function that determines if a property (quantity or subsection) will
            be excluded from the results. It takes the property definition and the current
            section as arguments. The function returns true for excluding and false for
            including the property. Exclude is applied recursively on subsections.
            Overrides categories.
        transform: A function that determines serialized quantity values.
            It takes the quantity definition, current section, the default
            serialized value and the metainfo path with respect to the
            document root as arguments. Depending on where this is used, you
            might have to ensure that the result is JSON-serializable.  By
            default, values are serialized to JSON according to the quantity
            type.
        stable_references: If true, use stable identifiers for definition
            references (e.g. base_sections, sub_section) instead of path-based
            keys. Stable identifiers use the format `qualified_name@tag`.
        subsection_as_dict: If true, try to serialize subsections as dictionaries.
            Only possible when the keys are unique. Otherwise, serialize as list.
        return_as_generator: If true, return as a generator instead of a dict.
    """
    pass
```

```python
# Serialize the entire system object.
serialized_data = my_molecule.m_to_dict()
print(serialized_data)
# Output will resemble:
# {
#     'm_def': '...',
#     'system_type': 'molecule',
#     'atoms': [
#         {
#             'm_def': '...',
#             'm_parent_index': 0,
#             'm_parent_sub_section': 'atoms',
#             'element': 'C',
#             'position': [0.0, 0.0, 0.0],
#         },
#         {
#             'm_def': '...',
#             'm_parent_index': 1,
#             'm_parent_sub_section': 'atoms',
#             'element': 'O',
#             'position': [1.2, 0.0, 0.0],
#         },
#     ],
# }
```

You can strictly control the serialization output using keyword arguments.

This serialized data is stored and communicated to the front end for UI rendering.

### Deserializing from Dictionaries

Reconstructing a Section from a dictionary is handled by the `m_from_dict` class method.
This method recursively traverses the dictionary, instantiates the correct Section subclasses, and populates the Quantities.
It performs thorough validation during ingestion, rejecting payload keys that do not exist in the schema.

```python
# Reconstruct the system from the dictionary payload.
restored_system = System.m_from_dict(serialized_data)
assert restored_system.atoms[0].element == 'C'
```

This bi-directional serialization pipeline forms the backbone of the NOMAD platform's REST API.

## Dynamic Schemas and Querying

### Reflection via `m_def`

The schema system provides powerful reflection capabilities, allowing developers to inspect schemas programmatically.
Every section class possesses an `m_def` attribute representing its metadata definition.
The `m_def` object contains lists of all `quantities` and `sub_sections` attached to the schema.
This makes it incredibly easy to write generic, schema-agnostic traversal algorithms.

```python
# Inspecting the System schema definition.
print(System.m_def.name) # Outputs: "System"

# Iterate over all defined quantities in the System schema.
for quantity_def in System.m_def.quantities:
    print(f"Quantity Name: {quantity_def.name}")
    print(f"Data Type: {quantity_def.type}")
    print(f"Description: {quantity_def.description}")
```

There is a wide range of different collections of useful information that can be accessed: `all_base_sections`, `all_inheriting_sections`, `all_properties`, `all_quantities`, `all_sub_sections`, etc.
Details can be found in the source code.

### Creating Classes Dynamically at Runtime

In advanced use cases, schemas are not known at compile time and must be generated dynamically.
The NOMAD schema system allows you to instantiate `Section`, `Quantity`, and `SubSection` objects on the fly.
You can use standard Python metaprogramming (like the `type` function) to create new `MSection` classes dynamically.
Alternatively, the `Section` definition object itself acts as a factory that can construct completely generic schema structures.
This dynamic generation is heavily utilized by NOMAD's custom schema plugin system, where users define schemas in YAML files that are translated at runtime.
