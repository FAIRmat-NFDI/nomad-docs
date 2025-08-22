# Guide to computational schema plugins

NOMAD uses [Schemas](../../reference/glossary.md#schema) to define the data structures and organization of [Processed Data](../../reference/glossary.md#processed-data). Schemas can be defined in yaml or Python formats. [How to write a schema](../../howto/customization/basics.md) describes the basics of writing a schema, in the yaml format. Computational schemas in NOMAD have historically been written in Python. There are several existing computational schema plugin projects for reference:

- [nomad-schema-plugin-run](https://github.com/nomad-coe/nomad-schema-plugin-run): contains schemas for standard processed computational data, stored in the `run` section within the NOMAD archive.
<!-- ! This naming must change, and I think it is a good moment now to do so. -->

- [nomad-schema-plugin-simulation-data](https://github.com/nomad-coe/nomad-schema-plugin-simulation-data): contains schemas for standard processed computational data, stored in the `data` section within the NOMAD archive.

- [nomad-schema-plugin-simulation-workflow](https://github.com/nomad-coe/nomad-schema-plugin-simulation-workflow): contains schemas for standard computational workflows defined in NOMAD.

- [nomad-normalizer-plugin-simulation-workflow](https://github.com/nomad-coe/nomad-normalizer-plugin-simulation-workflow): contains schemas for standard computational "normalized" data.

[Guide to Computational MetaInfo](metainfo.md) describes how these schemas are used to organize standard computational data within an [Entry](../../reference/glossary.md#entry) in the NOMAD repository.

<!-- TODO Add best practices + tips for schema implementation/design -->
<!-- ### Best practices for computational parser design -->

<!-- ### Tips for implementation of computaional parsers -->