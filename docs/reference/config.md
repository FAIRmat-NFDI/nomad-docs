# Configuration

Many aspects of NOMAD and its operation can be modified through configuration. Most configuration items have reasonable defaults and typically only a small subset has to be overwritten. Configuration items are structured hierarchically. For example, the configuration item `services.api_host` denotes the attribute `api_host` in the configuration section `services`.

## Configuration sources

Configuration items get their value based on a hierarchy of sources. The sources are applied in the following order of precedence, where later sources override earlier ones (see [merging rules](#merging-rules) below):

1. **Environment Variables:** A variable like `NOMAD_SERVICES_API_HOST`. These have the highest priority and will override all other settings. NOMAD services will inspect the environment for any variables starting with `NOMAD_`. The rest of the name is interpreted as a configuration item, where sections and attributes are concatenated with a `_`. For example, the environment variable `NOMAD_SERVICES_API_HOST` will set the value for the `api_host` attribute in the `services` section.

2. **Command-Line Configuration Files:** Files passed via the `-f` or `--config-file` flag to the NOMAD CLI. If multiple files are given, they are merged in order, with later files overriding earlier ones. For example, to load an additional configuration file on top of a default configuration, you could do the following:

    ```bash
    nomad admin run appworker -f nomad.yaml -f nomad-dev.yaml
    ```

3. **Default `nomad.yaml`:** A file named `nomad.yaml` in the current working directory, or a file pointed to by the `NOMAD_CONFIG` environment variable. This serves as the base configuration. This file is only automatically read if no file(s) have been specified using the command flag above.

4. **Built-in Defaults:** The default values hard-coded in the NOMAD source code. These have the lowest priority. These default values can be found from the `nomad/config/defaults.yaml` file in the source code.

## Merging Rules

When configuration is loaded from multiple sources (e.g., a default file and an override file), the values are merged according to the following rules:

- **Objects (Dictionaries):** When overwriting an *object*, the new value is recursively merged with the existing value. The final merged object will have all attributes from the new object, plus any attributes from the old object that were not overwritten. This allows you to change an individual setting deep in the configuration hierarchy without having to restate the entire structure.

- **Other Types (Lists, Strings, Numbers):** When overwriting any other data type, such as a list, string, or number, the new value **completely replaces** the old one.

It is crucial to remember that **lists are not appended or merged item-by-item**. When you provide a new list in an override file, it will **completely replace** the original list.

For example, consider a default configuration that enables several plugins:

```yaml
# In the base nomad.yaml
plugins:
  entry_points:
    include:
      - "systemnormalizer:system_normalizer_entry_point"
      - "atomisticparsers:amber_parser_entry_point"
```

If you provide an override file to run only the `systemnormalizer:system_normalizer_entry_point` for your nomad oasis:

```yaml
# In override.yaml
plugins:
  entry_points:
    include:
      - "atomisticparsers:amber_parser_entry_point"
```

The final list of normalizers for that run will be `["atomisticparsers:amber_parser_entry_point"]`. The `systemnormalizer` will be removed for that run because the entire `include` list was replaced.

If you intend to *add* an item to a list, you must repeat all the original items in your override file and add the new one.

## Configuration examples

Many of the configuration options use a data model that contains the following three fields: `include`, `exclude` and `options`. This structure allows you to easily disable, enable, reorder and modify the configuration values with minimal config rewrite. Here are examples of common customization tasks:

Disable plugin entry point

```yaml
plugins:
  entry_points:
    exclude:
      - <plugin-entry-point-id>
```

Explicitly select the list of plugins to use:

```yaml
plugins:
  entry_points:
    include:
      - <plugin-entry-point-id-1>
      - <plugin-entry-point-id-2>
```

Modify plugin configuration

```yaml
plugins:
  entry_points:
    options:
      <plugin-entry-point-id>:
        name: "Custom name"
```

Add a new item that does not yet exist in options. Note that by default all options are shown in the order they have been declared unless the order is explicitly given in `include`.

```yaml
plugins:
  entry_points:
    options:
      <plugin-entry-point-id>:
        menus:
          options:
            my_menu: # This option does not exist yet, create it here
              title: "My Menu"
              ...
```

## Configuration Reference

The following is a reference of all configuration sections and attributes.

### Services

{{ config_models(['services', 'meta', 'oasis', 'north']) }}

### Files, databases, external services

{{ config_models(['fs', 'mongo', 'elastic', 'rabbitmq', 'keycloak', 'logstash', 'datacite', 'rfc3161_timestamp', 'mail'])}}

### Processing

{{ config_models(['process', 'reprocess', 'bundle_export', 'bundle_import', 'normalize', 'celery', 'archive'])}}

### User Interface

These settings affect the behaviour of the user interface. Note that the preferred way for creating custom apps is by using [app plugin entry points](../howto/plugins/apps.md).

{{ config_models(['ui'])}}

### Others

{{ config_models() }}
