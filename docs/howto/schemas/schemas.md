# How to work with schemas in NOMAD

Every piece of data in NOMAD follows a *schema*. A schema is a collection of
[section](../../reference/glossary.md#section-and-subsection) and
[quantity](../../reference/glossary.md#quantity) definitions that give your data names, types,
shapes and units, so that it can be browsed, searched, compared and analyzed. Schemas are written in
the NOMAD Metainfo schema language.

This section collects everything you need to write and maintain them. If you are new to the concepts
behind schemas, read [Explanation > Data structure](../../explanation/data.md) first.

## Choose Python or YAML

You can write a schema in two syntaxes. They describe the same thing: there is a 1-to-1 translation
between a Python schema package (written as classes) and a YAML or JSON one (written as objects), and
both use the same concepts of *section*, *quantity* and *subsection*.

| | YAML schemas | Python schemas |
| --- | --- | --- |
| Where it lives | An `.archive.yaml` file you upload | A plugin, installed into a NOMAD distribution |
| Who can add it | Any NOMAD user | Plugin developers and Oasis administrators |
| Distribution | Within the upload it was uploaded to | To every installation that installs the plugin |
| Custom `normalize` functions | No | Yes |
| Best for | Exploring schemas, one-off and lab-specific ELNs | Reusable schemas, derived data, anything shipped to others |

Start with YAML if you are describing your own data and want to see results immediately. Move to
Python when you need custom normalization, want to share the schema across installations, or want
the schema to be version controlled and tested alongside code.

All built-in NOMAD schemas are written in Python and live in `nomad.datamodel.metainfo.*`.

## Get your schema into NOMAD

Writing the definitions is the same job in both syntaxes; getting them in front of NOMAD is not.

=== "Python"

    A Python schema is delivered as a plugin. Define a `SchemaPackageEntryPoint` whose `load` method
    returns your `SchemaPackage`, usually in `*/schema_packages/__init__.py`:

    ```python
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

    Then register it in `pyproject.toml` so NOMAD discovers it automatically:

    ```toml
    [project.entry-points.'nomad.plugin']
    mypackage = "nomad_example.schema_packages:mypackage"
    ```

    Once the plugin is installed, the schema is available to every user of that installation. See
    {{ nav_link("howto/plugins/types/schema_packages.md", breadcrumb=True) }} for the full entry
    point reference.

=== "YAML"

    A YAML schema is delivered by uploading it. NOMAD archive files carry data in NOMAD's native
    format and end in `.archive.yaml` or `.archive.json`; because a YAML schema is itself just data,
    the same file format carries schemas too.

    Upload the file like any other, and the definitions become available within that upload.

    ```yaml
    definitions:
      name: 'Sample management example schema'
      sections:
        Sample:
          base_sections:
            - nomad.datamodel.data.EntryData
          quantities:
            name:
              type: str
    ```

## Organize schema and data across files

A YAML archive file can hold `definitions`, `data`, or both. Which you choose decides how reusable
the schema is.

Keeping them **in one file** is the quickest way to try something out:

```yaml
definitions:
  sections:
    Sample:
      base_sections:
        - nomad.datamodel.data.EntryData
      quantities:
        name:
          type: str
data:
  m_def: Sample
  name: S1
```

Keeping them **in separate files** lets many data files share one schema, which is almost always what
you want beyond a first experiment. Put the definitions in `schema.archive.yaml`:

```yaml
definitions:
  sections:
    Sample:
      base_sections:
        - nomad.datamodel.data.EntryData
      quantities:
        name:
          type: str
```

and point each data file at it:

```yaml
data:
  m_def: '../upload/raw/schema.archive.yaml#Sample'
  name: S1
```

!!! note
    Schema packages in two different entries cannot reference each other. Each package has to be
    fully loaded before another can use it, so a circular dependency between two `.archive.yaml`
    files will not resolve.

Python schemas do not face this choice: the schema lives in the plugin, and data always lives in
uploaded files or is produced by a parser.

## Where to go next

{{ nav_list() }}

## Related materials

- For the schema language itself — attributes, types, conventions — see
  {{ nav_link("reference/metainfo.md", breadcrumb=True) }}.
- For the annotations that control how data is displayed and edited, see
  {{ nav_link("reference/annotations.md", breadcrumb=True) }}.
- For a guided introduction, see {{ nav_link("tutorial/eln/custom_eln_yaml.md", breadcrumb=True) }}
  and {{ nav_link("tutorial/develop_plugin/create_schema_package.md", breadcrumb=True) }}.
