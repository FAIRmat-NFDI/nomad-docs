# Schema language

The NOMAD Metainfo is the schema language used to define all data in NOMAD. This page is the
authoritative reference for the language itself: the attributes you can put on a definition, the
quantity types you can declare, and the conventions definitions should follow.

For task-oriented instructions, see [How-to guides > Work with schemas](../howto/schemas/schemas.md).
For the concepts behind the language, see [Explanation > Data structure](../explanation/data.md).

## Quantity types

The `type` of a quantity determines what values it accepts, how they are validated and converted,
and how they are serialized. Type names are **case insensitive**.

| YAML spelling | Python spelling | Runtime type | Serialized form | Notes |
| --- | --- | --- | --- | --- |
| `string`, `str` | `str` | `str` | JSON string | |
| `boolean`, `bool` | `bool` | `bool` | JSON boolean | |
| `int` | `int` | 32-bit integer | JSON number | Bare `int` is **32-bit**. Use `np.int64` for wider values. |
| `float` | `float` | 64-bit float | JSON number | |
| `complex` | `complex` | `complex` | `{"re": ..., "im": ...}` | |
| `np.int8`, `np.int16`, `np.int32`, `np.int64` | same | NumPy integer | JSON number or nested array | |
| `np.float16`, `np.float32`, `np.float64` | same | NumPy float | JSON number or nested array | |
| `np.complex128` | same | NumPy complex | `{"re": ..., "im": ...}` | |
| `Datetime` | `Datetime` | `datetime.datetime` (UTC) | ISO 8601 string | |
| `{type_kind: Enum, type_data: [...]}` | `MEnum('a', 'b')` | `str` | JSON string | Use `type_data` to list the allowed values. |
| `JSON` | `JSON` | `dict` | JSON object | Arbitrary nested JSON. |
| `Bytes` | `Bytes` | `bytes` | base64 string | The Python `bytes` type itself is **not** accepted; use the name. |
| `URL` | `URL` | `str` | JSON string | |
| `File` | `File` | `str` | JSON string | A path relative to the upload. |
| `Capitalized` | `Capitalized` | `str` | JSON string | Capitalizes the first letter on assignment. |
| `Any` | `Any` | any | as-is | No validation. |
| `User` | `User` | NOMAD user | user id string | |
| `Author` | `Author` | `Author` | JSON object | |
| `*<section name>*` | `MySection` | section instance or `MProxy` | reference URL | See [Work with schemas > Link data with references](../howto/schemas/references.md). |

### What you can write in `type`

Types are resolved by `nomad.metainfo.data_type.normalize_type()`, which accepts:

- **Strings** — `'string'`, `'boolean'`, `'json'`, `'datetime'`, `'url'`, `'file'`, `'any'`,
  `'capitalized'`, `'bytes'`, `'user'`, `'author'`, or any builtin name such as `'int'` and `'float'`.
- **NumPy names** — any `np.<dtype>` or `numpy.<dtype>` string, e.g. `'np.float64'`.
- **Python types** — `str`, `bool`, `int`, `float`, `complex`, `datetime.datetime`. Note that the
  Python `bytes` type is not accepted, only the string `'bytes'`.
- **NumPy types** — `np.int16`, `np.float32`, `np.complex128`, `np.bool_`, and `np.dtype(...)` instances.
- **Dictionaries** — the `{'type_kind': ..., 'type_data': ...}` form produced when a definition is
  serialized. This is how `MEnum` and custom types round-trip.

To add a type that is not in this list, see
[How-to guides > Develop the core software > Add a new type](../howto/develop/new_type.md).

## Shapes

The `shape` of a quantity is a list of dimensions. An empty list (or no shape) is a scalar, one
dimension is a vector, two a matrix, and so on. Each dimension may be:

- an integer, for a fixed size — a 3x3 matrix is `[3, 3]`;
- the string `'*'`, for an arbitrary size — a list is `['*']`;
- the name of a sibling quantity with an integer type, e.g. `['number_of_atoms', 3]`.

!!! note
    `shape` works the same way for every quantity type, including reference types. For a reference
    type it describes the dimensionality of the *references*, not of the referenced data.

## Value coercion

Values are converted to the declared type and unit on assignment, using
[NumPy](https://numpy.org/){:target="_blank" rel="noopener"} and
[Pint](https://pint.readthedocs.io/en/stable/){:target="_blank" rel="noopener"}. Assigning a Pint
quantity extracts the magnitude and converts it to the declared unit.

The rule for array quantities is:

- if the `type` is a NumPy type, such as `np.int32`, the value becomes a NumPy array;
- if the `type` is a Python type, such as `float` or `int`, the value becomes a (nested) Python list.

Units are given as strings parsed by Pint — simple units or expressions, e.g. `m`, `meter`, `mm`,
`m/s`, `m/s**2`. Uploaded schemas may use any unit; the built-in NOMAD schema uses SI units only.
See [Work with schemas > Work with units](../howto/plugins/tools/units.md).

## Naming conventions

- **Section definitions** use `UpperCamelCase`, e.g. `MySection`, `PvdEvaporation`.
- **Quantities and subsections** use `lower_snake_case`, e.g. `chamber_pressure`, `data_file`.
- Use a `_ref` suffix for quantities that hold references, e.g. `sample_ref`.
- Prefer subsections over inheritance when adding specific quantities to a general section. For
  example, the `workflow` section contains a `geometry_optimization` subsection for the quantities
  that only apply to geometry optimizations.
- Prefix parser-specific and user-defined definitions with `x_<name>_`, where `<name>` is the short
  handle of a code or method, e.g. `x_vasp_incar`.

These conventions apply equally to YAML and Python schemas. In Python they are not optional: a
definition takes its name from the Python class or attribute name, so it must be a valid identifier.

## Where definitions live

The `nomad-lab` package defines the Metainfo in three modules:

- `nomad.metainfo` — the schema language itself, including its self-referencing schema. This is the
  package rendered below.
- `nomad.datamodel` — the root section `EntryArchive` and the `metadata` section holding
  administrative metadata.
- `nomad.datamodel.metainfo` — the central, method-specific (but not parser-specific) definitions
  that are shared across parsers.

## Serialization options

`m_to_dict()` converts a section instance to a plain dictionary. The options you are most likely to
need:

| Option | Effect |
| --- | --- |
| `with_meta` | Include `m_def`, and `m_parent_index`/`m_parent_sub_section` where applicable. |
| `with_def_id` | Include the [definition id](../howto/schemas/evolution.md) of each definition. |
| `include_defaults` | Include quantities that still hold their default value. |
| `include_derived` | Include derived quantities. |
| `resolve_references` | Replace references with the sections they point to, instead of reference URLs. |
| `categories` | Only include definitions in the given categories. |
| `include`, `exclude` | Filter properties by a predicate. |
| `transform` | Apply a function to every serialized value. |

`m_from_dict()` performs the inverse, reconstructing a section tree from a dictionary and validating
it against the schema. It is the mechanism behind the archive REST API.

## Definition reference

The following is generated from the `nomad.metainfo` package, which defines the schema language in
terms of itself. `Section`, `Quantity` and `SubSection` are the definitions you use to write a
schema; `Definition` holds the attributes they all share.

!!! note
    The `more` attribute is not listed below. It collects any additional keyword arguments passed to
    a definition, so that schemas can carry custom metadata. `Category` is retained for backwards
    compatibility but is deprecated — use annotations instead.

{{ metainfo_package('nomad.metainfo.metainfo') }}
