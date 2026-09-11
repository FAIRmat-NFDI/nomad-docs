# How to create a schema package

Schema packages are used to define and distribute custom data definitions that can be used within NOMAD. These schema packages typically contain [schemas](../../../reference/glossary.md#schema) that users can select to instantiate manually filled entries using our ELN functionality, or that parsers select when organizing data they extract from files. Schema packages may also contain more abstract base classes that other schema packages use.

This documentation shows you how to create a plugin entry point for a schema package. You should read the [introduction to plugins](../plugins.md) to have a basic understanding of how plugins and plugin entry points work in the NOMAD ecosystem.

## Getting started

You can use our [template repository](https://github.com/FAIRmat-NFDI/nomad-plugin-template){:target="_blank" rel="noopener"} to create an initial structure for a plugin containing a schema package. The relevant part of the repository layout will look something like this:

```txt
nomad-example
   ├── src
   │   ├── nomad_example
   │   │   ├── schema_packages
   │   │   │   ├── __init__.py
   │   │   │   ├── mypackage.py
   ├── LICENSE.txt
   ├── README.md
   └── pyproject.toml
```

See the documentation on [plugin development guidelines](../plugins.md#plugin-development-guidelines) for more details on the best development practices for plugins, including linting, testing and documenting.

## Schema package entry point

The entry point defines basic information about your schema package and is used to automatically load it into a NOMAD distribution. It is an instance of a `SchemaPackageEntryPoint` or its subclass and it contains a `load` method which returns a `nomad.metainfo.SchemaPackage` instance that contains section and schema definitions. You will learn more about the `SchemaPackage` class in the next sections. The entry point should be defined in `*/schema_packages/__init__.py` like this:

```python
from pydantic import Field
from nomad.config.models.plugins import SchemaPackageEntryPoint


class MySchemaPackageEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        from nomad_example.schema_packages.mypackage import m_package

        return m_package


mypackage = MySchemaPackageEntryPoint(
    name='MyPackage',
    description='My custom schema package.',
)
```

Here you can see that a new subclass of `SchemaPackageEntryPoint` was defined. In this new class you can override the `load` method to determine how the `SchemaPackage` class is loaded, but you can also extend the `SchemaPackageEntryPoint` model to add new configurable parameters for this schema package as explained [Explanation > Plugins > Plugin configuration](../../../explanation/plugin_system.md#plugin-configuration).

We also instantiate an object `mypackage` from the new subclass. This is the final entry point instance in which you specify the default parameterization and other details about the schema package. In the reference you can see all of the available [configuration options for a `SchemaPackageEntryPoint`](../../../reference/plugins.md#schemapackageentrypoint).

The entry point instance should then be added to the `[project.entry-points.'nomad.plugin']` table in `pyproject.toml` in order for it to be automatically detected:

```toml
[project.entry-points.'nomad.plugin']
mypackage = "nomad_example.schema_packages:mypackage"
```

## Write the schema itself

The `load` method returns a `nomad.metainfo.SchemaPackage` instance holding your section and quantity
definitions. Writing those definitions has its own section of the documentation:

- {{ nav_link("howto/schemas/schemas.md", breadcrumb=True) }} — choose between Python and YAML.
- {{ nav_link("howto/schemas/python.md", breadcrumb=True) }} — define sections, quantities and
  normalize functions in Python.
- {{ nav_link("howto/schemas/base_sections.md", breadcrumb=True) }} — reuse and extend existing definitions.
- {{ nav_link("howto/schemas/evolution.md", breadcrumb=True) }} — version and migrate a schema package.
- {{ nav_link("reference/metainfo.md", breadcrumb=True) }} — the schema language reference.

## Schema packages developed by FAIRmat

The following is a list of plugins containing schema packages developed by FAIRmat:

| Description         | Project url                                                                |
| ------------------- | -------------------------------------------------------------------------- |
| simulation run      | <https://github.com/nomad-coe/nomad-schema-plugin-run.git>                 |
| simulation data     | <https://github.com/nomad-coe/nomad-schema-plugin-simulation-data.git>     |
| simulation workflow | <https://github.com/nomad-coe/nomad-schema-plugin-simulation-workflow.git> |
| NEXUS               | <https://github.com/FAIRmat-NFDI/pynxtools.git>                            |
| synthesis           | <https://github.com/FAIRmat-NFDI/AreaA-data_modeling_and_schemas.git>      |
| material processing | <https://github.com/FAIRmat-NFDI/nomad-material-processing.git>            |
| measurements        | <https://github.com/FAIRmat-NFDI/nomad-measurements.git>                   |
| catalysis           | <https://github.com/FAIRmat-NFDI/nomad-catalysis-plugin.git>               |
