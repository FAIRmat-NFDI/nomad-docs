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

## Where to go next

{{ nav_list() }}

## Related materials

- For the schema language itself — attributes, types, conventions — see
  {{ nav_link("reference/metainfo.md", breadcrumb=True) }}.
- For the annotations that control how data is displayed and edited, see
  {{ nav_link("reference/annotations.md", breadcrumb=True) }}.
- For a guided introduction, see {{ nav_link("tutorial/eln/custom_eln_yaml.md", breadcrumb=True) }}
  and {{ nav_link("tutorial/develop_plugin/create_schema_package.md", breadcrumb=True) }}.
