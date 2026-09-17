# How to add a new type

Adding a custom type involves subclassing either `NonPrimitive` (for custom objects/strings) or `Primitive` (for scalar/array types), implementing required serialization and normalization methods, and registering the type in `normalize_type()`.

The following checklist can be used.

- Step 1: Subclass `NonPrimitive` or `Primitive`: Inherit from `NonPrimitive` if your custom type operates on individual scalar values or 1D lists.
- Step 2: Implement `_normalize_impl(self, value, **kwargs)`: Define input validation and parsing logic. Convert valid inputs into your canonical runtime object representation, or raise `TypeError`/`ValueError` if validation fails.
- Step 3: Implement `_serialize_impl(self, value, **kwargs)`: Define how the canonical runtime object converts into a JSON-serializable structure (e.g., string, dict, int).
- Step 4: Implement `standard_type(self)` and `serialize_self()`: Specify the generic Python type name (used by schema mappers) and self-serialization metadata dictionary.
- Step 5: Register in `normalize_type()`: Add string lookup aliases for your new type inside `normalize_type()`.
