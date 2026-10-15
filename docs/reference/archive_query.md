# `ArchiveQuery` client

`nomad.client.ArchiveQuery` searches NOMAD Entries and retrieves selected
parts of their processed archives. This page describes the public constructor,
methods, result formats, and transfer behavior of the client.

```python
ArchiveQuery(
    owner='visible',
    query=None,
    required=None,
    url=None,
    after=None,
    results_max=1000,
    page_size=100,
    batch_size=10,
    username=None,
    password=None,
    retry=1,
    sleep_time=4.0,
    from_api=False,
    semaphore=8,
    max_requests_per_second=20,
)
```

## Selection options

| Option | Default | Description |
| --- | --- | --- |
| `owner` | `'visible'` | Ownership scope applied to both the Entry search and archive retrieval. |
| `query` | `None` | Entries API query. The client sends it to the server without validating the query syntax. |
| `required` | `None` | Archive selection expressed as a required tree. `None` requests the complete archive. |
| `after` | `None` | Opaque Entries API pagination value after which the initial search starts. |
| `results_max` | `1000` | Maximum number of matching Entries to fetch during the lifetime of the object. |

The ownership scopes are:

| Scope | Entries included |
| --- | --- |
| `public` | Published Entries without embargo. No authentication is required. |
| `visible` | Public Entries plus Entries visible to the authenticated user. |
| `all` | Published Entries, including embargoed Entries visible to the authenticated user, plus Entries owned by or shared with that user. |
| `shared` | Entries owned by or shared with the authenticated user. |
| `user` | Entries owned by the authenticated user. |
| `staging` | Unpublished Entries owned by or shared with the authenticated user. |
| `admin` | All Entries. This scope requires an administrator account. |

Except for `public`, a scope may require authentication to return non-public
Entries. Selecting a scope does not grant additional access: the server returns
only Entries that the authenticated user has permission to view. The `admin`
scope returns all Entries only for an administrator account.

## Connection and authentication options

| Option | Default | Description |
| --- | --- | --- |
| `url` | configured client URL | NOMAD API base URL. The constructor accepts URLs ending in `/api` or `/api/v1` and normalizes them to an API v1 URL. |
| `username` | `None` | Username used for password-based authentication. Prefer a personal access token for new integrations. |
| `password` | `None` | Password used with `username`. |
| `from_api` | `False` | With username/password authentication, obtain the token from the NOMAD API instead of contacting Keycloak directly. This fallback is mainly useful when Keycloak cannot be reached or configured. |

The corresponding environment variables are:

- `NOMAD_CLIENT_URL` for the API base URL, such as
  `https://nomad-lab.eu/develop/backend/api`.
- `NOMAD_CLIENT_ACCESS_TOKEN` for a bearer token, including a personal access
  token.

An explicit `url` overrides `NOMAD_CLIENT_URL`. The access token is read from
the client configuration; password-based credentials are supplied through the
`username` and `password` constructor arguments.

## Transfer controls

| Option | Default | Description |
| --- | --- | --- |
| `page_size` | `100` | Number of Entry identifiers requested per search page. It is capped below the API limit and cannot exceed `results_max`. |
| `batch_size` | `10` | Number of Entries requested in each archive-download request. |
| `semaphore` | `8` | Maximum number of concurrent archive-download requests. Values above `10` are capped at `10`. |
| `max_requests_per_second` | `20` | Client-side limit for archive-download requests. |
| `retry` | `1` | Number of retries for selected server errors while fetching Entry identifiers. |
| `sleep_time` | `4.0` | Seconds between fetch retries. |

Use smaller `batch_size` and `semaphore` values when archive responses are
large. Respect deployment-specific rate limits by setting
`max_requests_per_second` conservatively.

The fetch phase retries HTTP 500, 502, and 504 responses according to `retry`
and `sleep_time`. The download phase does not retry within the same method
call. When a download request fails, its Entries are restored to the pending
list and can be retried by calling `download()` or `async_download()` again.
Other unsuccessful fetch responses raise `ValueError` with the server's error
description.

## Methods

### `fetch(number=0)`

Search synchronously and append matching `(entry_id, upload_id)` pairs to the
pending list. `number` is a target rather than a strict limit: because the
search proceeds in pages, the result can include additional pairs up to the
current page boundary and `results_max`. With `number=0`, fetch up to the
remaining `results_max` limit. The return value is the number of pairs added.

### `download(number=0, *, as_plain_dict=False)`

Download Entries from the pending list synchronously. If no Entries have been
fetched, the method fetches first. If `number` exceeds the pending count, it
fetches additional Entries before downloading.

With `number=0`, the method downloads all currently pending Entries; if the
pending list is empty, it fetches and downloads up to the remaining
`results_max` limit.

The default result is `list[EntryArchive]`. With `as_plain_dict=True`, the
result is a list of JSON-like dictionaries.

### `async_fetch(number=0)` and `async_download(number=0, *, as_plain_dict=False)`

Coroutine equivalents of `fetch()` and `download()`. Use them when the caller
already follows an asynchronous control flow. The synchronous methods can also
be called while an event loop is running; the client runs their coroutine work
in a separate thread.

### `entry_list()`

Return the pending list of `(entry_id, upload_id)` pairs. Successful downloads
remove their pairs. Failed download requests restore their pairs to the list.

### `clear()`

Reset fetched identifiers, recorded synchronous download batches, pagination,
and result counts. The same `ArchiveQuery` can then run again from its initial
`after` value.

## Typed and plain results

Typed results are `EntryArchive` objects constructed from the returned JSON.
They provide schema-based attribute access, NumPy arrays, Pint quantities, and
archive-reference resolution. Accessing a plugin-specific section as a typed
object requires its schema package to be installed locally. Use
`archive.m_to_dict()` to serialize an object back to a JSON-compatible
dictionary.

Use `as_plain_dict=True` when schema-aware behavior is unnecessary or when the
local environment does not contain the Entry's schema package. Plain results
retain the serialized archive structure but do not provide typed attributes,
units, or automatic reference resolution.

## Dataframe conversion

`entries_to_dataframe()` flattens archives recorded by synchronous
`download()` calls:

```python
query.entries_to_dataframe(
    keys_to_filter=None,
    resolve_references=False,
    query_selection='last',
)
```

| Argument | Description |
| --- | --- |
| `keys_to_filter` | List of archive-path prefixes. Only flattened columns beginning with one of these prefixes are retained. `None` or an empty list retains every column. |
| `resolve_references` | Resolve archive references before flattening. This can add substantial data to the result. |
| `query_selection` | `'last'` for the latest synchronous download batch, `'all'` for every batch, or a list of zero-based download-call indexes. |

Dataframe conversion expects typed `EntryArchive` results. Do not select a
batch downloaded with `as_plain_dict=True`. Asynchronous downloads are not
recorded for later dataframe conversion; convert those returned objects
directly with your preferred dataframe library.

## Related pages

- {{ nav_link("howto/manage/program/archive_query.md", breadcrumb=True) }} — search, download, and inspect processed data in Python.
- {{ nav_link("howto/manage/program/api.md", breadcrumb=True) }} — query syntax and direct REST API calls.
- {{ nav_link("explanation/data.md", breadcrumb=True) }} — the archive structure and its schemas.
