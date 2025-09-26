---
hide: toc
---

# NOMAD How-to guides

## Manage and find data

These how-to guides cover every-day NOMAD usage including data management, exploration, and analysis
with NOMAD's graphical user interface and APIs.

<div markdown="block" class="home-grid">
<div markdown="block">

### With the GUI

Use NOMAD to manage, explore, and analyze data.

- [Upload and publish data for supported formats](manage/gui/upload.md)
- [Enter data with ELNs](manage/gui/eln.md)
- [Explore data](manage/gui/explore.md)
- [Analyze data in NORTH](manage/gui/north.md)
- [Create custom workflows](manage/gui/workflows.md)
- [Write a YAML schema package](manage/gui/yaml.md)
- [Create custom ELNs](manage/gui/elns.md)
- [Parse tabular data](manage/gui/tabular.md)

</div>
<div markdown="block">

### Programmatically

Use NOMAD's functionalities programmatically.

[API Overview](manage/program/api.md){ .md-button .nomad-button .center}

- [Download data](manage/program/download.md)
- [Publish data using Python](manage/program/publish_python.md)
- [Access processed data](manage/program/archive_query.md)
- [Transform data](manage/program/json_transformer.md)
- [Make graph-style API calls](manage/program/graph_api.md)

</div>
</div>

## Develop plugins

These how-to guides direct advanced users, data stewards, and NOMAD application administrators to
build robust and powerful customized NOMAD support with Python-based plugin software.

[Plugins Overview](plugins/plugins.md){ .md-button .nomad-button .center}

<div markdown="block" class="home-grid">
<div markdown="block">

### Entry point types

NOMAD plugins are connect with the core software via "entry points". There are various types of entry points, with specific roles within the infrastructure for providing support for data ingestion, visualization, search, and more:

- [APIs](plugins/types/apis.md)
- [Apps](plugins/types/apps.md)
- [Example uploads](plugins/types/example_uploads.md)
- [Normalizers](plugins/types/normalizers.md)
- [Parsers](plugins/types/parsers.md)
- [Schema packages](plugins/types/schema_packages.md)

</div>

<div markdown="block">

### Built-in tools

NOMAD's built-in tools ease the plugin development process and help to ensure standardization and efficiency of plugins.

- [Work with units](plugins/tools/units.md)
- [Handle large data with HDF5](plugins/tools/hdf5.md)
- [Parse efficiently with mapping annotations](plugins/tools/mapping_parser.md)

</div>
</div>

## Host a NOMAD Oasis

These how-to guides provide technical guidelines for system adminstrators to setup, deploy, and maintain a local installation of NOMAD.

<div markdown="block" class="home-grid">
<div markdown="block">

Host a NOMAD Oasis for your lab or institution.

- [Install](oasis/install.md)
- [Configure](oasis/configure.md)
- [Deploy](oasis/deploy.md)
- [Update](oasis/update.md)
- [Administer](oasis/admin.md)

</div>

</div>

## Develop the core software

These how-to guides provide technical guidelines for developers
of the core NOMAD software.

<div markdown="block" class="home-grid">
<div markdown="block">

Contribute to the core NOMAD software.

- [Get started](develop/setup.md)
- [Navigate the code](develop/code.md)
- [Contribute](develop/contrib.md)
- [Extend the search](develop/search.md)

</div>
</div>

## Additional Resources

[Support Page](https://nomad-lab.eu/nomad-lab/support.html){.md-button .nomad-button target="_blank" rel="noopener"}
