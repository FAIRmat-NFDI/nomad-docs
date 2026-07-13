---
hide: toc
---

# Tutorials

Tutorials provide guided, learning-oriented paths. Use them when you want to understand a workflow end to end. See {{ nav_link("howto/overview.md", breadcrumb=True) }} if you are trying to complete a known, isolated task.

## Before you begin

Unless stated otherwise, these tutorials use **NOMAD Central**, the public FAIRmat-hosted NOMAD platform. There are two relevant deployments:

- [**Production**](https://nomad-lab.eu/prod/v1/gui/search/entries){:target="_blank" rel="noopener"}: Use by default for any generic tutorial activities.
- [**Test**](https://nomad-lab.eu/prod/v1/test/gui/search/entries){:target="_blank" rel="noopener"}: Use primarily for testing publishing capabilities. This deployment contains a dedicated *temporary* database that is routinely wiped.

The majority of underlying concepts and workflows also apply to **NOMAD Oasis** deployments, although specific behavior may differ between installations depending on which plugins are installed.

### Create a NOMAD user account

Some tutorials require you to sign in before you can upload, share, or publish data. For step-by-step account creation and sign-in guidance, see {{ nav_link("howto/manage/gui/account.md", breadcrumb=True) }}.

## Tutorial paths

<div markdown="block" class="home-grid">
<div markdown="block">

### {{ nav_link("tutorial/explore.md") }}

Learn how to search, filter, and inspect published NOMAD data.

</div>
<div markdown="block">

### Upload and publish data

Follow a complete upload and publication workflow using either interface.

- {{ nav_link("tutorial/upload_publish.md") }}
- {{ nav_link("tutorial/upload_publish_api.md") }}

</div>
<div markdown="block">

### Use NOMAD as an ELN

Create structured experimental records using built-in or custom schemas.

- {{ nav_link("tutorial/eln/built_in_templates.md") }}
- {{ nav_link("tutorial/eln/custom_eln_yaml.md") }}
- {{ nav_link("tutorial/eln/tabular_parser_yaml.md") }}

</div>
<div markdown="block">

### {{ nav_link("tutorial/workflows_projects.md") }}

Connect related entries and organize them into projects and workflows.

</div>
<div markdown="block">

### Develop a NOMAD plugin

Build a plugin structure, schema package, and parser through guided exercises.

- {{ nav_link("tutorial/develop_plugin/plugin_structure.md") }}
- {{ nav_link("tutorial/develop_plugin/create_schema_package.md") }}
- **Create a parser**
    - {{ nav_link("tutorial/develop_plugin/create_parser.md") }}
    - {{ nav_link("tutorial/develop_plugin/create_parser_parser_only.md") }}
    - {{ nav_link("tutorial/develop_plugin/create_parser_eln_only.md") }}
    - {{ nav_link("tutorial/develop_plugin/create_parser_hybrid.md") }}

</div>
</div>

## Additional training resources

Find event materials and external training collections in the
{{ nav_link("reference/tutorials.md", breadcrumb=True) }}.
