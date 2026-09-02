# The NOMAD Schema --- Type System

## Overview

The NOMAD type system (`nomad.metainfo.data_type`) is a core foundational component of the NOMAD platform.

In NOMAD, data is modelled using schemas consisting of *Sections* and *Quantities*.
The type system is responsible for defining how primitive values, complex domain-specific objects, multidimensional arrays, and references are validated, converted, normalized, serialized, and mapped across multiple downstream storage and search engines (such as MongoDB, Elasticsearch, Pydantic models, JSON Schema, and OPTIMADE API specifications).

### Core Goals of the Type System

- **Robust Normalization & Validation**: Accept inputs from diverse sources (manual user input, raw parser outputs, serialized archive JSON files, Pandas DataFrames, NumPy arrays, Pint units) and coerce them into predictable Python/NumPy objects.
- **Unit and Dimensionality Awareness**: Seamlessly extract magnitudes from physical quantities (`pint.Quantity`) and validate unit dimensionalities against quantity definitions.
- **Bi-directional Serialization**: Convert standard runtime Python objects into JSON-compliant primitives for storage and transmission, while preserving schema metadata.
- **Multidimensional Array Support**: Handle both scalar values and multi-dimensional NumPy arrays or nested lists with strict shape checking.
- **Interoperability**: Seamlessly map to/from various database schemas including Elasticsearch, MongoDB (MongoEngine), Pydantic, JSON Schema, and OPTIMADE.

## Architecture and Class Hierarchy

The type system is built on an object-oriented class hierarchy headed by the abstract base class `Datatype`.
An incomplete overview looks like this.
Please note that the tree layout does not necessarily imply inheritance.

```text
                        +-------------------+
                        |     Datatype      |
                        +---------+---------+
                                  |
            +---------------------+-----------------+
            |                                       |
  +---------+---------+                   +---------+---------+
  |     Primitive     |                   |   NonPrimitive    |
  +---------+---------+                   +---------+---------+
            |                                       |
  +---------+---------+               +-------------+---------------+
  |      Number       |               |             |               |
  +---------+---------+           +---+---+     +---+---+     +-----+-----+
            |                     |  URL  |     | File  |     | Datetime  |
   +--------+--------+            +-------+     +-------+     +-----------+
   |                 |                |             |             |
+--+----------+  +---+-------+    +---+---+     +---+---+     +-----+-----+
| ExactNumber |  | Inexact   |    | Bytes |     | JSON  |     |   Unit    |
+--+----------+  | Number    |    +-------+     +-------+     +-----------+
   |             +---+-------+        |             |             |
 +-+-----+           |            +---+---+     +---+---+     +-----+-----+
 | m_int |        +--+----+       | Enum  |     | Any   |     | Callable  |
 +-------+        |m_float|       +-------+     +-------+     +-----------+
                  +-------+
```

### The Abstract Base Class: `Datatype`

`Datatype` defines the common interface and state flags for all types in the system:

- **Key Attributes / Slots**:
    - `_definition`: The associated `Quantity` or `SubSection` definition object.
    - `_support_array`: Boolean indicating if array values are supported (default: `True`).
    - `_disable_shape_check`: Flag to bypass array/scalar shape validation.
    - `_disable_type_check`: Flag to bypass strict type check enforcement.
    - `_disable_auto_conversion`: Flag to disable automatic type casting.
- **Derived Properties**:
    - `shape`: Retrieved from `_definition.shape` that specifies dimensions.
    - `is_scalar`: Returns `True` if shape is None or empty.
    - `unit`: Attached physical unit from definition.

### `Primitive` Types

`Primitive` inherits from `Datatype` and encapsulates data types natively supported by Python and NumPy (`int`, `float`, `complex`, `str`, `bool`).

- **Internal Mechanics**:
    - `_dtype`: Stores the underlying concrete Python or NumPy dtype (e.g., `np.int32`, `np.float64`, `bool`, `str`).
    - `_np_base`: Base type class (`np.integer`, `np.inexact`, `np.bool_`, `np.str_`) used to decide whether normalized array outputs should remain NumPy arrays or convert to Python lists.
