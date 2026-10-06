# How to transform JSON data structures

## Who is this how-to guide for?

This guide is designed for developers and data managers who need to parse, migrate, or normalize JSON-formatted data structures into another JSON format. A common NOMAD use case is transforming an external API response, or migrating legacy archives and repeating subsections onto modern NOMAD schema definitions (such as adding `m_def` annotations).

This document covers the principles, shortcuts, and advanced features of the `Transformer` class from `nomad.utils.json_transformer`.

## What should you know before this how-to guide?

Before diving into this guide, you should be familiar with the following:

- A basic understanding of Python dictionaries and lists.
- The `nomad-lab` package. Follow the [How to install NOMAD Python library](../../../howto/oasis/install.md#how-to-install-the-nomad-python-library) guide.

## What you will know at the end of this how-to guide?

By the end of this how-to guide, you will:

- Know how to quickly map JSON fields with minimal boilerplate using `Transformer.map`.
- Understand how to initialize `Transformer` with simple keyword arguments, dictionaries, or `Rules` objects.
- Learn how to transform lists and repeating subsections using **array rules** (`[n]`, `[n1]`, `[*]`).
- Know how to populate **default values across array elements** (e.g. adding missing `m_def` annotations).
- Know how to **merge into existing data** with `update_mode` instead of replacing it.
- Know how to apply rules **step by step** and **clean up** the result with delete rules.
- Use conditional logic (regex evaluation) and rule references (`use_rule`) for complex workflows.

---

## Quick Start: Minimal Mapping

If you only need to transform or copy a few fields, you do not need to construct verbose `Rules` or configuration dictionaries.

### 1. One-Liner with `Transformer.map`

Use the `Transformer.map(...)` classmethod to apply a mapping in a single line:

```python
from nomad.utils.json_transformer import Transformer

data = {'user': {'first_name': 'Alice', 'last_name': 'Smith'}, 'age': 30}

# Map a single field
result = Transformer.map(data, source='user.first_name', target='profile.name')
# Output: {"profile": {"name": "Alice"}}

# Set a default value directly
result = Transformer.map(data, target='version', default_value='1.0')
# Output: {"version": "1.0"}
```

By default, the result only contains the targets. Pass `inplace=True` to write the targets into a copy of the input instead, or pass an existing `target_data` dictionary:

```python
# Returns a copy of data with the target added, data itself is not modified
result = Transformer.map(data, source='user.last_name', target='surname', inplace=True)
# Output: {"user": {"first_name": "Alice", "last_name": "Smith"}, "age": 30, "surname": "Smith"}
```

Values are copied into the result, so modifying the result never changes the input data. Only a `target_data` that you pass is modified directly.

### 2. Shorthand Initializations

`Transformer` accepts multiple input formats to fit your preferred style:

=== "Keyword arguments"

    ```python
    transformer = Transformer(source='a.b', target='c.d')
    result = transformer.transform(data)
    ```

=== "Single Rule Dictionary"

    ```python
    transformer = Transformer({'source': 'a.b', 'target': 'c.d', 'default_value': 0})
    result = transformer.transform(data)
    ```

=== "List of Rules"

    ```python
    transformer = Transformer([
        {'source': 'input.x', 'target': 'output.x'},
        {'source': 'input.y', 'target': 'output.y'},
    ])
    result = transformer.transform(data)
    ```

=== "Rules Dictionary"

    ```python
    transformer = Transformer({
        'rules': {
            'copy_x': {'source': 'input.x', 'target': 'output.x'},
            'copy_y': {'source': 'input.y', 'target': 'output.y'},
        }
    })
    result = transformer.transform(data)
    ```

When using any of the shorthands above, you can simply call `transformer.transform(data)` without specifying a mapping name.

---

## Standard Usage: Named Transformation Rules

For modular or multi-rule migrations, you can define named rule groups using `nomad.datamodel.metainfo.annotations.Rules` and `Rule`.

### 1. Define Your Transformation Rules

Set the following JSON schema and data to a variable `json_example`:

```json
--8<-- "examples/data/json_transformer/basic_transformation.json"
```

Load the rules:

```python
from nomad.datamodel.metainfo.annotations import Rules
from nomad.utils.json_transformer import Transformer

rules = {'example_transformation': Rules(json_example['schema'])}
transformer = Transformer(rules)
```

### 2. Transform the Data

Pass your source JSON and the rule group name to `transform()`:

```python
source_json = json_example['data']
transformed_json = transformer.transform(source_json, 'example_transformation')
print(transformed_json)
```

Output:

```json
{
  "a": 1,
  "b": 2
}
```

---

## Working with Arrays and Repeating Structures

NOMAD archives often contain repeating lists of items, such as subsections, measurements, or calculation steps. The `Transformer` supports array notation to extract, transform, or populate values across all items in a list.

### 1. Array Index Placeholders (`[n]`, `[n1]`, `[n2]`, ...)

Use placeholders such as `[n]`, `[n1]`, or `[n2]` to indicate repeating array elements. `Transformer` automatically detects array syntax and iterates through all matching list elements:

```json
--8<-- "examples/data/json_transformer/array_transformation.json"
```

```python
from nomad.datamodel.metainfo.annotations import Rules
from nomad.utils.json_transformer import Transformer

rules = {'subsystem_migration': Rules(json_example['schema'])}
transformer = Transformer(rules)

source_json = json_example['data']
result = transformer.transform(source_json, 'subsystem_migration')
print(result)
```

Output:

```json
{
  "sub_systems": [
    {
      "label": "system_1",
      "nested_system": {
        "m_def": "nomad.datamodel.metainfo.basesections.v2.Element"
      }
    },
    {
      "label": "system_2",
      "nested_system": {
        "m_def": "nomad.datamodel.metainfo.basesections.v2.Element"
      }
    }
  ]
}
```

!!! tip "Automatic Array Rule Detection"

    `Transformer` automatically inspects rule paths for array patterns like `[n]`. Setting `array_rules=True` explicitly in `transformer.transform(data, array_rules=True)` is supported for backward compatibility, but is no longer mandatory when array placeholders are present.

### 2. Populating `default_value` Across Repeating Items

A common migration requirement is adding a missing field (such as a Metainfo definition `m_def`) to all items in an array:

```python
rule = {
    'target': 'sub_systems[n1].nested_system.m_def',
    'default_value': 'nomad.datamodel.metainfo.basesections.v2.Element',
}

# Apply to all items in sub_systems
Transformer.map(archive_dict, rule=rule, inplace=True)
```

Notice that:

- The rule does not require a `source` path.
- The `Transformer` iterates through each existing item in `sub_systems`, creating any intermediate dictionaries (such as `nested_system` if missing), and writes the `default_value`.
- If a `source` is provided but does not exist in some elements, the `default_value` is safely used as the fallback for those elements.

### 3. Wildcard Target Notation (`[*]`)

When the target path in your destination data structure is already a list, you can use the wildcard `[*]` notation to fill every element with a default value:

```python
target_data = {'items': [{}, {}, {}]}

Transformer.map(
    target_data,
    target='items[*].status',
    default_value='pending',
    inplace=True,
)
# Result: {"items": [{"status": "pending"}, {"status": "pending"}, {"status": "pending"}]}
```

!!! note "Wildcards only apply to lists"

    `[*]` iterates over list elements, not over the keys of a dictionary. A target such as `data.[*]` raises a `ValueError`. To move all keys of a section into another section, target the section itself and use an `update_mode`, see [Merging into Existing Data](#merging-into-existing-data).

### 4. Conditional Rules in Arrays

When applying conditions to repeating elements, you can use the array placeholder in the condition's `regex_path`. The placeholder dynamically resolves to the corresponding item's index:

```python
from nomad.datamodel.metainfo.annotations import Condition, RegexCondition, Rule

rule = Rule(
    target='elements[n1].category',
    default_value='Transition Metal',
    conditions=[
        Condition(
            regex_condition=RegexCondition(
                regex_path='elements[n1].symbol',
                regex_pattern='^(Fe|Co|Ni|Cu)$',
            )
        )
    ],
)
```

Only elements matching the condition will receive the target assignment.

---

## Merging into Existing Data

By default, a rule replaces whatever already exists at its target. Set `update_mode` to merge the value into the existing target instead:

| `update_mode`       | Fields only in the target | Fields in both      | Lists              |
| ------------------- | ------------------------- | ------------------- | ------------------ |
| `replace` (default) | removed                   | new value           | replaced           |
| `overwrite`         | kept                      | new value wins      | replaced           |
| `extend`            | kept                      | existing value wins | new items appended |

`overwrite` and `extend` merge nested dictionaries recursively. If the existing value or the new value is not a dictionary, `replace` and `overwrite` both write the new value, while `extend` keeps the existing one.

### 1. Moving a Section into Its Parent

A common migration step is moving all fields of a subsection into its parent section without listing every field. The following moves the content of `pure_substance` into `data`:

```python
data = {
    'data': {
        'name': 'water',
        'formula': 'old',
        'tags': ['a'],
        'pure_substance': {'formula': 'H2O', 'mass': 18.02, 'tags': ['b']},
    }
}

result = Transformer.map(
    data,
    source='data.pure_substance',
    target='data',
    update_mode='overwrite',
    delete_sources=True,
    inplace=True,
)
```

Output, depending on `update_mode`:

=== "replace"

    ```json
    {"data": {"formula": "H2O", "mass": 18.02, "tags": ["b"]}}
    ```

    Everything else in `data`, such as `name`, is lost.

=== "overwrite"

    ```json
    {"data": {"name": "water", "formula": "H2O", "tags": ["b"], "mass": 18.02}}
    ```

=== "extend"

    ```json
    {"data": {"name": "water", "formula": "old", "tags": ["a", "b"], "mass": 18.02}}
    ```

### 2. Setting a Default for All Rules

Instead of setting `update_mode` on every rule, set it once for the whole rule set. A rule's own `update_mode` takes precedence:

```python
rules = {
    'update_mode': 'extend',
    'rules': {
        'move_pure_substance': {'source': 'data.pure_substance', 'target': 'data'},
        'move_label': {
            'source': 'data.label',
            'target': 'data.name',
            'update_mode': 'overwrite',
        },
    },
}
```

The same works with `Rules(update_mode='extend', rules={...})`. The update mode of a rule is determined in the following order:

1. The rule's own `update_mode`.
2. The `update_mode` of the rule set.
3. The `update_mode` argument of `transform()` or `Transformer.map()`. This is useful to set a default without editing a rules file.
4. `replace`.

### 3. Combining Several Sources into One Target

Rules are applied in order, so several rules can write into the same target. The first rule creates the target, the following rules merge into it:

```python
transformer = Transformer({
    'rules': {
        'move_a': {'source': 'a', 'target': 'b'},
        'move_c': {'source': 'c', 'target': 'b', 'update_mode': 'extend'},
    }
})
result = transformer.transform(
    {'a': {'x': 1, 'l': [1]}, 'c': {'x': 2, 'y': 2, 'l': [2]}},
    inplace=True,
    delete_sources=True,
)
# Output: {"b": {"x": 1, "l": [1, 2], "y": 2}}
```

!!! warning "Use unique rule names"

    Rules are stored in a dictionary. If two rules have the same name, only the last one is applied.

### 4. Writing to the Root

Use an empty `target` to write to the root of the target data:

```python
result = Transformer.map(
    {'k': 0, 'metadata': {'author': 'Alice', 'year': 2024}},
    source='metadata',
    target='',
    update_mode='overwrite',
    delete_sources=True,
    inplace=True,
)
# Output: {"k": 0, "author": "Alice", "year": 2024}
```

With the default `replace`, the root is replaced entirely, so all other data is lost. The value must be of the same type as the root, usually a dictionary, otherwise a `TypeError` is raised.

### 5. Merging into Repeating Subsections

`update_mode` works with array placeholders. The following moves each element of `elemental_composition` into the `nested_system` of the corresponding `sub_system`, keeping the existing `m_def`:

```python
data = {
    'data': {
        'elemental_composition': [
            {'element': 'H', 'atomic_fraction': 0.67},
            {'element': 'O', 'atomic_fraction': 0.33},
        ],
        'sub_system': [
            {'label': 'hydrogen', 'nested_system': {'m_def': 'Element'}},
            {'label': 'oxygen'},
        ],
    }
}

result = Transformer.map(
    data,
    source='data.elemental_composition[n1]',
    target='data.sub_system[n1].nested_system',
    update_mode='overwrite',
    delete_sources=True,
    inplace=True,
)
```

Output:

```json
{
  "data": {
    "elemental_composition": [],
    "sub_system": [
      {
        "label": "hydrogen",
        "nested_system": {"m_def": "Element", "element": "H", "atomic_fraction": 0.67}
      },
      {
        "label": "oxygen",
        "nested_system": {"element": "O", "atomic_fraction": 0.33}
      }
    ]
  }
}
```

With `extend`, a `default_value` is only written where the target does not exist yet. This is useful to add a missing `m_def` without changing existing ones:

```python
result = Transformer.map(
    {'sub_systems': [{'nested_system': {'m_def': 'Custom'}}, {'nested_system': {}}]},
    target='sub_systems[n1].nested_system.m_def',
    default_value='Element',
    update_mode='extend',
    inplace=True,
)
# Output: {"sub_systems": [{"nested_system": {"m_def": "Custom"}}, {"nested_system": {"m_def": "Element"}}]}
```

!!! warning "`extend` with `delete_sources`"

    With `extend`, values that conflict with existing fields are not written. If you also set `delete_sources=True`, the source is still deleted, so these values are lost.

---

## Step-by-Step Transformations

### 1. Sequential Rule Sets

By default, every rule reads from the original source data, so a rule cannot see what previous rules wrote. Set `sequential` on the rule set to apply the rules one after another to a single document. Each rule then reads from the result of the previous rules:

```python
rules = {
    'sequential': True,
    'rules': {
        'step1': {'source': 'a', 'target': 'b'},
        'step2': {'source': 'b.x', 'target': 'c'},  # reads the 'b' written by step1
    },
}
result = Transformer(rules).transform({'a': {'x': 1}})
# Output: {"a": {"x": 1}, "b": {"x": 1}, "c": 1}
```

Without `sequential`, `step2` finds no `b` in the source and `c` is not written.

Sequential rule sets always work on a copy of the source data, which itself is not modified. The result therefore contains all source data, as with `inplace=True`, and passing a separate `target_data` raises a `ValueError`.

With `delete_sources=True`, the sources of each rule are deleted right after the rule is applied. This allows a later rule to write to a path that an earlier rule moved away:

```python
rules = {
    'sequential': True,
    'rules': {
        'move_a': {'source': 'a', 'target': 'b'},
        'move_c': {'source': 'c', 'target': 'a'},
    },
}
result = Transformer(rules).transform({'a': 1, 'c': 2}, delete_sources=True)
# Output: {"b": 1, "a": 2}
```

### 2. Cleaning Up the Target

A rule with `"action": "delete"` deletes its `target` from the target data. Since rules are applied in order, delete rules at the end of a rule set clean up the result after all other rules have been applied:

```python
rules = {
    'sequential': True,
    'update_mode': 'overwrite',
    'rules': {
        'merge_substance': {'source': 'data.pure_substance', 'target': 'data'},
        'merge_composition': {
            'source': 'data.elemental_composition[n1]',
            'target': 'data.sub_system[n1].nested_system',
        },
        'set_m_def': {
            'target': 'data.sub_system[n1].nested_system.m_def',
            'default_value': 'Element',
            'update_mode': 'extend',
        },
        'drop_tmp': {'target': 'data.sub_system[n1].tmp', 'action': 'delete'},
    },
}
result = Transformer(rules).transform(archive, delete_sources=True)
```

Notice that:

- Array placeholders (`[n]`, `[n1]`, `[*]`) are resolved against the target data, so `data.sub_system[n1].tmp` is deleted in every element of `sub_system`.
- Paths that do not exist are ignored.
- A delete rule only defines `target` and `action`. Combining it with `source`, `default_value`, `update_mode` or `conditions` raises a validation error.
- Delete rules always act on the target data. Without `sequential` or `inplace`, the target only contains what the previous rules wrote, and the source data is never modified.

For a single deletion, use `Transformer.map`:

```python
result = Transformer.map(data, target='sub_systems[n].tmp', action='delete', inplace=True)
```

### 3. Deleting Paths from Python

If you post-process the result of `transform()` in Python, use `Transformer.delete_path`. It modifies the data in place, supports the same array placeholders and returns the data:

```python
result = transformer.transform(data)
Transformer.delete_path(result, 'sub_systems[n].tmp')
```

---

## Advanced Features

### 1. Conditional Copy Based on Regex

You can use regular expressions to evaluate input values before copying.

```json
--8<-- "examples/data/json_transformer/conditional_transformation_met.json"
```

```python
transformer = Transformer(mapping_dict=rules)
transformed_json = transformer.transform(source_json, 'conditional_transformation_met')
print(transformed_json)
```

The rule checks if the value at path `"a"` matches `"^3\\d$"`. If the condition is met, the value is copied to `"age"`. If not met, `"default_value"` is applied.

### 2. Resolving References (`use_rule`)

When mapping related entities, a rule can inherit or reference another rule by setting `use_rule` to a path starting with `#`:

```python
from nomad.datamodel.metainfo.annotations import Rule, Rules

rules = {
    'employee_info': Rules(
        name='Employee Info Mapping',
        rules={
            'rule_manager': Rule(
                source="users[?role=='manager'].manager_id | [0]",
                target='manager_details',
                use_rule='#employee_info.details',
            ),
            'details': Rule(
                source="details[?id=='101'] | [0]",
                target='specific_manager',
            ),
        },
    )
}
```

!!! important "Rule Overwriting"

    Fields set on the referenced rule overwrite the fields of the local rule. Fields that are not set on the referenced rule, such as `update_mode` or `default_value`, are taken from the local rule. This allows you to reuse shared mapping structures and only fill in the missing attributes locally.

### 3. Nested Structure Manipulation & JMESPath

`Transformer` paths support standard dot notation for nesting as well as JMESPath expressions on source paths (such as filters `[?condition]` and projections `[*]`):

```json
--8<-- "examples/data/json_transformer/nested_transformation.json"
```

```python
# Deeply nested extraction
Transformer.map(data, source='f.nested.key', target='flattened_key')
```

### 4. Deleting Source Keys

To remove the transferred source fields from the result (useful during dictionary cleanup or migration):

```python
Transformer.map(
    data, source='old_field', target='new_field', delete_sources=True, inplace=True
)
```

Only sources whose value was actually transferred are deleted:

- Array placeholders are resolved, so `items[n]` deletes every transferred element of `items`. The emptied list itself is kept.
- Sources of rules whose conditions are not met are kept.
- A source is kept if its target lies inside it (for example `source='a'`, `target='a.copy'`), since deleting it would also delete the transferred data.
- Sources are deleted from the result, the data passed to `transform()` is not modified. Without `inplace=True` or `sequential`, the result does not contain the sources in the first place.
- Sources are deleted after all rules have been applied, or after each rule for [sequential rule sets](#1-sequential-rule-sets).

---

## Reference

### Rule fields

| Field           | Description                                                                                                                         |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `source`        | JMESPath to the value in the source data. Supports array placeholders such as `[n1]`.                                               |
| `target`        | Path to write to in the target data. Supports array placeholders. Use `''` for the root.                                            |
| `default_value` | Value to write if the source does not exist or no `source` is given.                                                                |
| `conditions`    | Regex conditions that must be met to apply the rule.                                                                                |
| `use_rule`      | Reference to another rule, `#<rule_set>.<rule>`, whose set fields overwrite the local ones.                                         |
| `update_mode`   | `replace` (default), `overwrite` or `extend`. See [Merging into Existing Data](#merging-into-existing-data).                         |
| `action`        | `set` (default) or `delete`. See [Cleaning Up the Target](#2-cleaning-up-the-target).                                               |

### Rule set fields

| Field         | Description                                                                                                   |
| ------------- | ------------------------------------------------------------------------------------------------------------- |
| `rules`       | Dictionary of named rules, applied in order.                                                                  |
| `name`        | Name of the rule set.                                                                                         |
| `update_mode` | Default `update_mode` for all rules that do not define their own.                                             |
| `sequential`  | If true, each rule reads from the result of the previous rules. See [Sequential Rule Sets](#1-sequential-rule-sets). |

### `transform()` arguments

| Argument         | Description                                                                                                      |
| ---------------- | ---------------------------------------------------------------------------------------------------------------- |
| `source_data`    | The data to transform. It is never modified.                                                                     |
| `mapping_name`   | Name of the rule set to apply. Optional if there is only one, or one named `default`.                            |
| `target_data`    | Existing data to write the targets into. It is modified directly. Not supported for sequential rule sets.        |
| `inplace`        | If true, write the targets into a copy of the source data.                                                       |
| `delete_sources` | If true, delete the transferred sources from the result. See [Deleting Source Keys](#4-deleting-source-keys).    |
| `update_mode`    | Default `update_mode` for rules that neither define one nor inherit one from the rule set.                       |

`Transformer.map()` accepts `target_data`, `inplace`, `delete_sources` and `update_mode` as well. To define the transformation, pass the rule fields (`source`, `target`, `default_value`, `conditions`, `use_rule`, `update_mode`, `action`) for a single rule, or `rule` or `rules` for an existing rule or rule set.
