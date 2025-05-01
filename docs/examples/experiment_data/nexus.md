# Standardized ingestion of data from materials characterization using NeXus

Build upon your understanding of NOMAD's features with domain-specific examples and explanations.

NeXus is a common data format developed by an international collaboration of scientists to support the exchange, storage, and archival of scientific data, particularly from neutron, X-ray, and muon experiments which is extended to cover experiment techniques used in Materials Science. Built on top of HDF5, NeXus adds a structured, self-describing framework designed specifically for complex scientific experiments.

The goal of NeXus is to make scientific data easier to share, analyze, and visualize, both within a facility and across different research institutions. It achieves this through:

- Well-defined metadata conventions that capture experimental context alongside the data itself.
- Application definitions that provide templates for specific experiment types to ensure consistency.
- A corresponding ontology which defines the terms and their relationship
- Standardized file structure that organizes data into hierarchical groups, folowing the ontology relationship

NeXus files can store raw data, processed data, and the metadata necessary to fully understand how the data was collected and analyzed. This makes NeXus a valuable tool for preserving data integrity and promoting FAIR (Findable, Accessible, Interoperable, Reusable) data practices across scientific disciplines.

Whether you are storing simple measurements or the output of complex multi-component instruments, NeXus provides a flexible, extensible framework to help ensure your data remains useful and understandable far into the future.

- [FAIRmat NeXus extension proposal](https://fairmat-nfdi.github.io/nexus_definitions/)
- [NeXusOntology](https://github.com/FAIRmat-NFDI/NeXusOntology/)
- [NeXus](https://www.nexusformat.org/)

