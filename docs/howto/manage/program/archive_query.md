# How to access processed data

In this guide, you will use the `ArchiveQuery` Python client to search for
NOMAD Entries, download selected parts of their processed archive data, and
work with the results as schema-aware Python objects. You will also learn when
to retrieve plain dictionaries, process results in batches, or use the
asynchronous interface.

## Before you begin

Install the `nomad-lab` Python package as described in
[How-to guides > ... > Install > How to install the NOMAD Python Library](../../oasis/install.md#how-to-install-the-nomad-python-library).

The examples query public data and do not require authentication. By default,
the client connects to NOMAD Central. To use another NOMAD deployment, set its
API base URL before starting Python. For example, to test against the NOMAD
develop deployment:

```sh
export NOMAD_CLIENT_URL="https://nomad-lab.eu/develop/backend/api"
```

## Search and select archive data

An `ArchiveQuery` combines two selections:

- `query` selects the Entries to retrieve using searchable metadata.
- `required` selects the archive sections and quantities to download for each
  matching Entry.

The following query selects public simulation Entries produced with VASP for
materials containing both titanium and oxygen. It downloads identifying
metadata and the normalized material data, while limiting the result to five
Entries:

```python
from nomad.client import ArchiveQuery

archive_query = ArchiveQuery(
    owner='public',
    query={
        'results.method.simulation.program_name': 'VASP',
        'results.material.elements': {'all': ['Ti', 'O']},
    },
    required={
        'metadata': {
            'entry_id': '*',
            'mainfile': '*',
        },
        'results': {
            'material': {
                'chemical_formula_reduced': '*',
            },
        },
    },
    results_max=5,
    page_size=5,
)
```

Use the query syntax described in
[Reference > REST API > Entry queries](../../../reference/api.md#entry-queries).
Request only
the archive data that your analysis needs: a narrowly scoped `required`
selection reduces both server work and transferred data.

## Retrieve and inspect the results

Call `download()` to search for and retrieve the matching archives. If you have
not called `fetch()` first, `download()` performs the search automatically:

```python
archives = archive_query.download()

for archive in archives:
    print(
        archive.metadata.entry_id,
        archive.results.material.chemical_formula_reduced,
    )
```

By default, each result is an `EntryArchive` object. Its attributes follow the
archive schema. Numerical arrays are represented as NumPy arrays, physical
quantities carry Pint units, and archive references can be followed as Python
attributes. Call `archive.m_to_dict()` to serialize a typed archive back to a
JSON-compatible dictionary.

The built-in `metadata` and `results` sections used above are available with
the `nomad-lab` package. To access a plugin-defined archive section as a typed
object, install its matching schema package in the same Python environment.
Otherwise, retrieve it as a plain dictionary as described below.

## Process results in batches

For a larger result set, separate the search from the downloads. `fetch()`
adds matching `(entry_id, upload_id)` pairs to a local pending list, and
`download()` removes successfully retrieved Entries from that list:

```python
batch_query = ArchiveQuery(
    owner='public',
    query={'results.material.elements': 'Ti'},
    required={'metadata': '*'},
    results_max=20,
)

batch_query.fetch(20)
print(batch_query.entry_list())

while batch_query.entry_list():
    batch = batch_query.download(5)
    for archive in batch:
        process(archive)
```

Calling `download(number)` without fetching first is also valid. The client
fetches more matching Entries whenever its pending list contains fewer than
`number` Entries. A failed download request remains pending so that a later
`download()` call can retry it.

For large queries, tune request concurrency and rate limiting conservatively
for the deployment you use. See
[Reference > ArchiveQuery client > Transfer controls](../../../reference/archive_query.md#transfer-controls)
for the relevant options.

## Retrieve plain dictionaries

Use `as_plain_dict=True` when you need JSON-like dictionaries instead of typed
`EntryArchive` objects. This is also useful when your local environment does
not have the plugin schema package used by an Entry:

```python
plain_query = ArchiveQuery(
    owner='public',
    query={'results.material.elements': 'Ti'},
    required={'metadata': '*', 'data': '*'},
    results_max=5,
)

archives = plain_query.download(as_plain_dict=True)
print(archives[0]['metadata']['entry_id'])
```

## Convert schema-aware results to a dataframe

After retrieving schema-aware `EntryArchive` objects with the synchronous
`download()` method, flatten the results into a pandas dataframe:

```python
dataframe = archive_query.entries_to_dataframe(
    keys_to_filter=['metadata', 'results.material'],
)
print(dataframe)
```

By default, the method converts the most recent synchronous `download()`
result. It can instead combine all downloads or select particular download
calls. See
[Reference > ArchiveQuery client > Dataframe conversion](../../../reference/archive_query.md#dataframe-conversion)
for the selection options and limitations.

## Use the asynchronous interface

In asynchronous applications and notebooks, call the coroutine methods
directly:

```python
archive_query = ArchiveQuery(
    owner='public',
    query={'results.material.elements': 'Ti'},
    required={'metadata': '*'},
    results_max=5,
)

await archive_query.async_fetch(5)
archives = await archive_query.async_download(5)
```

The synchronous `fetch()` and `download()` methods also work when an event loop
is already running, including in a Jupyter notebook. They do not require
`nest_asyncio`.

## Access non-public Entries

Create a personal access token as described in
[How-to guides > ... > Authenticate programmatically > Personal Access Tokens](./auth.md#personal-access-tokens)
and make it available to the Python client:

```sh
export NOMAD_CLIENT_ACCESS_TOKEN="<personal-access-token>"
```

Then choose an authenticated ownership scope such as `visible`, `user`,
`shared`, or `staging`. Do not put access tokens directly in source files.

## Complete example

<!-- fmt: off -->
```python
--8<-- "examples/archive/archive_query.py"
```
<!-- fmt: on -->

## Related pages

- {{ nav_link("reference/archive_query.md", breadcrumb=True) }} — constructor options, methods, batching, and result formats.
- {{ nav_link("howto/manage/program/api.md", breadcrumb=True) }} — query syntax and direct REST API calls.
- {{ nav_link("howto/manage/program/download.md", breadcrumb=True) }} — download raw files or processed data with `curl`.
- {{ nav_link("explanation/data.md", breadcrumb=True) }} — how Entries, archives, and schemas relate.
