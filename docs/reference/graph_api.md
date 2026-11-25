# Graph API

The Graph API accepts JSON selection trees at `POST /graph/query`, relative to
the built-in API base URL. Public data can be queried anonymously. Personal
access tokens require the `graph:read` scope; resource permissions still apply.
See [Reference > REST API > API discovery and base URLs](api.md#api-discovery-and-base-urls)
for deployment URLs and API discovery.

This reference covers general-purpose graph retrieval. The implementation's
[request configuration model](https://github.com/FAIRmat-NFDI/nomad/blob/develop/nomad/graph/model.py){:target="_blank" rel="noopener"}
and [graph readers](https://github.com/FAIRmat-NFDI/nomad/blob/develop/nomad/graph/graph_reader.py){:target="_blank" rel="noopener"}
define the available options and resource-specific validation. Deployments
can run different backend and schema versions.

## Request and response structure

A request tree contains resource keys, IDs, field names, and `m_request`
configuration objects. For example:

```json
{
  "uploads": {
    "<project-id>": {
      "upload_name": "*",
      "upload_create_time": {"m_request": {"directive": "plain"}}
    }
  }
}
```

`"*"` as a **value** is shorthand for plain retrieval. The corresponding
response has the same `uploads/<project-id>` parent and the two field values.
`"*"` as a **key** is a collection selector, described below.

Configuration beneath a node's `m_request` can retrieve fields implicitly;
explicit child selections can override that configuration. For example,
`{"archive": {"m_request": {"directive": "plain"}}}` requests the complete
archive rather than just its explicitly named children.

| Response key | Meaning |
| --- | --- |
| Resource ID | The selected record or its requested fields. |
| `m_response` | Effective collection query, pagination, or other retrieval information. |
| `m_errors` | Errors encountered while retrieving part of the graph. |
| `uploads` or `metainfo` added at the response root | Targets retrieved while resolving archive or definition references. |

## Resources and traversal keys

| Context | Key | Target |
| --- | --- | --- |
| Request root | `uploads`, `entries`, `users`, `groups`, `datasets` | Resource records keyed by ID. |
| Request root | `search` | Indexed entry metadata, keyed by entry ID. |
| Request root | `metainfo` | Registered schema packages. |
| Project (`uploads/<project-id>`) | `entries` | Entry processing records belonging to the project. |
| Project | `files` | Raw-file directory information. |
| Entry processing record | `upload` | The project's processing record. |
| Entry processing record | `metadata` | The entry's indexed metadata, not its stored archive metadata. |
| Entry processing record | `archive` | The stored archive. |
| Entry processing record | `mainfile` | Mainfile information from the project's raw files. |
| Search hit | `entry` | The corresponding entry processing record. |
| Raw file | `entry` | The associated entry processing record, if the file is recognized as a mainfile. |
| User | `uploads`, `entries`, `datasets` | Collections associated with that user, subject to permissions. |
| Dataset | `entries` | Entry processing records belonging to the dataset, subject to permissions. |
| Archive section | `m_def` | Its metainfo definition. |

`users/me` identifies the authenticated user. For example,
`{"users": {"me": {"uploads": {"*": {"upload_name": "*"}}}}}`
requests a page of that user's projects. It is not an anonymous user lookup.
Explicit user IDs can also be used. User collections are not an unrestricted
directory of every user's private resources.

Graph record fields use `mainfile_path` for the filename string because
`mainfile` is a traversal key. Archive metadata retains the schema's original
`mainfile` field.

## Collection queries and pagination

Configuration belongs on the collection being enumerated, including nested
collections such as `uploads/<project-id>/entries`. It does not belong on an
arbitrary scalar field, nor does a parent's query propagate into its child
collections.

| Collection | `m_request.query` model | `m_request.pagination` model |
| --- | --- | --- |
| `entries` | `EntryQuery`: case-sensitive regular-expression lists under `mainfile`, `parser_name`, and `references` | `EntryProcDataPagination` |
| `uploads` | `UploadProcDataQuery`: upload-processing filters | `UploadProcDataPagination` |
| `datasets` | `DatasetQuery`: `dataset_id`, `dataset_name`, `user_id`, `dataset_type`, `doi`, and `prefix` | `DatasetPagination` |
| `groups` | `UserGroupQuery`: group lookup filters | `UserGroupPagination` |
| `search` | A complete entry-search `Metadata` request, described below | `MetadataPagination` |

For example, this applies a parser-name filter to a project's entries:

```json
{
  "uploads": {
    "<project-id>": {
      "entries": {
        "m_request": {
          "query": {"parser_name": ["^parsers/vasp$"]},
          "pagination": {"page_size": 5}
        },
        "*": {"entry_id": "*", "mainfile_path": "*"}
      }
    }
  }
}
```

The `"*"` key expands over the records on the current page, not every match.
Collection enumeration is paginated even without an explicit page size. Page
metadata is returned under that collection's `m_response.pagination`, including
`total` and, where available, `next_page_after_value`. Pass the returned cursor
unchanged as `page_after_value` for the next request.

Explicit IDs select records directly; they do not enumerate a filtered page.
The allowed collection scope also depends on the starting resource and user.
For example, a project's `entries` collection is restricted to that project's
entries. A root processing-record collection is not a substitute for a public
metadata search; use `search` for that task.

### Search-index queries

`search.m_request.query` is the full entry-search request, not just its filter
expression. The second, inner `query` contains the criteria:

```json
{
  "search": {
    "m_request": {
      "query": {
        "owner": "public",
        "query": {"upload_create_time": {"gte": "2026-01-01"}},
        "pagination": {"page_size": 5},
        "required": {"include": ["entry_id", "upload_id"]}
      }
    },
    "*": {"entry_id": "*", "upload_id": "*"}
  }
}
```

The inner request accepts `owner`, `query`, `pagination`, `required`, and
`aggregations` according to the entry-search model. However, the graph reader
returns hits and pagination, not aggregation results. Use `POST /entries/query`
when you need aggregations in the response. `required` limits fields
loaded from the index; the graph tree then selects fields or relationships
from those hits. It does not select stored archive data. Keep `entry_id`
available when following the `entry` edge.

If both `m_request.query.pagination` and `m_request.pagination` are set, the
pagination inside `query` takes precedence. The effective page information
is returned at `search.m_response.pagination`.

For criteria, ownership, and aggregation contracts, consult
{{ nav_link("reference/api.md", breadcrumb=True) }} and the deployment's
`POST /entries/query` model. Explicitly set `owner` rather than relying on a
default that changes with authentication.

Deeply nested indexed fields can be selected with a nested graph tree. For a
known entry, `entries/<entry-id>/metadata` provides indexed metadata at that
location. Stored archives instead require `entries/<entry-id>/archive`, or
`search/<entry-id>/entry/archive` when starting from search hits.

## Wildcards and field filters

The older labels *fuzzy fetching* and *fuzzy querying* mean collection wildcard
selection and collection filtering respectively. They are not approximate
text-search operators.

| Syntax | Meaning |
| --- | --- |
| `"field": "*"` | Retrieve that field with the `plain` directive. |
| `"*": {"entry_id": "*"}` in an entry collection | Apply the child selection to each entry on the page. |
| `"m_request": {"include": ["*name*"]}` | Implicitly retrieve immediate fields whose names match a glob. |
| `"m_request": {"exclude": ["processing_logs"]}` | Implicitly retrieve immediate fields except those matching the glob. |

A collection `"*"` key is not supported as an archive or definition field
name. To retrieve an archive section's fields implicitly, use a plain
`m_request`, optionally with `include` or `exclude`.

Only one of `include` and `exclude` may be set in a configuration. Their glob
patterns select immediate field names, not arbitrary descendant paths. After
selecting a child container, the same name filter is not reapplied recursively
to all its descendants. Put another filter on a deeper section to constrain
that section's fields. Other inherited settings can be overridden by a child;
`inherit_from_parent: false` starts that child's configuration from defaults.

## Archive selection and limits

Explicit archive paths follow the entry's installed schema. Quantity names
and references are not necessarily the same across plugins or schema versions.

| Option | Behavior |
| --- | --- |
| `directive: plain` | Return the selected data without following archive references. |
| `directive: resolved` | Follow selected archive references, subject to limits and access permissions. |
| `index: [i]`, or a field name such as `inputs[0]` | Select a zero-based list position. Negative indices count from the end. |
| `index: [start, end]`, or `inputs[0:2]` | Select a range with an **inclusive** end: `0:2` requests positions 0, 1, and 2, unlike Python slicing. |
| `depth` | Bound traversal into nested archive containers. Primitive values are not replaced solely because of the depth limit. |
| `max_list_size`, `max_dict_size` | Limit implicit container retrieval by replacing oversized containers with internal markers; these options do not truncate them to the first N items. |
| `resolve_depth` | Bound reference traversal rather than ordinary container nesting. |

Index-selected lists preserve their original positions. Unrequested positions
before a returned item can appear as `null`; clients must not treat the result
as a compacted list.

Omitted container data can be represented by a string beginning with
`__INTERNAL__:` followed by an archive location. This is a retrieval marker,
not an HTTP URL or a guarantee that the target data is present elsewhere in
the response. These are traversal controls, not hard response-size caps:
explicit child selections can still retrieve data from a limited container.
Narrower explicit paths can retrieve data without requesting the entire container.

For backends supporting archive pagination, `pagination` on a repeating
subsection accepts `page_size`, `page`, or `page_containing`. `page` starts at
1; `page_containing` is a zero-based item index and cannot be combined with
`page`. The result records pagination at the parent section's
`m_response.subsection_lists.<subsection-name>.pagination`. Schema properties
are not themselves paginated. Explicit child requests do not inherit the
parent's selected page; implicitly traversed repeating subsections inherit
the page size.

Archive queries do not accept a collection-style `query`. Use metadata search
to select entries, then traverse their archives.

## Archive references

Plain retrieval preserves an archive reference string. `directive: resolved`
retrieves the target and rewrites the reference to a response-local path such
as:

```text
uploads/<upload-id>/entries/<entry-id>/archive/<section-path>
```

This target can be added at the response root even when the request starts at
`entries` or `search`. Local references and references to other entries use
the same response-root convention. Target retrieval can fail independently,
for example when the user lacks permission to read it.

`resolve_depth: 1` limits resolution to the first reference hop; it does not
mean one level of nested dictionaries. `depth` and container-size limits
remain separate controls. With no resolution-depth limit, resolving a branch
can fetch further references and create a much larger response.

| Additional option | Behavior |
| --- | --- |
| `always_rewrite_references` | Normalize reference paths even for plain retrieval; it does not by itself retrieve their targets. |
| `resolve_type` | Interpret a selected identifier as `upload`, `entry`, `user`, or `dataset`. Leave unset for ordinary archive data. |
| `resolve_inplace` | Deprecated; current backends force it to `false`. Targets are not inlined at the original reference field. |

## Schema definitions

`m_def` beneath an archive section retrieves its definition. For example:

```json
{
  "entries": {
    "<entry-id>": {
      "archive": {
        "data": {
          "m_def": {"m_request": {"directive": "plain"}}
        }
      }
    }
  }
}
```

Use a section present in the archive; `data` is not populated in every entry.
Definitions can be written to `metainfo/<package-name>/section_definitions`
for installed schema packages or to an archive's `definitions` subtree for
entry-defined schemas. The returned `m_def` describes the response-local
definition location; clients must not assume a fixed package or section index.

| Option | Behavior |
| --- | --- |
| `include_definition: none` | Do not automatically add section definitions; default. Explicit `m_def` selections remain possible. |
| `include_definition: specialized_only` | Include specialized definitions identified by the archive section. |
| `include_definition: both` | Include definitions for standard and specialized sections. |
| `export_whole_package` | Export the containing schema package rather than only the selected definition. |
| `m_def_format: short` | On backends supporting it, return a compact qualified-name/tag reference instead of the full `m_def` representation; implicitly enables definition inclusion. |

Definition references such as `base_sections` can be resolved with
`directive: resolved`; depth and resolution limits bound the result. Definition
reader `include` and `exclude` settings filter exported package names, not
archive quantity names. The root `metainfo` resource provides access to the
registered package collection.

## File information

`uploads/<project-id>/files` lists a project's raw-file tree.
`entries/<entry-id>/mainfile` starts at the entry's mainfile. These return
information, not file bytes:

| Field | Meaning |
| --- | --- |
| `m_is` | `File` or `Directory`. |
| `path` | Path within the project's raw files. |
| `size` | File size in bytes. |
| `m_response.pagination` | Directory listing page information. |

Explicit path components can be nested under `files`; `".."` navigates to a
parent within the project's file tree. A listing can be bounded with
`m_request.pagination`, validated as `RawDirPagination`. File access is checked
separately from search-metadata visibility. For file contents, use the download
endpoints rather than the Graph API.

## Errors and partial results

Malformed configuration can return HTTP 400; other invalid graph requests
can return HTTP 422. Authentication and authorization can fail before graph
retrieval. An HTTP 200 response can still contain `m_errors` at the affected
reader's result root, including beneath a resource or archive.

Error records include `error_type` and `message`. Types include `NOACCESS`,
`NOTFOUND`, `ARCHIVEERROR`, and `GENERAL`. Check for these before interpreting
a missing field as absent source data. A successful search does not establish
that every requested archive, file, reference, or definition was retrieved.

## Related pages

- {{ nav_link("howto/manage/program/graph_api.md", breadcrumb=True) }} — common retrieval tasks and a complete Python example.
- {{ nav_link("explanation/graph_api.md", breadcrumb=True) }} — why resource paths, field selection, and response assembly differ.
- {{ nav_link("reference/api.md", breadcrumb=True) }} — shared API conventions and entry-search syntax.
