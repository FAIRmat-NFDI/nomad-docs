# Configuration

## Introduction

Many aspects of NOMAD and its operation can be modified through configuration. Most
configuration items have reasonable defaults and typically only a small subset has to be
overwritten.

Configuration items get their value based on a clear hierarchy of sources. The sources are applied in the following order of precedence, where later sources override earlier ones:

1.  **Environment Variables:** A variable like `NOMAD_SERVICES_API_HOST`. These have the highest priority and will override all other settings.
2.  **Command-Line Configuration Files:** Files passed via the `-f` or `--config-file` flag to the NOMAD CLI. If multiple files are given, they are merged in order, with later files overriding earlier ones.
3.  **Default `nomad.yaml`:** A file named `nomad.yaml` in the current working directory, or a file pointed to by the `NOMAD_CONFIG` environment variable. This serves as the base configuration.
4.  **Built-in Defaults:** The default values hard-coded in the NOMAD source code. These have the lowest priority.

Configuration items are structured hierarchically. For example, the configuration item `services.api_host` denotes the attribute `api_host` in the configuration section `services`.

### Setting values from the environment

NOMAD services will inspect the environment for any variables starting with `NOMAD_`. The rest of the name is interpreted as a configuration item, where sections and attributes are concatenated with a `_`.
For example, the environment variable `NOMAD_SERVICES_API_HOST` will set the value for the `api_host` attribute in the `services` section.

#### Setting values from YAML files

NOMAD uses YAML files for file-based configuration. The system looks for files in the following order:

1.  **Default Base File:** NOMAD first looks for a file named `nomad.yaml` in the current working directory. You can specify a different location for this base file by setting the `NOMAD_CONFIG` environment variable. This file is always loaded first if it exists.

2.  **Override Files (CLI only):** When using the NOMAD command-line interface (CLI), you can specify one or more additional configuration files using the `-f` (or `--config-file`) flag. These files are merged in the order they are provided, with values from later files overriding values from earlier ones. All override files are applied *on top of* the default `nomad.yaml`.

    For example, you could have a specific configuration for a certain plugin:
    ```bash
    nomad admin run appworker -f plugin-config.yaml
    ```
    Or layer multiple configurations:
    ```bash
    nomad admin run appworker -f temporal-config.yaml -f plugin-config.yaml
    ```

An example `nomad.yaml` file:
```yaml
--8<-- "ops/docker-compose/nomad-oasis/configs/nomad.yaml"
```

#### Merging Rules

When configuration is loaded from multiple sources (e.g., a default file and an override file), the values are merged according to the following rules:

-   **Objects (Dictionaries):** When overwriting an *object*, the new value is recursively merged with the existing value. The final merged object will have all attributes from the new object, plus any attributes from the old object that were not overwritten. This allows you to change an individual setting deep in the configuration hierarchy without having to restate the entire structure.

-   **Other Types (Lists, Strings, Numbers):** When overwriting any other data type, such as a list, string, or number, the new value **completely replaces** the old one.

##### A Word of Caution on Merging Lists

It is crucial to remember that **lists are not appended or merged item-by-item**. When you provide a new list in an override file, it will **completely replace** the original list.

For example, consider a default configuration that enables several plugins:
```yaml
# In the base nomad.yaml
plugins:
  include:
    - "systemnormalizer:system_normalizer_entry_point"
    - "atomisticparsers:amber_parser_entry_point"
```
If you provide an override file to run only the `systemnormalizer:system_normalizer_entry_point` for your nomad oasis:
```yaml
# In override.yaml
plugins:
  include:
    - "atomisticparsers:amber_parser_entry_point"
```
The final list of normalizers for that run will be `["atomisticparsers:amber_parser_entry_point"]`. The `systemnormalizer` will be removed for that run because the entire `include` list was replaced.

If you intend to *add* an item to a list, you must repeat all the original items in your override file and add the new one.


### User interface customization

Many of the UI options use a data model that contains the following three fields: `include`, `exclude` and `options`. This structure allows you to easily disable, enable, reorder and modify the UI layout with minimal config rewrite. Here are examples of common customization tasks using the search columns as an example:

Disable item:

```yaml
ui:
  apps:
    options:
      entries:
        columns:
          exclude: ['upload_create_time']
```

Explicitly select the shown items and their order

```yaml
ui:
  apps:
    options:
      entries:
        columns:
          include: ['entry_id', 'upload_create_time']
```

Modify existing option

```yaml
ui:
  apps:
    options:
      entries:
        columns:
          options:
            upload_create_time:
              label: "Uploaded"
```

Add a new item that does not yet exist in options. Note that by default all options are shown in the order they have been declared unless the order is explicitly given in `include`.

```yaml
ui:
  apps:
    options:
      entries:
        columns:
          options:
            upload_id:
              label: "Upload ID"
```

The following is a reference of all configuration sections and attributes.

## Services

{{ config_models(['services', 'meta', 'oasis', 'north']) }}

## Files, databases, external services

{{ config_models(['fs', 'mongo', 'elastic', 'rabbitmq', 'keycloak', 'logstash', 'datacite', 'rfc3161_timestamp', 'mail'])}}

## Processing

{{ config_models(['process', 'reprocess', 'bundle_export', 'bundle_import', 'normalize', 'celery', 'archive'])}}

## User Interface

These settings affect the behaviour of the user interface. Note that the preferred way for creating custom apps is by using [app plugin entry points](../howto/plugins/apps.md).

{{ config_models(['ui'])}}

## Others
<<<<<<< HEAD

=======
>>>>>>> ce28bd5 (added docs configs)
{{ config_models() }}
