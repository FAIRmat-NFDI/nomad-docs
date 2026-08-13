# Configuration

Many aspects of NOMAD and its operation can be modified through configuration. Most configuration items have reasonable defaults and typically only a small subset has to be overwritten. Configuration items are structured hierarchically. For example, the configuration item `services.api_host` denotes the attribute `api_host` in the configuration section `services`.

## Configuration sources

Configuration items get their value based on a hierarchy of sources. The sources are applied in the following order of precedence, where later sources override earlier ones (see [merging rules](#merging-rules) below):

1. **Environment Variables:** A variable like `NOMAD_SERVICES_API_HOST`. These have the highest priority and will override all other settings. NOMAD services will inspect the environment for any variables starting with `NOMAD_`. The rest of the name is interpreted as a configuration item, where sections and attributes are concatenated with a `_`. For example, the environment variable `NOMAD_SERVICES_API_HOST` will set the value for the `api_host` attribute in the `services` section.

2. **Command-Line Configuration Files:** The configuration files to read are selected in one of the following three ways, listed from highest to lowest precedence. Only the first one that applies is used: the files named by the others are not read at all, and they are not merged underneath. This follows the same design as `docker compose`, where `-f` overrides the `COMPOSE_FILE` environment variable and no implicit `docker-compose.yml` is read.

    - **The `-f` or `--config-file` flag** passed to the NOMAD CLI. It can be repeated, and it can be given before or after the sub-command, so the following two are equivalent:

        ```bash
        nomad admin run appworker -f nomad.yaml -f nomad-dev.yaml
        nomad -f nomad.yaml -f nomad-dev.yaml admin run appworker
        ```

        If the flag is given, it entirely replaces whatever `NOMAD_CONFIG` named. To build on top of another configuration file, name it explicitly, as in the examples above.

    - **The `NOMAD_CONFIG` environment variable**, which can name several files, separated by `:` (`;` on Windows). This is how to select configuration files for services that are not started through the NOMAD CLI, and for deployments where you can set environment variables but not the command, such as a Helm chart or a `docker-compose.yaml`:

        ```yaml
        services:
          app:
            environment:
              NOMAD_CONFIG: /app/nomad.yaml:/app/nomad-dev.yaml
        ```

    - **The default `nomad.yaml`**, a file of that name in the current working directory, used when neither of the above is given. **This is what most NOMAD installations use**: without the flag and without the environment variable, this single file is the whole configuration. In the official NOMAD Docker image the working directory is `/app`, so mounting your configuration at `/app/nomad.yaml` is all that is needed.

    Whichever of the three applies, if it names several files they are merged in order, with later files overriding earlier ones. A file that is named but does not exist produces a warning and is skipped; a missing default `nomad.yaml` is not reported, since running without one is normal.

3. **Built-in Defaults:** The default values hard-coded in the NOMAD source code. These have the lowest priority. These default values can be found from the `nomad/config/defaults.yaml` file in the source code.

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

If you provide an override file to run only the `systemnormalizer:system_normalizer_entry_point` for your nomad Oasis:

```yaml
# In override.yaml
plugins:
  entry_points:
    include:
      - "atomisticparsers:amber_parser_entry_point"
```

The final list of normalizers for that run will be `["atomisticparsers:amber_parser_entry_point"]`. The `systemnormalizer` will be removed for that run because the entire `include` list was replaced.

If you intend to *add* an item to a list, you must repeat all the original items in your override file and add the new one.

## Inspecting the effective configuration

To see the configuration that NOMAD actually ends up using, i.e. the result of merging all of the sources above, use:

```bash
nomad dev config
```

Pass a section to narrow the output down:

```bash
nomad dev config services
nomad dev config auth.authorized_users
```

The command takes the same `-f` flag, which makes it a quick way to check what a set of files will produce before starting a service:

```bash
nomad dev config -f nomad.yaml -f nomad-dev.yaml services
```

The list of configuration files that were read is written to stderr, so the configuration itself can be redirected to a file:

```bash
nomad dev config > effective-config.yaml
```

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

{{ config_models(['services', 'meta', 'oasis', 'auth', 'north']) }}

### Files, databases, external services

{{ config_models(['fs', 'mongo', 'elastic', 'keycloak', 'logstash', 'datacite', 'rfc3161_timestamp', 'mail'])}}

### Processing

{{ config_models(['process', 'reprocess', 'bundle_export', 'bundle_import', 'normalize', 'archive'])}}

### User Interface

These settings affect the behaviour of the user interface. Note that the preferred way for creating custom apps is by using [app plugin entry points](../howto/plugins/types/apps.md).

{{ config_models(['ui'])}}

### Others

{{ config_models() }}
