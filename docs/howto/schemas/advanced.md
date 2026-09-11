# Advanced schema concepts

This page collects the parts of the Metainfo you are unlikely to need when writing your first schema,
but which become useful as schemas grow: modelling tabular scientific data as data frames, populating
and reading sections by name at runtime, inspecting schemas programmatically, and building
definitions dynamically.

## Model data frames

On top of sections, quantities and subsections, the Metainfo provides a mechanism for modelling
*data frames*.

A NOMAD data frame is a multi-index table with named indices (*variables*) and columns (*fields*). All
columns must match in length, because they are all parametrized by the same indices. Both variables
and fields are defined standalone using `Values`, and a `DataFrame` combines fields and variables with
matching dimensions. Conceptually this is close to an xarray dataset, a pandas data frame, or the
NeXus `NXData` group.

A `DataFrame` may contain any number of `Values`; the minimum set is declared with
`mandatory_variables` and `mandatory_fields`.

You normally do not use `Values` and `DataFrame` directly. Instead you create reusable *templates*:
the same kind of `Values` for a physical property such as energy, temperature or pressure, and the
same kind of `DataFrame` for a material property measured against those variables, such as a density
of states or a band gap.

<!-- fmt: off -->
```py
--8<-- "examples/metainfo/data_frames.py:9:31"

--8<-- "examples/metainfo/data_frames.py:41:44"


--8<-- "examples/metainfo/data_frames.py:55:63"
```
<!-- fmt: on -->

### Fields versus variables

Both fields and variables hold columns of values. *Fields* hold the actual data; *variables* span the
data space and provide the column indices.

Variables and dimensions are not quite the same thing. Variables provide the values along a dimension
via shared indices, and the number of variables is often — but not always — equal to the number of
dimensions: variables that depend on each other may span shared dimensions. Fields always provide
values for all dimensions.

Compare a dataset you would plot as a heatmap with one you would plot as a scatter plot. Both have
two variables, `Temperature` and `Pressure`, and one field, `Energy`.

In the heatmap case, temperature and pressure vary independently, so there is an energy value for
every combination. Two values per variable give four field values:

<!-- fmt: off -->
```py
--8<-- "examples/metainfo/data_frames.py:89:97"
```
<!-- fmt: on -->

In the scatter plot case, temperature and pressure vary together. Each pair yields one energy value,
so two readings give two field values:

<!-- fmt: off -->
```py
--8<-- "examples/metainfo/data_frames.py:100:106"
```
<!-- fmt: on -->

The `ValueTemplate` keyword argument `spanned_dimensions` declares how the variables relate. The
indices refer to the indices of the field values and represent the logical dimensions of the data
space. The first example above, without `spanned_dimensions`, is equivalent to spanning two
independent dimensions explicitly:

<!-- fmt: off -->
```py
--8<-- "examples/metainfo/data_frames.py:109:117"
```
<!-- fmt: on -->

### Data frames in the schema versus in parsing

Templates let you declare *mandatory* fields and variables in the schema, which a parser must provide
when instantiating the dataset. Parsers may also provide additional fields and variables, so a
template can be extended without new definitions.

### How data frames are stored

Each call to `ValueTemplate` and `DatasetTemplate` produces a section definition inheriting from
`Values` and `DataFrame` respectively.

`Values` sections define a single `values` quantity, always a NumPy array with the type and shape
given in the template plus one dimension of arbitrary length. Variable values are a flat list anyway.
Field values are always flattened: you may supply them in a higher-dimensional array matching the
dimensionality of the variables, but `values` only provides one extra dimension because the real
number of dimensions is only known at runtime. The original runtime shape is kept in the
`original_shape` quantity.

`DataFrame` sections define repeating `fields` and `variables` subsections. The specific `DataFrame`
produced by a template also carries a `DatasetAnnotation` holding `mandatory_fields` and
`mandatory_variables` for runtime validation. Those subsections hold a `Values` instance for each
mandatory field and variable, plus any extra ones determined during parsing.

Using a `ValuesTemplate` — for example `some_property = Energy()` — creates a quantity that is a copy
of the template's `values` quantity, which is what makes templated value quantities reusable. Using a
`DatasetTemplate` — for example `some_property = BandGap()` — creates a subsection targeting the
`DataFrame` section defined by the template.

!!! warning "Attention"
    Utility functions for translating a `DataFrame` into xarray datasets and pandas data frames exist
    on `DataFrame`, but their documentation is still pending.

## Populate data dynamically

When the property you want to set is only known at runtime, use `m_set` and `m_get` instead of
attribute access. Both accept property names and their aliases:

```python
system.m_set('n_atoms', 3)
value = system.m_get('n_atoms')
```

For repeating subsections, `m_get` takes an `index`, which may be an integer, a slice or a string,
and `as_list=True` forces a list result even for a single match:

```python
second = my_molecule.m_get('atoms', index=1)
just_one = my_molecule.m_get('atoms', index=1, as_list=True)
```

!!! warning "Attention"
    Calling `m_set` with a list on a *repeating* subsection **appends** to the existing sections
    rather than replacing them. To replace the contents, clear the subsection first or assign the
    list directly as an attribute.

## Inspect a schema at runtime

Every section class carries an `m_def` attribute holding its definition, which makes generic,
schema-agnostic traversal straightforward:

```python
print(System.m_def.name)  # Outputs: "System"

for quantity_def in System.m_def.quantities:
    print(f'Quantity Name: {quantity_def.name}')
    print(f'Data Type: {quantity_def.type}')
    print(f'Description: {quantity_def.description}')
```

Besides `quantities` and `sub_sections`, a definition exposes collections such as
`all_base_sections`, `all_inheriting_sections`, `all_properties`, `all_quantities` and
`all_sub_sections`. See {{ nav_link("reference/metainfo.md", breadcrumb=True) }} for the full set.

## Serialize and deserialize

`m_to_dict()` converts a section instance into a plain dictionary, and `m_from_dict()` reconstructs
one, validating the data against the schema as it goes. This pair is the backbone of the archive REST
API:

```python
system = System.m_from_dict(serialized_data)
```

The available serialization options are listed in
{{ nav_link("reference/metainfo.md", breadcrumb=True) }}.

## Create definitions at runtime

Sometimes a schema is not known when the code is written and has to be generated. You can instantiate
`Section`, `Quantity` and `SubSection` objects on the fly and build new `MSection` classes with
standard Python metaprogramming such as the `type` function; alternatively, the `Section` definition
object itself acts as a factory for completely generic structures.

This is how NOMAD realizes YAML schemas: user definitions in `.archive.yaml` files are translated
into Metainfo definitions at runtime.

## Categories

Categories were an earlier mechanism for organizing definitions by generalization, formerly called
*abstract types*.

!!! warning "Attention"
    Categories are deprecated. Use annotations instead — see
    {{ nav_link("reference/annotations.md", breadcrumb=True) }}. The `Category` definition remains in
    {{ nav_link("reference/metainfo.md", breadcrumb=True) }} for backwards compatibility.

## Related materials

- {{ nav_link("howto/plugins/tools/hdf5.md", breadcrumb=True) }} — offload large arrays to HDF5.
- {{ nav_link("howto/plugins/tools/units.md", breadcrumb=True) }} — physical units and display units.
- {{ nav_link("howto/develop/search.md", breadcrumb=True) }} — the `a_elasticsearch` Metainfo extension.
- {{ nav_link("howto/develop/new_type.md", breadcrumb=True) }} — add a new quantity type.
