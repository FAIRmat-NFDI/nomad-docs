# Matching and creating an ELN entry (Hybrid Approach)

Users often prefer a hybrid approach of tutorial 1 and 2, where raw files can be matched automatically (as in tutorial 1) but an ELN is generated for users to provide input. The data is then read from the raw file in the `normalize` method (as in tutorial 2).

This can be achieved by matching the raw file but only creating a minimal "Raw Data File" entry. The parser then selects and creates an appropriate ELN entry with the reading logic in its `normalize` method.

Realizing this approach requires multiple steps from the developer. To simplify the process, we created a specialized `ElnParserEntryPoint` class which redefines a standard `ParserEntryPoint`. The specific classes for both the Raw Data File entry and the ELN can be selected by the developer.

## Tutorial instructions

!!! question "Tutorial 3.1"
    Please switch to the parser tutorial 3 by commenting out lines corresponding to `tutorial_2` and uncommenting the lines corresponding to `tutorial_3` in the `[project.entry-points.'nomad.plugin']` section of the `pyproject.toml`.

    You can find this file in the `tutorial-mode` branch under the root of the repository. Read the instructions in the code for more information.

??? success "Tutorial 3.1: Solution"
    ```toml
    [project.entry-points.'nomad.plugin']
    # parser_tutorial_1_schema = "nomad_plugin_tutorials.parsers.tutorial_1.schema:microscopy"
    # parser_tutorial_1_parser = "nomad_plugin_tutorials.parsers.tutorial_1.parsers:microscopy"

    # parser_tutorial_2_schema = "nomad_plugin_tutorials.parsers.tutorial_2.schema:microscopy"

    parser_tutorial_3_schema = "nomad_plugin_tutorials.parsers.tutorial_3.schema:microscopy"
    parser_tutorial_3_parser = "nomad_plugin_tutorials.parsers.tutorial_3.parsers:microscopy"
    ```

When using `ElnParserEntryPoint`, you can choose to utilize default versions of both the Raw Data File entry and the ELN entry (`ElnParserRawFile` and `ElnParserSection` respectively). Alternatively, you can define specialized schema classes inheriting from the default classes for one or both of them. In this tutorial, we use the default schema for the raw file entry and a custom schema for the ELN entry.

!!! question "Tutorial 3.2"
    Define the appropriate parser entry point in the `__init__.py` file of the parsers folder. Note that the `OpticalMicroscopy` schema and its normalization are almost exactly the same as in the previous tutorial, and therefore all the manual user updates in the ELN will be correctly saved to the entry archive. The only difference is the inheritance from `ElnParserSection` instead of the usual `EntryData`.

    You can find the file in the `tutorial-mode` branch under `src / nomad_plugin_tutorials / parsers / tutorial_3 / parsers / __init__.py`. Read the instructions in the code for more information.

??? success "Tutorial 3.2: Solution"

    ```py
    from nomad.config.models.plugins import ElnParserEntryPoint

    microscopy = ElnParserEntryPoint(
        name='Parser Tutorial 3: Microscopy Parser',
        description='Microscopy parser entry point.',
        mainfile_name_re=r'.*\.xml$',
        eln_m_def='nomad_plugin_tutorials.parsers.tutorial_3.schema.schema_package.'
        'OpticalMicroscopy',
    )
    ```

## Hybrid approach: the outcome

The hybrid approach to parsing combines the advantages of the two previously described methods at the cost of the increased complexity of the resulting data structure. The raw file is automatically parsed into a **static** raw data file entry, that references an additional **automatically generated but user-editable** ELN entry.

## Testing the parser

If you use the `nomad-distro-dev` development environment, all functionality of the plugin can be tested within the GUI by restarting the appworker and/or the GUI. For details, please see the `README.md` file of the [`nomad-distro-dev` repository](https://github.com/FAIRmat-NFDI/nomad-distro-dev){:target="_blank" rel="noopener"}.

For a stand-alone installation of the plugin, please use the provided `tutorial.ipynb` Jupyter notebook (you can find it under `src / nomad_plugin_tutorials / parsers / tutorial_3 / tutorial.ipynb`).

Before running the notebook, ensure that the plugin and all dependencies are installed by running

```sh
uv sync --extra dev
```

or, if you use pip:

```sh
pip install -e '.[dev]'
```

In step 1, you will use the `parse()` function from `nomad.client` to imitate uploading a file in the GUI.

In step 2, you can inspect the parsing results of the raw file archive.

In step 3, you parse a newly created ELN archive and run the normalizer to populate the data from the source file.

In step 4, you can inspect the parsing results of the ELN archive.
