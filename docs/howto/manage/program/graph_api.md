# How to make Graph API calls

Use the Graph API to retrieve selected fields from related projects, entries,
and archives in one request. This guide covers a known project, a search for
public entries, and retrieval of archive data and file information.

<a id="overview"></a>
<a id="navigating-the-graph-structure"></a>
<a id="existing-data-resources"></a>

For the relationship between resource selection and response structure, see
{{ nav_link("explanation/graph_api.md", breadcrumb=True) }}. The Graph API uses
JSON requests, not GraphQL query syntax.

<a id="what-you-will-learn"></a>
<a id="recommended-preparation"></a>

## Before you begin

You need a NOMAD API base URL and a tool that can send JSON requests, such as
`curl` or Python's `requests`. Obtain the base URL from your deployment's API
dashboard. For NOMAD Central, set:

```sh
export NOMAD_API_URL="https://nomad-lab.eu/backend/api/v1"
```

For another deployment, replace the complete URL, including its path prefix.
For example, the NOMAD develop deployment uses
`https://nomad-lab.eu/develop/backend/api/v1`.

The public-data examples do not require authentication. For non-public data,
create a personal access token with `graph:read` and add an
`Authorization: Bearer <your-token>` header. Follow
{{ nav_link("howto/manage/program/auth.md", breadcrumb=True) }} for token
creation and secure handling. A token does not grant access to other users'
private data.

<a id="basic-data-fetching"></a>

## Retrieve a project's name and creation time

Use the project's **Project ID** as the key under `uploads`. Each GUI project
corresponds to a backend upload resource; the Graph API retains the names
`uploads`, `upload_id`, and `upload_name`.

Save this request as `request.json`, replacing `<project-id>`:

```json
{
  "uploads": {
    "<project-id>": {
      "upload_name": {"m_request": {"directive": "plain"}},
      "upload_create_time": {"m_request": {"directive": "plain"}}
    }
  }
}
```

Send the file to `/graph/query`:

```sh
curl --fail-with-body --silent --show-error \
  "$NOMAD_API_URL/graph/query" \
  -H 'Accept: application/json' \
  -H 'Content-Type: application/json' \
  --data-binary @request.json
```

The response keeps the selected path and replaces the field configurations
with values. For example:

```json
{
  "uploads": {
    "<project-id>": {
      "upload_name": "Example project",
      "upload_create_time": "2026-01-15T12:00:00Z"
    }
  }
}
```

The ID, name, and timestamp depend on the project. For plain retrieval,
`"upload_name": "*"` is shorthand for the explicit `m_request` form above.

For the following tasks, replace the contents of `request.json` and send it
with the same command. Check for `m_errors` in the JSON response as well as an
unsuccessful HTTP status: part of a graph may fail while the request returns
HTTP 200.

<a id="fuzzy-fetching"></a>
<a id="fuzzy-querying"></a>

## List entries in a project

Add `entries` beneath a known project. Use the `"*"` key to apply the same
field selection to each entry on the returned page:

```json
{
  "uploads": {
    "<project-id>": {
      "entries": {
        "m_request": {"pagination": {"page_size": 5}},
        "*": {"entry_id": "*", "mainfile_path": "*"}
      }
    }
  }
}
```

Read entry records from `uploads/<project-id>/entries/<entry-id>`, and page
information from `uploads/<project-id>/entries/m_response/pagination`.
Use the returned `next_page_after_value` as `page_after_value` in the next
request's `m_request.pagination`; stop when there is no next page.

To select only entries matching a parser name, add a `query` alongside
`pagination` in this collection's `m_request`:

```json
{
  "query": {"parser_name": ["^parsers/vasp$"]},
  "pagination": {"page_size": 5}
}
```

