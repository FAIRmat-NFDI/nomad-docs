# Create and publish Projects

A **Project** is the container for files, entries, collaborators, publication
settings, and an optional DOI. The backend APIs still use the term *upload*,
so API endpoints, upload IDs, and related technical documentation retain that
terminology.

## Create a Project

1. Open the [NOMAD GUI](https://nomad-lab.eu/prod/v1/gui/v2/){:target="_blank" rel="noopener"}
   and sign in. If you do not have a NOMAD Central account, follow the
   [account creation instructions](../../../tutorial/overview.md#create-a-nomad-user-account).
2. Open **Projects** and select **New Project**.
3. Enter a **Project name** and, optionally, a description.
4. Optionally, add initial files by dragging them into the dialog or selecting
   **Add files**. You can also add files after creating the Project.
5. Optionally, use **Add User** or **Add Group** to invite collaborators and
   assign each one the **Reviewer** or **Coauthor** role.
6. Select **Create**. NOMAD creates the Project and opens its **Overview** page.

Only the Project name is required. You can therefore create an empty Project
and add data and collaborators later. The name and description can be edited
under **Settings** > **General**.

## Add data to a Project

After creating a Project, you can create entries in two ways:

1. **From supported files:** Add files in a format recognized by an installed
   parser. NOMAD processes the files and creates entries automatically.
2. **From a schema:** Select **New entry**, then choose a built-in or custom
   schema. NOMAD creates an editable entry that you can complete in the data
   editor.

### Create entries from supported files

Which file formats are supported depends on the parsers and plugins installed
in the deployment. You can add individual files or a `.zip` or `.tar.gz`
archive. NOMAD extracts archives and preserves their internal directory
structure.

Keep the files for one calculation or experiment together in the same Project
so that the parser can associate them with the same entry.

You can add initial files while creating the Project. To add files later, open
**Files** and select **Upload files**, then choose one or more files or
archives. You can also drag files onto the Files page. NOMAD processes added
files automatically; files recognized by an installed parser produce entries.

For scripted transfers, select **Upload via API** on the Files page to get a
command for the current Project.

<a id="processing-files"></a>
#### How uploaded files become entries

NOMAD checks the files using the parsers and plugins installed in the current
deployment. When a parser recognizes a file as the primary raw-data source
that defines an entry, that file becomes the entry's
[**mainfile**](../../../reference/glossary.md#mainfile). NOMAD then creates and
processes the corresponding entry.

All Project files remain available under **Files**, but only recognized
mainfiles produce entries that appear under **Entries** and can be found in
search. Parsers can also associate other files with a mainfile as **auxiliary
files** for the resulting entry. A Project must contain at least one
successfully processed entry before it can be published.

!!! warning "VASP POTCAR files"
    VASP `POTCAR` files contain licensed pseudopotential data. Standard NOMAD
    processing creates a stripped representation and, by default, removes the
    original file during processing. The behavior is filename-based and the
    staging policy can be configured by the deployment.

    See the [VASP parser documentation](https://fairmat-nfdi.github.io/nomad-parser-plugins-simulation/parsers/vasp/vasp_about.html#potcar-files-and-license-compliance){:target="_blank" rel="noopener"}
    for the supported filenames, compressed formats, publication behavior,
    and uploader responsibilities.

### Create entries from built-in or custom schemas

To create an editable entry without uploading a parser-supported mainfile:

1. Open **Files** in the Project and navigate to the folder where you want to
   create the entry.
2. Select **New entry**.
3. Choose a schema under **Built-in schemas** or **Custom schemas**. The custom
   schemas available to you depend on the schema packages you can access.
4. Enter a filename and select **Create**. NOMAD adds the `.archive.json`
   extension, creates and processes the file, and opens the resulting entry in
   the data editor.

Creating an entry from a schema is separate from uploading files. When an
uploaded file is recognized as a mainfile, NOMAD creates its entry
automatically; **New entry** is not required.

This section introduces how to start a schema-based entry as part of the
Project workflow. See [Enter data with ELNs](eln.md) for the detailed data-entry
flow and [Write a YAML schema package](yaml.md) for defining custom schemas.

## Visibility and access

The Project owner can manage access under **Settings**.

Under **Collaborators**, use **Add User** to add a collaborator and assign one
of these roles:

- **Reviewer** can view the unpublished Project.
- **Coauthor** can also edit it.

Select **Save** after changing the collaborator list or a role. If group
collaboration is enabled in the deployment, **Add Group** provides the same
role choices for a user group. See the [user-groups API guide](../program/api.md#user-groups)
for information about creating and editing groups.

Under **Visibility**, select **Private** or **Public**, then select **Save**.
A public, unpublished Project is visible to everyone. Public visibility and a
publication embargo cannot be used together, so keep the Project private if
you intend to publish it under embargo.

## Provide entry metadata

Project information and entry metadata are managed separately. Edit the
Project name under **Settings** > **General**. Additional entry metadata, such
as comments and references, can be supplied in a file named `nomad.json` or
`nomad.yaml`.

For example, a `nomad.json` file can provide defaults and mainfile-specific
values:

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

The metadata file is applied when an entry is first processed. Add it before,
or in the same file transfer as, the mainfiles to which it applies.

## Publish and assign a DOI

Only the Project owner can publish a Project or assign its DOI.

1. Confirm under **Entries** that the Project contains at least one
   successfully processed entry.
2. Open **Settings** > **General**.
3. In **Publish**, select **No embargo** or an embargo period. If the Project
   is already publicly visible, the embargo control is disabled; change its
   visibility to **Private** first if you need an embargo.
4. Select **Publish** or **Publish with embargo**, then confirm the action.

Publication is permanent. The Project's files and entries become read-only
and cannot be edited or deleted. Without an embargo, the data become public
immediately. With an embargo, the entry metadata are public while access to
the files remains restricted until the embargo ends.

If the deployment has DataCite integration enabled, **Settings** > **General**
also contains **Digital Object Identifier (DOI)**. After publishing, select
**Assign DOI** and confirm the action. The DOI is assigned directly to the
Project; creating a dataset is not required.

!!! warning
    DOI assignment is irreversible. The DOI remains permanently associated
    with the Project.

!!! note "DOI availability"
    DOI controls are only shown on deployments with DataCite integration.
    They may therefore be absent from a NOMAD Oasis.

<a id="upload-limits"></a>

## Project limits

Project limits are configurable and can differ between deployments. The
default NOMAD configuration allows:

- a maximum Project size of **32 GiB**;
- at most **10 unpublished Projects** per user.

A Project must also contain at least one recognized entry before it can be
published. Check your deployment's guidance if its configured limits differ.

## Strategies for large amounts of data

Test the workflow first with a small, representative subset of the data.
Review the resulting files and entries, then delete the test Project if it is
no longer needed.

When data exceed the deployment's Project-size limit, split them across
multiple Projects. Do not split the mainfile and auxiliary files belonging to
one entry between Projects. The appropriate split therefore depends on how
the data are organized.

For repeatable transfers, use **Upload via API** on the Project's **Files**
page or automate the backend upload endpoints. These APIs retain *upload* in
their paths and require a [personal access token](../program/auth.md#create-a-pat)
with at least the `uploads:write` permission. The upload endpoint also supports
direct publication through `publish_directly`; use it only after testing the
processing and publication workflow with representative data.

!!! info "Large transfers to NOMAD Central"
    Contact [NOMAD support](https://nomad-lab.eu/about/support){:target="_blank" rel="noopener"}
    before transferring hundreds of gigabytes or requesting an exceptional
    transfer arrangement. Allow time to agree on an appropriate transfer and
    Project layout. Server-side transfers require coordination with NOMAD
    Central operators and are not part of the ordinary end-user workflow.
