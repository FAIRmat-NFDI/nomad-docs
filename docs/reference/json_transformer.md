# JSON transformer

This page lists the fields of transformation rules and rule sets, and the arguments of the `Transformer` class from `nomad.utils.json_transformer`. For examples, see {{ nav_link("howto/manage/program/json_transformer.md") }}.

## Rules

{{ pydantic_model('nomad.datamodel.metainfo.annotations.Rule', heading='### Rule') }}

{{ pydantic_model('nomad.datamodel.metainfo.annotations.Rules', heading='### Rules') }}

## Transformer

### `transform()`

| Argument         | Description                                                                                               |
| ---------------- | --------------------------------------------------------------------------------------------------------- |
| `source_data`    | The data to transform. It is never modified.                                                              |
| `mapping_name`   | Name of the rule set to apply. Optional if there is only one, or one named `default`.                     |
| `target_data`    | Existing data to write the targets into. It is modified directly. Not supported for sequential rule sets. |
| `inplace`        | If true, write the targets into a copy of the source data.                                                |
| `delete_sources` | If true, delete the transferred sources from the result.                                                  |
| `update_mode`    | Default `update_mode` for rules that neither define one nor inherit one from the rule set.                |

### `Transformer.map()`

`Transformer.map()` accepts `target_data`, `inplace`, `delete_sources` and `update_mode` like `transform()`. To define the transformation, pass the fields of a single rule (`source`, `target`, `default_value`, `conditions`, `use_rule`, `update_mode`, `action`), or `rule` or `rules` for an existing rule or rule set.
