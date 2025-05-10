# Custom schemas in NOMAD

Custom schemas in NOMAD define how data is structured, stored, and displayed, allowing users to tailor NOMAD’s metainfo to their specific research requirements. With custom schemas, users can:

- Extend NOMAD's metainfo to support their experiment-specific data.
- Define data structures that dictate how information is organized and presented.
- Enable ELN functionality for manual data input and structured documentation.
- Extract structured data from files using parsers, which allow NOMAD to read data from raw files.
- Transform and enrich data post-upload using normalizers, ensuring compatibility with schema requirements and enhancing metadata consistency.


There are two primary approaches to creating custom schemas:

- **Python schemas**: These offer highest possible level of customization by allowing the integration of **custom parsers** and **normalizers**, enabling maximum automation.
- **Serialized schemas (YAML/JSON)**: Human-readable and easier to write and manage, ideal for defining customized ELNs without coding skills. However, they do not support normalizers.

This part of the tutorial covers the following topics:

- [YAML schemas](custom_yaml.md): Defining structured YAML schemas for NOMAD.
- [Custom ELN with YAML](custom_eln.md): Creating an ELN schema to enable structured metadata entry.
- [Tabular parser in YAML](custom_tabular.md): Utilizing the built-in tabular parser to process spreadsheet data.
- [Python schemas](custom_python.md): Exploring Python schemas and their advanced capabilities.
- [Normalizers](custom_normalizer.md): Implementing normalizers to automate data processing.