- **Hierarchy of Primitives**:
    - **`Number`** *(Abstract)*: Base for numeric types.
        - **`ExactNumber`**: Integer types (`np.integer`). Implemented by `m_int` and concrete subclasses: `m_int8`, `m_int16`, `m_int32`, `m_int64`.
        - **`InexactNumber`**: Floating-point and complex types (`np.inexact`). Implemented by `m_float` (`m_float16`, `m_float32`, `m_float64`) and `m_complex` (`m_complex128`).
    - **`m_bool`**: Boolean values (`bool` or `np.bool_`).
    - **`m_str`**: String values (`str` or `np.str_`).

### `NonPrimitive` Types

`NonPrimitive` is the base class for rich domain-specific types.
Unlike primitives, `NonPrimitive` classes execute element-wise operations via template methods `_normalize_impl()` and `_serialize_impl()`.

Supported `NonPrimitive` types:

- **`Datetime`**: Converts strings (via `dateutil`), Unix timestamps, `date`, `pd.Timestamp`, or `np.datetime64` into UTC-aware `datetime.datetime` objects. Serializes to ISO-8601 strings.
- **`Unit`**: Converts string unit declarations or `pint.Quantity` objects to `pint.Unit` instances while validating physical dimensionality using `check_dimensionality`.
- **`Enum`**: String enumerations configured with a fixed set of allowed string values and optional description mappings (`m_descriptions`).
- **`JSON`**: Validates dictionary inputs and standardizes key-value structures using `orjson`.
- **`Bytes`**: Handles raw byte strings or base64-encoded ASCII strings.
- **`URL` / `File`**: Validates uniform resource locators and file relative path references within NOMAD archives.
- **`Capitalized`**: Coerces input strings to capitalized format (`value.capitalize()`).
- **`Dimension`**: Represents matrix/tensor dimension bounds (integers or dimension symbols).
- **`Callable`**: Validates callable Python objects and optional argument counts (`nargs`).
- **`Any`**: Transparent pass-through type.

### Reference Types

- **`Reference` / `MSectionReference` / `QuantityReference`**: Handle typed cross-references to other sections or quantities across archives. Users typically do not need to handle those types manually.

## Core Methods and Mechanics

### `normalize(value, **kwargs)`

The `normalize()` method is the workhorse of the type system.
It takes raw, unstructured, or parsed input data and converts it into a valid, strongly-typed internal representation.
All the normalization, validation, etc. shall happen in this method.

***It is important to ensure the value returned is valid and complies with the definition as no additional checks will performed and other parts of the system expect only valid data.***

The parent section that contains the destination data is available via `kwargs`, for example, `section=kwargs.get('section')`.
This may be useful when interactions with the parent container is necessary.

#### Normalization Pipeline for Primitives

1. **Unit & Magnitude Extraction**: If `value` is a `pint.Quantity`, `normalize()` extracts its numerical magnitude (`extract_magnitude`). If a target unit is configured on the definition, it converts the quantity to the definition's unit before extracting the magnitude.
2. **Scalar Normalization**:
    - Checks if input type matches `_dtype`.
    - If auto-conversion is disabled (`_disable_auto_conversion`) and types differ, raises `ValueError`.
    - Checks explicit convertibility via `convertible_from()`.
    - Attempts safe type conversion or close numeric comparison (`np.isclose`).
3. **Array Normalization**:
    - Converts input (`pd.DataFrame`, `pd.Series`, `list`, `tuple`, `np.ndarray`) to a NumPy array.
    - Performs dtype casting safely (`array.astype(self._dtype, casting='safe')`).
    - Converts back to Python lists if `_dtype` is a pure Python type rather than a NumPy base type.
    - Applies `_check_shape()` to enforce array dimensions against `self.shape`.

***Although at the current stage it makes little to no difference as eventually all data is stored in a JSON-compatible format, the validation also considers strong safe type conversion in such a way that no data loss could potentially occur.***

#### Normalization Pipeline for NonPrimitives

- Enforces 1D/scalar shape constraints via `_check_shape()`.
- Iterates over elements (for lists) or directly invokes `_normalize_impl(value, **kwargs)` for scalars.

### `serialize(value, **kwargs)`

`serialize()` converts valid internal runtime values (e.g., NumPy arrays, `datetime` objects, `pint.Unit` objects) into standard JSON-serializable structures (dicts, primitives, lists).

