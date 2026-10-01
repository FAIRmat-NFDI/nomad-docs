# How to import data from external ELNs

This guide explains how to import data from third-party electronic lab notebooks
(ELNs) into NOMAD using integration parsers and schemas.

The plugin
[nomad-external-eln-integrations](https://github.com/FAIRmat-NFDI/nomad-external-eln-integrations){:target="_blank" rel="noopener"}
provides the integrations described here: a generic importer for `.eln`
files, and dedicated integrations for elabFTW, Labfolder, Chemotion, and
openBIS. For `.eln` files, elabFTW, and Chemotion, you upload an exported file
that NOMAD parses. For Labfolder and openBIS, you create a schema-based Entry and provide
the connection details for the external system.

!!! note

    The plugin is part of the default NOMAD distribution. On a NOMAD Oasis
    built from a custom distribution, an administrator must install
    `nomad-external-eln-integrations` before these integrations are available.

## ELN file format

The
[ELN file format](https://github.com/TheELNConsortium/TheELNFileFormat){:target="_blank" rel="noopener"}
is a ZIP-based exchange format for experimental results and data. A `.eln` file
bundles structured metadata with the associated data files so that records can
be transferred between compatible ELNs and other research data systems,
including NOMAD.

## Generic `.eln` import

NOMAD can import `.eln` files exported by any ELN that follows the ELN file
format, for example Kadi4Mat, SampleDB, PASTA, or RSpace. Files exported from
elabFTW are handled by the dedicated
[elabFTW integration](#elabftw-integration) instead.

To import a `.eln` file into NOMAD:

1. In your ELN, export the records you want to transfer in the ELN file
   format and save the `.eln` file to your computer without changing its
   extension.
2. In NOMAD, create or open a Project and add the exported file under
   **FILES** using **UPLOAD FILES**.
3. NOMAD processes the `.eln` file and creates an Entry for each record
   (experiment) in the exported file. Each Entry is named after the record's
   title.

Open an Entry to inspect the parsed data in the `ELN Import` section. Because
ELNs export different amounts of information, the importer maps the fields
that the ELN file format defines for all tools:

- **Record metadata**: title, description, main content, author, creation
  and modification dates, keywords, identifier, category, rating, and the URL
  of the record in the source ELN. `source_software` names the ELN that
  produced the file.
- **extra_fields**: tool-specific fields that have no dedicated Quantity,
  stored as JSON.
- **files**: a subsection for each file of the record, with its name, format,
  size, and checksum, and a link to the file in the Project.
- **comments**: comments made on the record, with their author and date.

## elabFTW integration

elabFTW can export one or more experiments in the ELN file format.

To import elabFTW data into NOMAD:

1. In elabFTW, export your data as an **ELN Archive** and save the `.eln`
   file to your computer without changing its extension.
2. In NOMAD, create or open a Project and add the exported file under
   **FILES** using **UPLOAD FILES**.
3. NOMAD processes the `.eln` file and creates an Entry for each experiment in
   the exported file.

Open an Entry to inspect the parsed data. The `ELabFTW Project Import`
section contains metadata for the experiment, including
`experiment_data` and `experiment_files` subsections.

The **experiment_data** section contains detailed information about the given
elabFTW experiment, such as links to external resources and extra fields.
The **experiment_files** section is a list of subsections containing
metadata and additional information about the files associated with the experiment.

## Labfolder integration

Labfolder provides API endpoints for accessing ELN data. NOMAD retrieves and
maps data from your Labfolder instance to a NOMAD schema. The integration
requires the following information:

- **project_url**: The URL address to the Labfolder project. It should follow
  this pattern:
  `https://your-labfolder-server/eln/notebook#?projectIds=your-project-id`.
  This is used to set up the server and initialize the NOMAD schema.
- **labfolder_email**: The email used to authenticate. This information is
  discarded once authentication is complete.
- **password**: The password used to authenticate. This information is
  discarded once authentication is complete.

To import Labfolder data into NOMAD:

1. Create or open a NOMAD Project and select **NEW ENTRY**.
2. Choose the `Labfolder Project Import` schema, name the Entry, and select
   **CREATE**.
3. In the new Entry, enter the project URL, email, and password, then save
   the Entry. NOMAD retrieves the project data and populates the Entry.

Each Labfolder entry in your project appears under `entries`, and its
`elements` subsection lists the data and files of that entry. NOMAD imports
six element types returned by Labfolder's API:

- `TEXT`: content of text fields.
- `FILE`: attached files, which NOMAD downloads into the Project.
- `IMAGE`: images, which NOMAD downloads into the Project.
- `TABLE`: tables, stored as JSON content.
- `DATA`: structured data elements. NOMAD also provides `labfolder_data`, a
  flattened and aggregated version of the data content.
- `WELL_PLATE`: well-plate templates and their content.

To fetch the project again after changes in Labfolder, enable
`resync_labfolder_repository`, enter your email and password again, and save
the Entry.

## Chemotion integration

NOMAD supports importing your data from a Chemotion repository via the
`chemotion` parser. The parser maps your data, which is structured under
Chemotion schema, into a predefined NOMAD schema. From your Chemotion repository,
you can export your entire data set as a ZIP file, which is then used to
populate the NOMAD schema.

To import Chemotion data into NOMAD:

1. Export your data from Chemotion as a ZIP file and save it to your computer.
2. In NOMAD, create or open a Project and add the ZIP file under **FILES**
   using **UPLOAD FILES**.
3. NOMAD processes the archive and creates an Entry in the Project.

Open the resulting Entry to inspect the parsed data in the `Chemotion Project
Import` section. Other sections are populated when the exported data contains
corresponding information.

If a section contains an image or attachment, it is appended to the same
section under the `file` Quantity.

## openBIS integration

openBIS provides API endpoints for interacting with ELN data. NOMAD
retrieves, parses, and maps data from your openBIS instance to a NOMAD
schema. The integration requires the following information:

- **project_url**: The URL address of the openBIS instance. It should follow
  this pattern: `https://openbis.example.com`. This is used to set up the
  server and initialize the NOMAD schema.
- **username**: The username used to authenticate. This information is
  discarded once authentication is complete.
- **password**: The password used to authenticate. This information is
  discarded once authentication is complete.

To import openBIS data into NOMAD:

1. Create or open a NOMAD Project and select **NEW ENTRY**.
2. Choose the `Openbis Project Import` schema, give the Entry a name, and
   select **CREATE**.
3. In the new Entry, enter the project URL, username, and password, then
   save the Entry. NOMAD retrieves and imports the project data.

NOMAD imports all spaces, projects, and experiments that your account can
access into this Entry, together with the experiment attachments.

## Related pages

- {{ nav_link("howto/manage/gui/upload.md", breadcrumb=True) }}
- {{ nav_link("tutorial/eln/built_in_templates.md", breadcrumb=True) }}
