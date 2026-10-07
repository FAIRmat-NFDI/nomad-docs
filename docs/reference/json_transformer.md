# JSON transformer

This page lists the fields used to define JSON transformation rules and the
arguments accepted by the `Transformer` methods from
`nomad.utils.json_transformer`.

## Rule models

### `Rule`

| Field | Description |
| --- | --- |
| `source` | JMESPath to the value in the source data. Supports array placeholders such as `[n1]`. |
| `target` | Path to write to in the target data. Supports array placeholders. An empty string targets the root. |
| `conditions` | Regular-expression conditions that must be satisfied before applying the rule. |
| `default_value` | Value to write when the source does not exist or the rule does not define a source. |
| `use_rule` | Reference in the form `#<rule-set>.<rule>` to another rule whose defined fields should be reused. |
| `update_mode` | How to combine the value with an existing target: `replace` (default), `overwrite`, or `extend`. |
| `action` | Action to perform: `set` (default) or `delete`. |

### `Rules`

| Field | Description |
| --- | --- |
| `name` | Optional name of the rule set. |
| `other_metadata` | Optional additional metadata associated with the rule set. |
| `rules` | Dictionary of named `Rule` objects, applied in their defined order. |
| `update_mode` | Default update mode for rules that do not define their own. |
| `sequential` | If `True`, each rule reads from the result produced by the preceding rules. |

## Transformer methods

### `transform()`

| Argument | Description |
| --- | --- |
| `source_data` | Data to transform. The method does not modify this object. |
| `mapping_name` | Name of the rule set to apply. Optional when the transformer contains only one rule set or one named `default`. |
| `target_data` | Existing data to write into. The method modifies this object directly. Sequential rule sets do not support it. |
| `inplace` | If `True`, start from a copy of `source_data` and write the targets into that copy. |
| `array_rules` | If `True`, resolve rules as array rules. Array placeholders are otherwise detected automatically. |
| `delete_sources` | If `True`, remove successfully transferred source paths from the result. |
| `source` | Source path for a direct, single-rule transformation. Use it together with `target`. |
| `target` | Target path for a direct, single-rule transformation. An empty string targets the root. |
| `default_value` | Value to use when the direct rule has no source value. |
| `conditions` | Conditions that must be satisfied before applying the direct rule. |
| `rule` | Existing `Rule` object or rule dictionary to apply directly. |
| `update_mode` | Update mode for a direct rule, or the default for rules that do not define or inherit one. |
| `action` | Action for a direct rule: `set` or `delete`. |

### `Transformer.map()`

| Argument | Description |
| --- | --- |
| `data` | Data to transform. |
| `source` | Source path for a single rule. |
| `target` | Target path for a single rule. An empty string targets the root. |
| `default_value` | Value to use when the rule has no source value. |
| `conditions` | Conditions that must be satisfied before applying the rule. |
| `use_rule` | Reference to another rule whose fields should be reused. |
| `rule` | Existing `Rule` object or rule dictionary to apply. |
| `rules` | Existing `Rules` object, rule-set dictionary, or list of rules to apply. |
| `target_data` | Existing data to write into. The method modifies this object directly. |
| `inplace` | If `True`, start from a copy of `data` and write the targets into that copy. |
| `delete_sources` | If `True`, remove successfully transferred source paths from the result. |
| `update_mode` | Update mode for a single rule, or the default for rules that do not define or inherit one. |
| `action` | Action for a single rule: `set` or `delete`. |

## Related pages

- {{ nav_link("howto/manage/program/json_transformer.md", breadcrumb=True) }}
