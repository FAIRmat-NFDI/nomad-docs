# How to download data

A common use-case for the NOMAD API is to download large amounts of NOMAD data.
In this how-to guide, we use `curl` and API endpoints
that stream .zip files to download many resources with a single request directly from
the command line.

## Prerequisites

Here is some background information to understand the examples better.

### `curl`

To download resources from a REST API using [`curl`](https://curl.se/){:target="_blank" rel="noopener"},
you can utilize the powerful command-line tool to send HTTP requests and retrieve the desired data.
`curl` provides a simple and efficient way to interact with RESTful APIs,
allowing you to specify the necessary headers, parameters, and authentication details.
Whether you need to download files, retrieve JSON data, or access other resources,
`curl` offers a flexible and widely supported solution for programmatically
fetching data from REST APIs.

Refer to our guide for [auth with `curl`](./auth.md#with-curl).

### Raw files vs processed data

We are covering two types of resources: *raw files* and *processed data*.
The former is organized into backend uploads and subdirectories. Each upload
resource corresponds to a project in the GUI. The organization depends
on how the author was providing the files.
The latter is organized by entries. Each NOMAD entry has corresponding structured data.

Endpoints that target raw files typically contain `raw`, e.g. `uploads/<id>/raw`
or `entries/raw/query`. Endpoints that target processed data contain `archive`
(because we call the entirety of all processed data the NOMAD Archive), e.g.
`entries/<id>/archive` or `entries/archive/query`.

### Entry vs upload

API endpoints for data download either target *entries* or backend *uploads*. For both types
of entities, endpoints for raw files and processed data (as well as searchable metadata)
exist. API endpoint paths start with the entity, e.g. `uploads/<id>/raw` or `entries/<id>/raw`.

## Download a whole project

The API represents a project as an upload resource. To download an entire project,
use its upload ID—the value shown as **Project ID** under **SETTINGS** in the GUI.
In this example, the upload ID is
`wW45wJKiREOYTY0ARuknkA`.

```sh
curl -X GET "{{ nomad_url() }}/v1/uploads/wW45wJKiREOYTY0ARuknkA/raw" -o download.zip
```

This creates a `download.zip` file in the current folder containing the project's
raw-file directory.

The `uploads/<id>/raw` endpoint is only available for published projects. For those,
all raw files have already been
packed into a ZIP file and this endpoint simply lets you download it. This is the simplest
and most reliable download implementation.

Alternatively, you can download specific files or sub-directories. This method is available
for all projects, including unpublished projects.

```sh
curl -X GET "{{ nomad_url() }}/v1/uploads/wW45wJKiREOYTY0ARuknkA/raw/?compress=true" -o download.zip
```

This endpoint looks very similar, but is implemented very differently. Note that we
put an empty path `/` to the end of the URL, plus a query parameter `compress=true`.
The path can be replaced with any directory or file path in the project; `/` denotes the
whole project. The query parameter says that we want to download the whole directory
as a ZIP file instead of an individual file. This traverses all files and
creates a ZIP file on the fly.

## Download raw files matching a query

To download raw files associated with multiple entries, submit a search query to
the `entries/raw/query` endpoint. This example selects entries whose material
contains both titanium and oxygen:

```sh
curl -X POST "{{ nomad_url() }}/v1/entries/raw/query" \
-H 'Content-Type: application/json' \
-d '{
    "query": {
        "results.material.elements": {
            "all": ["Ti", "O"]
        }
    }
}' \
-o download.zip
```

The ZIP file contains the raw files from directories containing the mainfiles of
the matching entries. You can replace the example with any
[How-to guides > ... > Queries](api.md#queries).

Existing dataset links and DOIs are still resolved by NOMAD. To download the
entries from one of these retained backend collections, replace the `query`
object with a query for its DOI:

```json
{
    "query": {
        "datasets.doi": "10.17172/NOMAD/2023.11.17-2"
    }
}
```

You can instead identify an existing dataset by using `datasets.dataset_id`.

This does not necessarily download every file in each matching project. To
download complete projects instead, aggregate the upload IDs for the matching
entries and use the method from the previous section:

```sh
curl -X POST "{{ nomad_url() }}/v1/entries/query" \
-H 'Content-Type: application/json' \
-d '{
    "query": {
        "results.material.elements": {
            "all": ["Ti", "O"]
        }
    },
    "pagination": {
        "page_size": 0
    },
    "aggregations": {
        "upload_ids": {
            "terms": {
                "quantity": "upload_id"
            }
        }
    }
}'
```

The last command prints JSON data containing all the upload IDs. It uses
the `entries/query` endpoint that allows you to query NOMAD's search.
It does not return any results (`page_size: 0`),
but performs an aggregation over all search results and collects the upload IDs
from all entries.

## Download processed data matching a query

Similar to raw files, you can also download processed data. This is also an
entry-based operation based on a query. This time we also specify a `required`
to explain which parts of the processed data, we are interested in:

```sh
curl -X POST "{{ nomad_url() }}/v1/entries/archive/download/query" \
-H 'Content-Type: application/json' \
-d '{
    "query": {
        "results.material.elements": {
            "all": ["Ti", "O"]
        }
    },
    "required": {
        "metadata": {
            "entry_id": "*",
            "mainfile": "*",
            "upload_id": "*"
        },
        "results": {
            "material": "*"
        },
        "run": {
            "system[-1]": {
                "atoms": "*"
            }
        }
    }
}' \
-o download.zip
```

Here we use the `entries/archive/download/query` endpoint. The result is a zip file
with one json file per entry. There are no directories and the files are named
`<entry-id>.json`. To associate the json files with entries, you should require
information that tells you more about the entries, e.g. `required.metadata.mainfile`.
When resolving an existing dataset, the query can select its DOI or ID in the
same way as the raw-file download above.

See also [How-to guides > ... > Access processed data](./archive_query.md).