- **Transform Hooks**: Accepts an optional `transform(val, path)` callback, enabling recursive transformation of array elements or scalar fields during serialization.
- **Primitive Serialization**: Converts NumPy arrays (`tolist()`) and scalar generics (`item()`) into standard Python lists and primitives.
- **NonPrimitive Serialization**: Delegates element-wise conversion to `_serialize_impl()`. For instance, `Datetime` calls `isoformat()`, `Unit` returns `str(value)`, and `Bytes` encodes bytes to base64 ASCII strings.

### `serialize_self()`

Serializes the metadata of the `Datatype` object itself into a dictionary containing `type_kind`, `type_data`, and active flags.
This is mainly used in serializing the schema.

Example output for `m_int32`:

```python
{
    'type_kind': 'numpy',
    'type_data': 'int32',
    'disable_shape_check': False
}
```

### Type Resolver: `normalize_type(value)`

`normalize_type()` serves as a central factory function that parses flexible shorthand type declarations into concrete `Datatype` instances.
It supports:

- **Strings**: `'string'` -> `m_str()`, `'boolean'` -> `m_bool()`, `'np.float64'` -> `m_float64()`, `'datetime'` -> `Datetime()`, `'json'` -> `JSON()`, etc.
- **Python Types**: `int` -> `m_int32()`, `float` -> `m_float64()`, `str` -> `m_str()`, `bool` -> `m_bool()`, `datetime` -> `Datetime()`.
- **NumPy Types**: `np.int16`, `np.float32`, `np.complex128`, `np.bool_`.
- **Dictionaries**: Reconstructs types from `serialize_self()` output dictionaries.

## How to Add a New Type to the System

Adding a custom type involves subclassing either `NonPrimitive` (for custom objects/strings) or `Primitive` (for scalar/array types), implementing required serialization and normalization methods, and registering the type in `normalize_type()`.

The following checklist can be used.

- Step 1: Subclass `NonPrimitive` or `Primitive`: Inherit from `NonPrimitive` if your custom type operates on individual scalar values or 1D lists.
- Step 2: Implement `_normalize_impl(self, value, **kwargs)`: Define input validation and parsing logic. Convert valid inputs into your canonical runtime object representation, or raise `TypeError`/`ValueError` if validation fails.
- Step 3: Implement `_serialize_impl(self, value, **kwargs)`: Define how the canonical runtime object converts into a JSON-serializable structure (e.g., string, dict, int).
- Step 4: Implement `standard_type(self)` and `serialize_self()`: Specify the generic Python type name (used by schema mappers) and self-serialization metadata dictionary.
- Step 5: Register in `normalize_type()`: Add string lookup aliases for your new type inside `normalize_type()`.

## Summary Matrix of Built-in Data Types

The following are common types that can be used.

| Type Class     | Python / Runtime Type       | Example Normalized Input  | Serialized Output             | Target Mongo / Elastic / Schema |
|-:--------------|-:---------------------------|-:-------------------------|-:-----------------------------|-:-------------------------------|
| `m_int32`      | `int` or `np.int32`         | `42`, `"42"`              | `42`                          | `IntField` / `integer`          |
| `m_float64`    | `float` or `np.float64`     | `3.14`, `100 cm` (mag)    | `3.14`                        | `FloatField` / `double`         |
| `m_complex128` | `complex` / `np.complex128` | `1+2j`, `{'re':1,'im':2}` | `{'re': 1.0, 'im': 2.0}`      | Custom object / string          |
| `m_bool`       | `bool` / `np.bool_`         | `True`, `"True"`          | `True`                        | `BooleanField` / `boolean`      |
| `m_str`        | `str` / `np.str_`           | `"NOMAD"`                 | `"NOMAD"`                     | `StringField` / `keyword`       |
| `Datetime`     | `datetime.datetime` (UTC)   | `"2026-08-25"`            | `"2026-08-25T00:00:00+00:00"` | `DateTimeField` / `date`        |
| `Unit`         | `pint.Unit`                 | `"joule"`, `"J"`          | `"joule"`                     | `StringField` / `keyword`       |
| `Enum`         | `str`                       | `"running"`               | `"running"`                   | `StringField` / `keyword`       |
| `JSON`         | `dict`                      | `{'a': 1}`                | `{'a': 1}`                    | `DictField` / `object`          |
| `Bytes`        | `bytes`                     | `b"data"`, `"ZGF0YQ=="`   | `"ZGF0YQ=="`                  | String / Binary                 |
| `URL`          | `str`                       | `"https://nomad-lab.eu"`  | `"https://nomad-lab.eu"`      | `StringField` / `keyword`       |
