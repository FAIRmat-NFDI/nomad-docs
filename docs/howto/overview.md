---
hide: toc
---

# NOMAD How-to guides

## Manage and find data

<span class="badge badge-user">U</span> Regular User Tag

These how-to guides target "regular" NOMAD users and cover data management, exploration, and analysis
with NOMAD's graphical user interface and APIs.

<div markdown="block" class="home-grid">
<div markdown="block">

### GUI

Use NOMAD to manage, explore, and analyze data.

- [Upload and publish data for supported formats](manage/upload.md)
- [Use ELNs](manage/eln.md)
- [Explore data](manage/explore.md)
- [Use NORTH](manage/north.md)

</div>
<div markdown="block">

### Programmatic

Use NOMAD's functionalities programmatically.

- [Use the API](programmatic/api.md)
- [Publish data using python](programmatic/publish_python.md)
- [Install nomad-lab](programmatic/pythonlib.md)
- [Access processed data](programmatic/archive_query.md)
- [Transform data](programmatic/json_transformer.md)
- [Graph-style API](./graph-api/basics.md)

</div>
</div>

## Customize

<span class="badge badge-advanced">A</span> Advanced User / Application Adminstrator Tag

These how-to guides direct advanced users, NOMAD application administrators, and data stewards to
customize various NOMAD features.

<div markdown="block" class="home-grid">
<div markdown="block">

### YAML (quick)

Implement quick and dirty customizationations of NOMAD entries.

- [Write a schema](customization/basics.md)
- [Define ELNs](customization/elns.md)
- [Use base sections](customization/base_sections.md)
- [Parse tabular data](customization/tabular.md)
- [Define workflows](customization/workflows.md)

</div>

<div markdown="block">

### Python Plugins (robust)

Implement robust and powerful customizations for data ingestion, visualization, search, and more.

- [Introduction to plugins](plugins/plugins.md)
- [Write an API](plugins/apis.md)
- [Write an app](plugins/apps.md)
- [Write an example upload](plugins/example_uploads.md)
- [Write a normalizer](plugins/normalizers.md)
- [Write a parser](plugins/parsers.md)
- [Write a schema packages](plugins/schema_packages.md)
- [Work with units](customization/units.md)
- [Use HDF5 to handle large quantities](customization/hdf5.md)
- [Use Mapping parser to write data on archive](customization/mapping_parser.md)

</div>
</div>

### Host and develop NOMAD Oasis

<span class="badge badge-sysadmin">S</span> System Adminstrator / Developer Tag

These how-to guides provide technical guidelines for system adminstrators and developers
of the core NOMAD software.

<div markdown="block" class="home-grid">
<div markdown="block">

### Host

Host a NOMAD Oasis for your lab or institution.

- [Configure an Oasis](oasis/configure.md)
- [Deploy an Oasis](oasis/deploy.md)
- [Update an Oasis](oasis/update.md)
- [Perform admin tasks](oasis/admin.md)

</div>
<div markdown="block">

### Develop

Contribute to the core NOMAD software.

- [Get started](develop/setup.md)
- [Navigate the code](develop/code.md)
- [Contribute](develop/contrib.md)
- [Extend the search](develop/search.md)

</div>
</div>

<h2>One last thing</h2>

If you can't find what you're looking for in our guides, you can find additional resources for
personalized help and assistance on our
[Support Page](https://nomad-lab.eu/nomad-lab/support.html){:target="_blank"}.
