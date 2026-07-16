# Create a parser

This tutorial guides you through creating NOMAD parsers that transform raw files into structured database entries. It covers three different approaches, each reflecting a different level of user interaction in the NOMAD GUI:

- **[Tutorial 1](./create_parser_parser_only.md)** — A `MatchingParser` automatically detects and parses the file into a *static* entry when it is uploaded.
- **[Tutorial 2](./create_parser_eln_only.md)** — An ELN entry is created manually by the user. Uploading a file to its `data_file` field triggers the parsing.
- **[Tutorial 3](./create_parser_hybrid.md)** — A hybrid approach: automated matching creates an ELN entry with `data_file` pre-populated, which immediately triggers parsing in one step.

## Learning Outcomes

By the end of this tutorial, you will be able to:

1. Build a `MatchingParser` that automatically processes uploaded raw files.
2. Implement three different parser–entry interaction patterns in NOMAD.
3. Use ELN entries for parsing data from raw files.

## Before you begin

This tutorial assumes basic familiarity with Python and Git. You should have Python 3.10 or higher installed, along with Git. We recommend using a modern Python IDE (such as VS Code or PyCharm) to follow along.

We will use the [nomad-plugin-tutorials](https://github.com/FAIRmat-NFDI/nomad-plugin-tutorials){:target="_blank" rel="noopener"} repository to build the schema package step by step. Start by cloning the repository and navigating into it:

```bash
git clone git@github.com:FAIRmat-NFDI/nomad-plugin-tutorials.git
cd nomad-plugin-tutorials
```

To access the "tutorial mode" version of the code (which contains code-along exercises with missing snippets for you to implement), switch to the `tutorial-mode` branch:

```bash
git checkout tutorial-mode
```

For instructions on installing and running the plugin locally, refer to the repository's [README.md](https://github.com/FAIRmat-NFDI/nomad-plugin-tutorials#getting-started){:target="_blank" rel="noopener"}.

The parser tutorial code is located in the `src / nomad_plugin_tutorials / parsers` directory. It contains three sub-tutorials in
the directories `tutorial_1/`, `tutorial_2/`, and `tutorial_3/`, one for each parsing approach.

## Example data from Optical Microscopy

All three tutorials use the same example dataset from an optical microscopy measurement, located in `src / nomad_plugin_tutorials / parsers / data / om_example`. It consists of an XML metadata file (`metadata.xml`) containing acquisition parameters such as resolution, magnification, sample ID, and datetime, together with a JPEG image file (`image.jpeg`) referenced from the metadata.

The XML metadata file contains the following:

```xml
<image_metadata type="microscopy">
  <resolution>500x500</resolution>
  <magnification>5x</magnification>
  <sample>
    <sample_ID>Sample_001</sample_ID>
    <description>Spin-coated slide after annealing.</description>
  </sample>
  <datetime>2025-06-01T12:00:00</datetime>
  <imageFileName>image.jpeg</imageFileName>
</image_metadata>
```

A shared helper function `read_data_file` (from `nomad_plugin_tutorials.parsers.reader`) uses NOMAD's `XMLParser` to open the file via `archive.m_context` and convert it to a Python dictionary. We use the resulting `data_dict` to populate the schema.

## Register the parser

A parser is registered in the same way as a schema package: by defining a `ParserEntryPoint` in the `__init__.py` of the parsers module and adding it to `pyproject.toml`.

The entry point class overrides `load()` to instantiate and return the parser. Crucially, `mainfile_name_re` sets a regular expression pattern that NOMAD uses to match this parser to incoming files. Let's take the example of Tutorial 1:

```py
from nomad.config.models.plugins import ParserEntryPoint

class MicroscopyParserEntryPoint(ParserEntryPoint):
    def load(self):
        from nomad_plugin_tutorials.parsers.tutorial_1.parsers.parser import (
            OpticalMicroscopyParser,
        )
        return OpticalMicroscopyParser(**self.model_dump())

microscopy = MicroscopyParserEntryPoint(
    name='Parser Tutorial 1: Microscopy Parser',
    description='Microscopy parser entry point.',
    mainfile_name_re=r'.*\.xml$',
)
```

Register both the schema package and the parser entry points in `pyproject.toml`:

```toml
[project.entry-points.'nomad.plugin']
parser_tutorial_1_schema = "nomad_plugin_tutorials.parsers.tutorial_1.schema:microscopy"
parser_tutorial_1_parser = "nomad_plugin_tutorials.parsers.tutorial_1.parsers:microscopy"
```

Then reinstall the plugin:

```sh
pip install -e '.[dev]'
```

or, if you use `uv`:

```sh
uv sync --extra dev
```

For Tutorial 2, we only have a schema package, whereas for Tutorial 3, we again
have both parser and schema package entry points.
