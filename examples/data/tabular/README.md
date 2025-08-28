# Demonstration for tabular data usage

This upload demonstrates the use of tabular data. In this example we use an *xlsx* file in combination with a custom schema. The schema describes what columns in the excel file mean and how NOMAD is expected to parse and map the content accordingly in order to produce a **FAIR** dataset.

This schema is meant as a starting point. You can download the schema file and
extend the schema for your own tables.

In order to see the parsed data, create an entry by clicking on the ***create from schema*** button,
pick a name for your entry, and select ***Custom schema*** from the options. Then click on the
search icon, from the dialogue, click on the ***Periodic Table*** and select ***Element*** from the
dropdown menu. Clicking on `Create` would trigger the parser and you should be able to see all elements
successfully parsed into individual entries.

Consult our [documentation on the NOMAD Archive and Metainfo](https://nomad-lab.eu/prod/v1/staging/docs/) to learn more about schemas.