This is a case-sensitive regular-expression filter for entries in that
project, not a query over indexed scientific quantities. For those, use
`search`, as below. The supported filters and pagination models are listed in
[Reference > Graph API > Collection queries and pagination](../../../reference/graph_api.md#collection-queries-and-pagination).

<a id="elasticsearch-metadata"></a>

## Find public entries and retrieve their project and archive data

Use `search` when you do not know the entry IDs or need filters on indexed
metadata. Its `m_request.query` contains an entry-search request: `owner`, the
search criteria under another `query`, and optional pagination and field
selection.

Install `requests`, save the following complete example as `query_graph.py`,
and run it with `python query_graph.py`:

```sh
pip install requests
```

<!-- fmt: off -->
```python
--8<-- "examples/docs/graph/query_graph.py"
```
<!-- fmt: on -->

This example selects two public entries. Replace the inner empty `query`
with the criteria you need, using
[Reference > REST API > Entry queries](../../../reference/api.md#entry-queries).
For each result:

- `search/<entry-id>/entry_id` comes from the search index;
- `search/<entry-id>/entry/upload` contains the project's selected fields; and
- `search/<entry-id>/entry/archive/metadata` contains the selected archive data.

Read the next search cursor from `search/m_response/pagination` and pass it
under `search.m_request.query.pagination.page_after_value`. The `"*"` key
applies to the current page, not every matching entry at once.

<a id="accessing-archives"></a>
<a id="nested-fetching"></a>

## Retrieve selected archive data for a known entry

If you already have an entry ID, start with `entries` and follow `archive`;
there is no need to perform a search first:

```json
{
  "entries": {
    "<entry-id>": {
      "archive": {
        "metadata": {"entry_id": "*", "mainfile": "*"}
      }
    }
  }
}
```

Replace or extend the selection beneath `archive` with fields present in the
entry's schema. For example, select quantities beneath `data` for an ELN
entry. Request only the branches you need; fetching a complete archive can
produce a large response.

To retrieve indexed metadata for the same entry, use
`entries/<entry-id>/metadata` instead. This differs from
`entries/<entry-id>/archive/metadata`: the first reads the search index, while
the second reads the stored archive.

<a id="resolving-references"></a>
<a id="controlling-reference-resolution"></a>

### Follow an archive reference

For an entry whose workflow contains input links, request the first input's
`section` with `directive: resolved`:

```json
{
  "entries": {
    "<entry-id>": {
      "archive": {
        "workflow2": {
          "inputs[0]": {
            "section": {
              "m_request": {"directive": "resolved", "resolve_depth": 1}
            }
          }
        }
      }
    }
  }
}
```

Use a reference path that exists in your entry; not every archive has a
workflow or an input. The response keeps a reference at the requested path
and adds its target under `uploads/<upload-id>/entries/<entry-id>/archive`.
Follow that response-local path to inspect the target; do not assume it is
inlined into `section`. See
[Reference > Graph API > Archive references](../../../reference/graph_api.md#archive-references)
for resolution limits and response layout.

<a id="advanced-fetching"></a>
<a id="list-slicing"></a>
<a id="limiting-depth"></a>
<a id="limiting-container-size"></a>
<a id="filtering-unknown-keys"></a>

For list indexing, glob filters, depth, and size limits, use
[Reference > Graph API > Archive selection and limits](../../../reference/graph_api.md#archive-selection-and-limits).

<a id="accessing-definitions"></a>
<a id="basic-usage"></a>
<a id="resolve-dependencies"></a>
<a id="useful-settings"></a>

For schema definitions and their dependencies, use
[Reference > Graph API > Schema definitions](../../../reference/graph_api.md#schema-definitions).

<a id="miscellaneous-functionalities"></a>
<a id="listing-file-information"></a>

## Inspect the files associated with an entry

Use `mainfile` beneath an entry to retrieve file information, not file content:

```json
{
  "entries": {
    "<entry-id>": {"mainfile": "*"}
  }
}
```

The result contains the file's `path`, `size` in bytes, and `m_is: File`.
For a project directory listing, use `uploads/<project-id>/files` with a
directory path and pagination. The syntax is documented in
[Reference > Graph API > File information](../../../reference/graph_api.md#file-information).
To download the files themselves, follow
{{ nav_link("howto/manage/program/download.md", breadcrumb=True) }}.

<a id="user-information"></a>
<a id="further-resources"></a>

## Related pages

- {{ nav_link("explanation/graph_api.md", breadcrumb=True) }} — data sources, traversal, and response assembly.
- {{ nav_link("reference/graph_api.md", breadcrumb=True) }} — resources, selectors, filters, references, definitions, and errors, including `users/me`.
- {{ nav_link("howto/manage/program/api.md", breadcrumb=True) }} — direct REST requests without graph traversal.
- {{ nav_link("howto/manage/program/archive_query.md", breadcrumb=True) }} — bulk archive retrieval and schema-aware Python objects.
