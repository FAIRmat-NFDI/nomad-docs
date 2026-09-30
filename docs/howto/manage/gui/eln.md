# How to import data from third-party ELNs

This guide explains how to import data from third-party electronic lab notebooks
(ELNs) into NOMAD using integration parsers and schemas.

The `nomad-external-eln-integrations` package provides these integrations.
The specific integrations available in your NOMAD deployment depend on the
parsers and schemas installed there. The procedures below cover elabFTW,
Labfolder, Chemotion, and openBIS. In each case, the integration maps data from
the external ELN into NOMAD Entries, although the retrieval and mapping process
varies by provider.

If you want to create and edit ELN Entries directly in NOMAD, see
[Tutorials > ELN > Built-in ELN templates](../../../tutorial/eln/built_in_templates.md).

### elabFTW integration

elabFTW is part of [the ELN Consortium](https://github.com/TheELNConsortium){:target="_blank" rel="noopener"}
and supports exporting experimental data in ELN file format. ELNFileFormat is a zipped file
that contains <b>metadata</b> of your elabFTW project along with all other associated data of
your experiments.

To import elabFTW data into NOMAD:

1. In elabFTW, export the experiment as an `ELN Archive` and save the `.eln`
   file to your computer without changing its extension.
1. In NOMAD, create or open a Project and add the exported file under
   **FILES** using **UPLOAD FILES**.
1. NOMAD processes the archive and creates an Entry for each experiment in the
   elabFTW project.

Open an Entry to inspect the parsed data. The `ElabFTW Project Import` section
contains metadata for the experiment, including `experiment_data` and
`experiment_files` subsections.

<b>experiment_data</b> section contains detailed information of the given elabFTW experiment, such as
links to external resources and extra fields. <b>experiment_files</b> section is a list of subsections
containing metadata and additional info of the files associated with the experiment.

### Labfolder integration

Labfolder provides API endpoints for accessing ELN data. NOMAD retrieves and
maps data from your Labfolder instance to a NOMAD schema. The integration
requires the following information:

<i>project_url</i>:
        The URL address to the Labfolder project. It should follow this pattern:
        `https://your-labfolder-server/eln/notebook#?projectIds=your-project-id`. This is used to setup
        the server and initialize the NOMAD schema.

<i>labfolder_email</i>:
        The email used to authenticate. This information is discarded once
        authentication is complete.

<i>password</i>:
        The password used to authenticate. This information is discarded once
        authentication is complete.

      To import Labfolder data into NOMAD:

      1. Create or open a NOMAD Project and select **NEW ENTRY**.
      1. Choose the `Labfolder Project Import` schema, name the Entry, and select
         **CREATE**.
      1. In the new Entry, enter the project URL, email, and password, then save the
         Entry. NOMAD retrieves the project data and populates the Entry.

The `elements` section lists all the data and files in your projects. There are 6 main data types
returned by Labfolder's API: `DATA`, `FILE`, `IMAGE`, `TABLE`, `TEXT` and `WELLPLATE`. `DATA` element is
a special Labfolder element where the data is structured in JSON format. Every data element in NOMAD has a special
`Quantity` called `labfolder_data` which is a flattened and aggregated version of the data content.
`IMAGE` element contains information of any image stored in your Labfolder project. `TEXT` element
contains data from text fields in your Labfolder project.

### Chemotion integration

NOMAD supports importing your data from Chemotion repository via `chemotion` parser. The parser maps
your data that is structured under chemotion schema, into a predefined NOMAD schema. From your Chemotion
repo, you can export your entire data as a zip file which then is used to populate NOMAD schema.

To import Chemotion data into NOMAD:

1. Export your data from Chemotion as a ZIP file and save it to your computer.
1. In NOMAD, create or open a Project and add the ZIP file under **FILES** using
  **UPLOAD FILES**.
1. NOMAD processes the archive and creates an Entry in the Project.

Open the resulting Entry to inspect the parsed data in the `Chemotion Project
Import` section. Other sections are populated when the exported data contains
corresponding information.

If a section contains an image (or attachment) it is appended to the same section under `file` Quantity.

### Openbis integration

openBIS provides API endpoints for interacting with ELN data. NOMAD retrieves,
parses, and maps data from your openBIS instance to a NOMAD schema. The
integration requires the following information:

- **project_url**: The URL address to the Openbis project. It should follow this pattern: `https://openbis.example.com`.
  This is used to set up the server and initialize the NOMAD schema.
- **username**: The username (user credential) to authenticate and log in the user. **Important Note**: this information
  **is discarded** once the authentication process is finished.
- **password**: The password (user credential) to authenticate and log in the user. **Important Note**: this information
  **is discarded** once the authentication process is finished.

#### Import openBIS data into NOMAD

To import data, follow these steps:

1. Create or open a NOMAD Project and select **NEW ENTRY**.
1. Choose the `Openbis Project Import` schema, give the Entry a name, and select
   **CREATE**.
1. In the new Entry, enter the project URL, username, and password, then save
  the Entry. NOMAD retrieves and imports the project data.

The normalizer will search for all entries in your Openbis project and attempt to import them one by one.
