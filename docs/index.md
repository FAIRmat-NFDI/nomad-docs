---
hide: toc
---

# Home

NOMAD is an open-source research data platform for materials science. It helps researchers, labs, and developers make data FAIR: findable, accessible, interoperable, and reusable.

This documentation is organized into four sections. Use the section that best matches your need: learning, completing a task, understanding a concept, or finding technical information.

<div markdown="block" class="home-grid">
<div markdown="block">

## Tutorials

Learn NOMAD step by step through guided, hands-on examples.

- {{ nav_link("tutorial/explore.md") }}: start with published data and the search interface.
- {{ nav_link("tutorial/upload_publish.md") }}: learn the basic data submission workflow.
- {{ nav_link("tutorial/eln/built_in_templates.md") }}: create structured experimental records.
- {{ nav_link("tutorial/develop_plugin/plugin_structure.md") }}: begin the plugin development tutorial path.

[Open all tutorials](tutorial/overview.md){:.md-button .nomad-button .nomad-button--card-action}

</div>
<div markdown="block">

## How-to guides

Accomplish specific tasks by following practical instructions.

- {{ nav_link("howto/manage/gui/upload.md") }}: publish data through the graphical interface.
- {{ nav_link("howto/manage/program/api.md") }}: automate data access and management.
- {{ nav_link("howto/plugins/plugins.md") }}: develop extensions for NOMAD.
- {{ nav_link("howto/oasis/install.md") }}: install a self-hosted NOMAD deployment.

[Open all how-to guides](howto/overview.md){:.md-button .nomad-button .nomad-button--card-action}

</div>
<div markdown="block">

## Explanation

Understand NOMAD's key concepts, architecture, and underlying mechanisms.

- {{ nav_link("explanation/basics.md") }}
- {{ nav_link("explanation/data.md") }}
- {{ nav_link("explanation/plugin_system.md") }}
- {{ nav_link("explanation/oasis.md") }}

[Open all explanations](explanation/overview.md){:.md-button .nomad-button .nomad-button--card-action}

</div>
<div markdown="block">

## Reference

Find detailed technical information such as configuration options, CLI commands, and schema details.

- {{ nav_link("reference/config.md") }}
- {{ nav_link("reference/cli.md") }}
- {{ nav_link("reference/basesections.md") }}
- {{ nav_link("reference/glossary.md") }}

[Open all reference](reference/overview.md){:.md-button .nomad-button .nomad-button--card-action}

</div>
</div>

<!-- TODO: Revisit and update the below once the nomad-lab homepage refactor is complete. -->

## Using NOMAD

Most examples in the documentation use **NOMAD Central**, the public FAIRmat-hosted NOMAD platform. There are two relevant deployments:

- [**Production**](https://nomad-lab.eu/prod/v1/gui/search/entries){:target="_blank" rel="noopener"}: The primary deployment for day-to-day use and most documentation examples.
- [**Test**](https://nomad-lab.eu/prod/v1/test/gui/search/entries){:target="_blank" rel="noopener"}: A separate deployment intended for testing features such as data publication. The underlying database is temporary and is periodically reset.

The majority of underlying concepts and workflows also apply to **NOMAD Oasis** deployments, although specific behavior may differ between installations depending on which plugins are installed.

## Who NOMAD supports

- Researchers using [NOMAD Central](https://nomad-lab.eu/prod/v1/gui/){:target="_blank" rel="noopener"} to manage, explore, and publish data.
- Labs and institutions operating a NOMAD Oasis.
- Plugin developers extending NOMAD for domain-specific needs.
- Core contributors working on `nomad-lab`.

## Project and community

NOMAD is developed by FAIRmat, an NFDI consortium building shared data infrastructure for materials science.

- [Get support](https://nomad-lab.eu/nomad-lab/support.html){:target="_blank" rel="noopener"}
- [Contribute to NOMAD](howto/develop/contrib.md)
- [View the roadmap](https://nomad-lab.eu/nomad-lab/features.html){:target="_blank" rel="noopener"}
- [Read the code guidelines](reference/code_guidelines.md)
