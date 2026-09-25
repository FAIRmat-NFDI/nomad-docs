# How to add a new type

The Metainfo type system lives in `nomad.metainfo.data_type`. It is responsible for validating
incoming values, converting them to a canonical runtime representation, enforcing shapes and units,
and serializing values to and from JSON.

Adding a custom type means subclassing `NonPrimitive` or `Primitive`, implementing the normalization
and serialization methods, and registering the type in `normalize_type()`. This is core-software work
— it requires changes to `nomad-lab` itself. For the types that already exist, see
{{ nav_link("reference/metainfo.md", breadcrumb=True) }}.

## Checklist

1. **Subclass `NonPrimitive` or `Primitive`.** Inherit from `NonPrimitive` if your type operates on
   individual scalar values or 1D lists; from `Primitive` if it wraps a native Python or NumPy scalar
   or array type.
1. **Implement `_normalize_impl(self, value, **kwargs)`.** Define input validation and parsing.
   Convert valid input into your canonical runtime representation, or raise `TypeError`/`ValueError`
   if validation fails.
1. **Implement `_serialize_impl(self, value, **kwargs)`.** Define how the canonical runtime object
   becomes a JSON-serializable structure — a string, dict or number.
1. **Implement `standard_type(self)` and `serialize_self()`.** Specify the generic Python type name
   used by schema mappers, and the self-serialization metadata dictionary.
1. **Register in `normalize_type()`.** Add the string lookup aliases for your new type.

## Background

### The `Datatype` base class

`Datatype` defines the common interface and state flags shared by every type:

- Key attributes:
    - `_definition` — the associated `Quantity` or `SubSection` definition.
    - `_support_array` — whether array values are supported (default `True`).
    - `_disable_shape_check` — bypass array/scalar shape validation.
    - `_disable_type_check` — bypass strict type check enforcement.
    - `_disable_auto_conversion` — disable automatic type casting.
- Derived properties:
    - `shape` — the dimensions, from `_definition.shape`.
    - `is_scalar` — `True` if the shape is `None` or empty.
    - `unit` — the physical unit attached to the definition.

### `Primitive` types

`Primitive` covers the types natively supported by Python and NumPy (`int`, `float`, `complex`,
`str`, `bool`).

- `_dtype` holds the concrete Python or NumPy dtype, e.g. `np.int32`, `np.float64`, `bool`, `str`.
- `_np_base` holds the base type class (`np.integer`, `np.inexact`, `np.bool_`, `np.str_`), which
  decides whether normalized array output stays a NumPy array or becomes a Python list.

The concrete primitives are:

- `Number` (abstract) — the base for numeric types.
    - `ExactNumber` — integer types, implemented by `m_int` and `m_int8`, `m_int16`, `m_int32`, `m_int64`.
    - `InexactNumber` — floating-point and complex types, implemented by `m_float` (`m_float16`,
      `m_float32`, `m_float64`) and `m_complex` (`m_complex128`).
- `m_bool` — boolean values (`bool` or `np.bool_`).
- `m_str` — string values (`str` or `np.str_`).

### `NonPrimitive` types

`NonPrimitive` is the base for rich domain-specific types. Unlike primitives, these perform
element-wise operations through the template methods `_normalize_impl()` and `_serialize_impl()`.

- `Datetime` — converts strings (via `dateutil`), Unix timestamps, `date`, `pd.Timestamp` or
  `np.datetime64` into UTC-aware `datetime.datetime`. Serializes to ISO 8601.
- `Unit` — converts unit strings or `pint.Quantity` objects to `pint.Unit`, validating dimensionality
  with `check_dimensionality`.
- `Enum` — string enumerations with a fixed set of allowed values and optional descriptions
  (`m_descriptions`).
- `JSON` — validates dictionary input and standardizes key-value structures using `orjson`.
- `Bytes` — raw byte strings or base64-encoded ASCII.
- `URL` and `File` — validate URLs and file paths relative to a NOMAD archive.
- `Capitalized` — coerces strings with `value.capitalize()`.
- `Dimension` — matrix or tensor dimension bounds, as integers or dimension symbols.
- `Callable` — validates callable objects and an optional argument count (`nargs`).
- `Any` — a transparent pass-through.

`Reference` and `QuantityReference` handle typed cross-references between sections and quantities.
You will rarely need to touch them directly — see
{{ nav_link("howto/schemas/define.md", breadcrumb=True) }}.

## `normalize(value, **kwargs)`

`normalize()` turns raw, unstructured or parsed input into a valid, strongly-typed internal
representation. All validation and conversion happens here.

!!! warning "Attention"
    The value you return must be valid and comply with the definition. No further checks are
    performed, and the rest of the system assumes only valid data.

The parent section holding the destination data is available through `kwargs`, as
`section=kwargs.get('section')`, when you need to interact with the container.

### Normalization pipeline for primitives

- **Unit and magnitude extraction** — if `value` is a `pint.Quantity`, its magnitude is extracted with
  `extract_magnitude`, after converting to the definition's unit when one is configured.
- **Scalar normalization** — checks the input type against `_dtype`; raises `ValueError` if
  auto-conversion is disabled and the types differ; checks `convertible_from()`; attempts a safe
  conversion or a close numeric comparison with `np.isclose`.
- **Array normalization** — converts input (`pd.DataFrame`, `pd.Series`, `list`, `tuple`,
  `np.ndarray`) to a NumPy array; casts with `array.astype(self._dtype, casting='safe')`; converts
  back to Python lists when `_dtype` is a pure Python type; applies `_check_shape()`.

Validation deliberately uses safe conversion so that no data loss can occur, even though everything
is eventually stored in a JSON-compatible format.

### Normalization pipeline for non-primitives

- Enforces 1D or scalar shape constraints via `_check_shape()`.
- Iterates over elements for lists, or calls `_normalize_impl(value, **kwargs)` directly for scalars.

## `serialize(value, **kwargs)`

`serialize()` converts valid runtime values — NumPy arrays, `datetime` objects, `pint.Unit` objects —
into JSON-serializable structures.

- **Transform hooks** — an optional `transform(val, path)` callback allows recursive transformation of
  array elements and scalar fields during serialization.
- **Primitive serialization** — NumPy arrays become lists via `tolist()`, scalar generics become
  Python primitives via `item()`.
- **Non-primitive serialization** — delegates element-wise conversion to `_serialize_impl()`. For
  example `Datetime` calls `isoformat()`, `Unit` returns `str(value)`, and `Bytes` encodes to base64.

## `serialize_self()`

`serialize_self()` serializes the metadata of the `Datatype` object itself into a dictionary with
`type_kind`, `type_data` and the active flags. It is used when serializing the schema. For `m_int32`
it produces:

```python
{'type_kind': 'numpy', 'type_data': 'int32', 'disable_shape_check': False}
```

## Register the type

`normalize_type()` is the factory that turns a shorthand type declaration into a `Datatype` instance.
Add your string aliases there. The accepted spellings it already supports are listed in
{{ nav_link("reference/metainfo.md", breadcrumb=True) }}.
