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

You can also pass `inplace=True` to modify the input dictionary directly, or pass an existing `target_data` dictionary:

```python
# Modifies data in-place
Transformer.map(data, source='user.last_name', target='surname', inplace=True)
```

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

    The referenced rule's fields are overwritten by the local rule. This allows you to import shared mapping structures and override only specific attributes.

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

To remove source fields from the original structure after copying (useful during dictionary cleanup or migration):

```python
Transformer.map(
    data, source='old_field', target='new_field', delete_sources=True, inplace=True
)
```
