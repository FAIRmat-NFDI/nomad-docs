# How to create and publish Projects

A **Project** is the container for files, Entries, collaborators, publication
settings, and an optional DOI.

## Create a Project

1. Open the [NOMAD GUI](https://nomad-lab.eu/prod/v1/gui/v2/){:target="_blank" rel="noopener"}
   and sign in. If you do not have a NOMAD Central account, follow the
   [Create a NOMAD user account](account.md#create-a-nomad-account).
1. Open **PROJECTS** and select **NEW PROJECT**. A prompt appears where you can
   add:

     - a **Project name** (mandatory)
     - a description
     - initial files by drag-and-drop or by browsing your file system with
     **ADD FILES**
     - users or groups to your Project as **Reviewer** or **Coauthor**

1. When you have finished filling in the prompt, select **CREATE**. NOMAD
   creates the Project and opens its **Overview** page.

The Project name can be edited under **SETTINGS** > **General**.

### Add a Project README

To provide a longer, formatted description of the Project, add a file named
`README.md` to the Project root. NOMAD renders its Markdown content below
**All Files** on the Project **Overview** page. You can add the README in the
**New Project** prompt or upload it later.

## Create Entries

You can create Entries in a Project in two ways:

1. **From supported files:** Add files in a format recognized by an installed
   parser. NOMAD processes the files and creates Entries automatically.
1. **From a schema:** On the Project **Overview** page, select **NEW ENTRY**,
   then choose a built-in or custom schema. NOMAD creates an editable
   Electronic Lab Notebook (ELN) Entry that you can complete in the data
   editor.

??? info "Additional Project and Entry metadata"
      Beyond the Project name and description, additional comments and references
      can be added as Project metadata in a file named `nomad.json` or
      `nomad.yaml`. The file can also contain Entry-specific comments. For
      example, a `nomad.json` file can have the following format:

      ```json
      {
         "comment": "Data from a research project",
         "references": ["https://example.org/article"],
         "entries": {
            "path/to/mainfile": {
               "comment": "Metadata for this entry"
            }
         }
      }
      ```

      NOMAD reads this file when processing the Project. Add it before, or in
      the same file transfer as, the mainfiles to which it applies. If you add
      it later, reprocess the Project to apply the metadata to its Entries.

### Create Entries from supported files

<a id="processing-files"></a>

#### How uploaded files become Entries

NOMAD checks the files using the parsers and plugins installed in the current
deployment. When a parser recognizes a file as the primary raw-data source
that defines an Entry, that file becomes the Entry's
[**mainfile**](../../../reference/glossary.md#mainfile). NOMAD then creates and
processes the corresponding Entry. Which file formats are supported therefore
depends on the parsers and plugins installed in the deployment. See
[Explanation > Processing](../../../explanation/processing.md) for a detailed
explanation of file matching and processing.

All Project files remain available under **FILES**, but only recognized
mainfiles produce Entries that appear under **ENTRIES** and can be found in
search. Parsers can also associate other files with a mainfile as **auxiliary
files** for the resulting Entry. A Project must contain at least one
successfully processed Entry before it can be published.

If you added supported files in the **New Project** prompt, the corresponding
Entries are created automatically during Project creation. To create further
Entries from files, open **FILES** and select **UPLOAD FILES**, then choose one
or more files. Alternatively, drag files into the file-list area below
**All Files**.

You can add individual files or package them in a `.zip` or `.tar.gz` file.
NOMAD extracts these compressed bundles and preserves their internal directory
structure. Keep the files for one calculation or experiment together in the
same Project so that the parser can associate them with the same Entry.

For scripted transfers, select the drop-down arrow next to **UPLOAD FILES** and
choose **Upload via API**. The dialog provides an example command for uploading
to the current Project folder.

??? warning "License Compliance for VASP POTCAR Files"

    The VASP license does **not** permit users to freely distribute **POTCAR** files, which are
    considered copyrighted material. To ensure compliance, NOMAD automatically handles POTCAR
    files for you.

    Upon **publication**, NOMAD removes the original POTCAR files and replaces them with
    `POTCAR.stripped` files. The stripped files contain a checksum of the original file
    at the top, followed by metadata headers extracted from the original POTCAR, but not
    the proprietary pseudopotential data. The stripped files can be accessed and downloaded
    by anyone, while the original POTCAR files are automatically removed.

    **Important considerations:**

    - Stripping is filename-based. Ensure "POTCAR" appears in the filename for licensed files.
    - POTCAR files **must be uncompressed** for automated stripping to work. Compressed files (e.g., `POTCAR.gz`) will not be properly processed and may be entirely removed without creating stripped versions.
    - Stripping only occurs upon publication. We strongly recommend **against** temporarily making unpublished uploads publicly visible when they contain licensed material.

    While NOMAD provides this service as a courtesy, **uploaders remain responsible for
    verifying overall license compliance**.

### Create ELN Entries from built-in or custom schemas

An [Electronic Lab Notebook (ELN)](../../../reference/glossary.md#eln) Entry is
a schema-based Entry that you can edit directly in NOMAD. To create an ELN Entry:

1. On the Project **Overview** page, select **NEW ENTRY**. To create the Entry
   in a specific folder instead, open **FILES**, navigate to that folder, and
   select **NEW ENTRY** there.
1. Choose a schema under **BUILT-IN SCHEMAS** or **CUSTOM SCHEMAS**. Custom
   schemas come from schema packages uploaded to the current NOMAD deployment.
   Depending on your access, these can include schemas from this Project, your
   other Projects, or Projects shared or published by other users.
1. Enter a filename and select **CREATE**. NOMAD creates the ELN and opens
   it in the data editor.

**Related pages:** [Enter data with ELNs](eln.md);
[Write a YAML schema package](yaml.md).

## Visibility and access

On the Project **Overview** page, the Project owner can select **SETTINGS** to
manage access.

Under **Collaborators**, use **ADD USER** to add a collaborator and assign one
of these roles:

- **Reviewer** can view the files and Entries in an unpublished Project but
  cannot change them.
- **Coauthor** can view and modify the files and Entries while the Project is
  unpublished.

Select **SAVE** after changing the collaborator list or a role. If group
collaboration is enabled in the deployment, **ADD GROUP** provides the same
role choices for a user group. See
[How-to guides > ... > API Overview > User Groups](../program/api.md#user-groups)
for information about creating and editing groups.

Under **Visibility**, select **Private** or **Public**, then select **SAVE**.
A public, unpublished Project is visible to everyone. Public visibility and a
publication embargo cannot be used together, so keep the Project private if
you intend to publish it under embargo.

## Publish and assign a DOI

Only the Project owner can publish a Project or assign its DOI.

1. Open **ENTRIES** and review every Entry. Confirm that all expected Entries
   are present and that their extracted or entered data are complete and
   correct.
1. In the Project header, select the status button with the drop-down arrow.
   Depending on the current state, it is labelled **Completed**, **Failed**,
   **Processing**, or **Idle**. In the **Processing status** panel, confirm that
   **Matching** found the expected number of Entries, **Parsing** completed
   successfully for every Entry, and **Cleanup** reports no unresolved warnings
   or errors.
1. For an Entry with failed processing, unexpected data, or a concerning
   warning, open the Entry and select **LOGS**. Review the processing messages,
   correct the source data or Entry as needed, and reprocess before publishing.
1. Open **SETTINGS** > **General**.
1. In **Publish**, select **No embargo** or an embargo period. If the Project
   is already publicly visible, the embargo control is disabled; change its
   visibility to **Private** first if you need an embargo.
1. Select **PUBLISH** or **PUBLISH WITH EMBARGO**, then confirm the action.

If processing errors persist or the impact of a warning is unclear, contact
the administrator of your NOMAD deployment before publishing. NOMAD Central
users and NOMAD Oasis administrators who need further assistance can contact
[NOMAD > Support](https://nomad-lab.eu/nomad-lab/support.html){:target="_blank" rel="noopener"}.
Include the Project ID, the affected Entries, and the relevant processing logs
in your request.

Publication is permanent. The Project's files and Entries become read-only
and cannot be edited or deleted. Without an embargo, the data become public
immediately. With an embargo, the Entry metadata are public while access to
the files remains restricted until the embargo ends.

On NOMAD Central, or on a NOMAD Oasis deployment with DataCite integration
enabled, **SETTINGS** > **General** also contains **Digital Object Identifier
(DOI)**. After publishing, select **ASSIGN DOI** and confirm the action. The DOI
is assigned directly to the Project; creating a dataset is not required.

!!! warning
    DOI assignment is irreversible. The DOI remains permanently associated
    with the Project.

!!! note
    DOI controls are only shown on deployments with DataCite integration.
    They may therefore be absent from a NOMAD Oasis.

<a id="upload-limits"></a>

## Project limits

Project limits are configurable and can differ between deployments. The
default NOMAD configuration and NOMAD Central allow:

- a maximum Project size of **32 GiB**;
- at most **10 unpublished Projects** per user.

## Strategies for large amounts of data

Test the workflow first with a small, representative subset of the data.
Review the resulting files and Entries, then delete the test Project if it is
no longer needed.

When data exceed the deployment's Project-size limit, split them across
multiple Projects. Do not split the mainfile and auxiliary files belonging to
one Entry between Projects. The appropriate split therefore depends on how
the data are organized.

For repeatable transfers, choose **Upload via API** from the **UPLOAD FILES**
drop-down menu or automate the backend upload endpoints. These APIs retain
*upload* in their paths and require a
[How-to guides > ... > Programmatic authentication > Create a PAT](../program/auth.md#create-a-pat)
with at least the `uploads:write` permission. The upload endpoint also supports
direct publication through `publish_directly`; use it only after testing the
processing and publication workflow with representative data.

!!! info
    Contact [NOMAD > Support](https://nomad-lab.eu/nomad-lab/support.html){:target="_blank" rel="noopener"}
    before transferring hundreds of gigabytes or requesting an exceptional
    transfer arrangement. Allow time to agree on an appropriate transfer and
    Project layout. Server-side transfers require coordination with NOMAD
    Central operators and are not part of the ordinary end-user workflow.
