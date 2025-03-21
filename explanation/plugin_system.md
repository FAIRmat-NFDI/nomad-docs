# NOMAD plugin system

## Introduction

NOMAD is used by many research communities with their specific data, workflows, and analysis tools. NOMAD plugins are key
to adopt NOMAD to these heterogeneous environments.
You can think of plugins as “add-ons” that provide additional capabilities.
Each plugin is a small independant software project that integrates with the core NOMAD and provides features without modifictions to the core NOMAD itself.
Some key advantages of using plugins:

- **Modularity**: You can pick and choose which features or functions to add, rather than having everything baked into the core NOMAD.

- **Customizability**: Users can add their own plugins to address specific use cases, without changing the official NOMAD software.

- **Easy updates**: If a feature needs to be updated or improved, it can be done at the plugin level, without having to release a new NOMAD version.

- **Collaboration**: Since plugins are independent, multiple developers can work on different features in parallel and with different release cycles without interfering with each other.

## Architecture

There are three core components to the plugin system:

- **Distributions** define lists of plugins and their version. A distribution is a small
  Git and Python project that maintains a list of plugin dependencies in its `pyproject.toml`. We provide a [template repository](https://github.com/FAIRmat-NFDI/nomad-distro-template)
  for a quick start into creating distributions.
- **Plugins** are Git and Python projects that contain one or many _entry points_.
  We provide a [template repository](https://github.com/FAIRmat-NFDI/nomad-plugin-template)
  for a quick start into plugin development.
- **Entry points** are individual contributions (e.g. parsers, schemas, or apps)
  which are defined using a feature of Python called [_entry points_](https://setuptools.pypa.io/en/latest/userguide/entry_point.html).

<figure markdown style="width: 100%">
  ``` mermaid
  %%{init:{'flowchart':{'nodeSpacing': 25, 'subGraphTitleMargin': {'top': 5, 'bottom': 10}, 'padding': 10}}}%%
  graph LR
    subgraph NOMAD Distribution
      subgraph NOMAD Plugin C
        ro7(Entry point: Schema 1)
        ro8(Entry point: Schema 2)
      end
      subgraph NOMAD Plugin B
        ro4(Entry point: Schema)
        ro5(Entry point: App 1)
        ro6(Entry point: App 2)
      end
      subgraph NOMAD Plugin A
        ro1(Entry point: Schema)
        ro2(Entry point: Parser 1)
        ro3(Entry point: Parser 2)
      end
    end
  ```
  <figcaption>Relation between NOMAD distributions, plugins and entry points.</figcaption>
</figure>

This architecture allows plugin developers to freely choose a suitable granularity for their use case: they may create a single plugin package that contains everything that e.g. a certain lab needs: schemas, parsers and apps. Alternatively they may also develop multiple plugins, each containing a single entry point. Reduction in package scope can help in developing different parts indepedently and also allows plugin users to choose only the parts that they need.

## Plugin entry points

Plugin entry points represent different types of customizations that can be added to a NOMAD installation. The following plugin entry point types are currently supported:

- [APIs](../howto/plugins/apis.md)
- [Apps](../howto/plugins/apps.md)
- [Example uploads](../howto/plugins/example_uploads.md)
- [Normalizers](../howto/plugins/parsers.md)
- [Parsers](../howto/plugins/parsers.md)
- [Schema packages](../howto/plugins/schema_packages.md)


Entry points contain **configuration**, but also a **resource**, which lives in a separate Python module. This split enables lazy-loading: the configuration can be loaded immediately, while the resource is loaded later when/if it is required. This can significantly improve startup times, as long as all time-consuming initializations are performed only when loading the resource. This split also helps to avoid cyclical imports between the plugin code and the `nomad-lab` package.

For example the entry point configuration for a parser is contained in `.../parsers/__init__.py` and it contains e.g. the name, version and any additional entry point-specific parameters that control its behaviour. The entry point has a `load` method than can be called lazily to return the resource, which is a `Parser` instance defined in `.../parsers/myparser.py`.

In `pyproject.toml` you can expose plugin entry points for automatic discovery. E.g. to expose an app and a package, you would add the following to `pyproject.toml`:

```toml
[project.entry-points.'nomad.plugin']
myapp = "nomad_example.parsers:myapp"
mypackage = "nomad_example.schema_packages:mypackage"
```

Here it is important to use the `nomad.plugin` group name in the `project.entry-points` header. The value on the right side (`"nomad_example.schema_packages:mypackage"`) must be a path pointing to a plugin entry point instance inside the python code. This unique key will be used to identify the plugin entry point when e.g. accessing it to read some of it's configuration values. The name on the left side (`mypackage`) can be set freely.

You can read more about how to write different types of entry points in their dedicated documentation pages or learn more about the [Python entry point mechanism](https://setuptools.pypa.io/en/latest/userguide/entry_point.html).

### Plugin configuration

The plugin entry point configuration is an instance of a [`pydantic`](https://docs.pydantic.dev/latest/) model. This base model may already contain entry point-specific fields (such as the file extensions that a parser plugin will match) but it is also possible to extend this model to define additional fields that control your plugin behaviour.

Here is an example of a new plugin entry point configuration class and instance for a parser, that has a new custom `parameter` configuration added as a `pydantic` `Field`:

```python
from pydantic import Field
from nomad.config.models.plugins import ParserEntryPoint


class MyParserEntryPoint(ParserEntryPoint):
    parameter: int = Field(0, description='Config parameter for this parser.')

myparser = MyParserEntryPoint(
    name = 'MyParser',
    description = 'My custom parser.',
    mainfile_name_re = '.*\.myparser',
)
```

The plugin entry point behaviour can be controlled in `nomad.yaml` using `plugins.entry_points.options`:

```yaml
plugins:
  entry_points:
    options:
      "nomad_example.parsers:myparser":
        parameter: 47
```

Note that the model will also validate the values coming from `nomad.yaml`, and you should utilize the validation mechanisms of `pydantic` to provide users with helpful messages about invalid configuration.

### Plugin resource

The configuration class has a `load` method that returns the entry point resource. This is typically an instance of a class, e.g. `Parser` instance in the case of a parser entry point. Here is an example of a `load` method for a parser:

```python
class MyParserEntryPoint(ParserEntryPoint):

    def load(self):
        from nomad_example.parsers.myparser import MyParser

        return MyParser(**self.dict())
```

Often when loading the resource, you will need access to the final entry point configuration defined in `nomad.yaml`. This way also any overrides to the plugin configuration are correctly taken into account. You can get the final configuration using the `get_plugin_entry_point` function and the plugin name as defined in `pyproject.toml` as an argument:

```python
from nomad.config import config

configuration = config.get_plugin_entry_point('nomad_example.parsers:myparser')
print(f'The parser parameter is: {configuration.parameter}')
```

## Entry point discovery

Entry points are like pre-defined connectors or hooks that allow the main system to recognize and load the code from plugins without needing to hard-code them directly into the platform. This mechanism enables the automatic discovery of plugin code. The following diagram illustrates how NOMAD interacts with the entry points in a plugin:

<figure markdown style="width: 100%">
  ``` mermaid
  %%{init:{'sequence':{'mirrorActors': false}}}%%
  sequenceDiagram
    autonumber
    rect
      NOMAD->>Plugin: Request entry points matching the nomad.plugin group
      Plugin-->>NOMAD: Return all entry point configurations
    end
      Note over NOMAD: Other tasks
    rect
      NOMAD->>Plugin: Request a specific entry point resource
      opt
        Plugin->>NOMAD: Request configuration overrides from nomad.yaml
        NOMAD-->>Plugin: Return final configuration for entry point
      end
      Plugin-->>NOMAD: Return fully initialized entry point resource
    end
  ```
  <figcaption>NOMAD interaction with a plugin.</figcaption>
</figure>

1.  When NOMAD starts, it scans for plugin entry points defined under the `nomad.plugin` group in all of the Python packages that have been installed.
2.  The plugin returns all entry points that it has registered in `pyproject.toml` under the `nomad.plugin` group. This only loads the configuration, but does not yet load the resource, i.e. main Python implementation.
3.  When NOMAD needs to load the actual resource for an entry point (e.g. a parser), loads it by using the configuration instance.
4.  When the resource is being loaded, the entry point may ask for any configuration overrides that may have been set in `nomad.yaml`.
5.  NOMAD will return the final validated configuration that contains the default values and possible overrides.
6.  The plugin loads and returns the resource using the final configuration. This typically involves creating an instance of a specific class, e.g. `Parser` in the case of parser entry points.

## Learn how to write plugins

You can learn more about plugin development in the [introduction to plugins](../howto/plugins/plugins.md) -page.
