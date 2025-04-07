# Transform JSON Data Structures with Transformer

## Who is this how-to guide for?

This guide is designed for mid-level NOMAD users who need to parse JSON-formatted data structures into another JSON
format. An example use case is transforming an external API response, partially or wholly, onto a NOMAD archive in a
standardized format. This document will cover the basic principles and common applications of the JsonToJson Transformer
from
the `nomad-lab` package.

## What should you know before this how-to guide?

Before diving into this guide, you should be familiar with the following:

- A basic understanding of the `nomad-lab` package. Follow the [How to install nomad-lab](pythonlib.md) guide

## What you will know at the end of this how-to guide?

By the end of this how-to guide, you will:

- Understand how to use the `Transformer` class to transform JSON data structures.
- Be able to apply transformation rules to transform data from one format to another.
- Learn how to customize and extend data conversion rules for specific needs.


## Steps

### 1. Define Your Transformation Rules

Create a Python file and define the rules that specify how to transform your JSON data. These rules dictate where to
source
data in the input JSON and where and how to place it in the output JSON. Set the following JSON data to a
variable `json_example` and create rules as:

```json
--8<-- "examples/data/json_transformer/basic_transformation.json"
```

Use this script to load the rules:

```python
from nomad.datamodel.metainfo.annotations import Rules

rules = {
    "example_transformation": Rules(
        json_example['schema']
    )
}
```

### 2. Initialize the Transformer

In your Python script, initialize the `Transformer` with the rules you defined.

```python
from nomad.utils.json_transformer import Transformer

transformer = Transformer(rules)
```

### 3. Prepare Your Source JSON

Prepare the JSON data that needs to be transformed. This data can come from files, API responses, or other sources. Here
we are reading from the `json_example` from above:

```python
source_json = json_example['data']
```

### 4. Transform the Data

Use the `transform` method of your transformer instance to apply the transformation rules to your source JSON.

```python
transformed_json = transformer.transform(source_json, "example_transformation")
print(transformed_json)
```

this should produce:

```json
{
  "a": 1,
  "b": 2
}
```

## Advanced Usage of JsonToJson Transformer

### Handling Complex JSON Transformations

In more complex scenarios, you may need to handle nested JSON structures, apply conditional logic, or resolve
references. This section will guide you through using advanced features of the `Transformer` class to address these
challenges.

### Prerequisites

Before proceeding, it is better to have read the basic instructions explained above as it contains information on how
to load the transformer.

### Complex Rules Definition

In more sophisticated environments, transformation rules may require the evaluation of conditions, the manipulation of
lists, or the resolution of nested structures. Below are examples of such advanced usage:

### Conditional Copy Based on Regex

You can use regular expressions to conditionally copy data based on pattern matching. This is useful when you need to
filter or format data before placing it in the target JSON.

```json
--8<-- "examples/data/json_transformer/conditional_transformation_met.json"
```

```python
transformer = Transformer(mapping_dict=rules)

transformed_json = transformer.transform(source_json, "conditional_transformation_met")
print(transformed_json)
```

The rule checks if the value at path "a" matches the regex pattern (i.e., starts with '3' followed by any digit).
If the condition is not met, the target "age" is set to "default_age".

this should produce:

```json
{
  "a": 30
}
```

### Resolving References

When dealing with complex data structures, it might be necessary to use the structure of another `rule` defined in a
different part of the transformation. For this you can set the `reference` value to the path of your interest (keep in
mind that this path should be started with `#` sign).

!!! important

    The referenced rule's values will be overwritten by the local rule; meaning you can partly import the referenced rule and overwrite other fields onto your desired values.

```python
source_json = {
    "users": [
        {"name": "user_1", "role": "manager", "manager_id": "101"},
        {"name": "user_2", "role": "employee", "manager_id": "102"},
        {"name": "user_3", "role": "manager", "manager_id": "103"}
    ],
    "details": [
        {"id": "101", "name": "user_4", "department": "A"},
        {"id": "102", "name": "user_5", "department": "B"},
        {"id": "103", "name": "user_6", "department": "C"}
    ]
}

rules = {
    "employee_info": Rules(
        name="Employee Info Mapping",
        rules={
            "rule_manager": Rule(
                source="users[?role=='manager'].manager_id | [0]",
                target="manager_details",
                use_rule="#employee_info.details"
            ),
            "details": Rule(
                source="details[?id=='101'] | [0]",
                target="specific_manager"
            )
        }
    )
}
```

In this example, the first item in the `rule` list, is a reference to the second item in the list. This setup extracts
manager details a specific manager from the list.

## Implementing Advanced Transformations

### Nested Structure Manipulation

You can manipulate nested structures by specifying deeper paths and using lists or dictionaries as intermediary storage.

```json
--8<-- "examples/data/json_transformer/nested_transformation.json"
```

The Transformer can handle deeply nested JSON structures. Define rules that navigate through nested paths to extract or
set data.
