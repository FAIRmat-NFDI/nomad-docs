# The Graph Structure

## Navigating the Graph Structure

<!-- The previous sections cover how to fetch data from existing data structures, using only isolated "nodes".
To leverage the graph structure capabilities and navigate from one data structure to another, we need to introduce 'edges' to link 'nodes' together. -->

The data structures in NOMAD are inherently linked together.
For example, an upload is a collection of entries, an entry corresponding to an archive, a user group is a collection of users,
each user may be the owner of several uploads, etc.

Thus, it is natural to link these data structures together via **special tokens**.
The following schematic illustrates various NOMAD data structures with the special tokens defining links between them.

![NOMAD graph](./images/graph.svg)

For example, if there is an upload with ID `<example_upload_id>`, and it has an entry with ID `<example_entry_id>`,
the request to fetch the `entry_id` and `entry_create_time` of the entry, together with `upload_create_time` in the upload, would look like this.

```json hl_lines="5"
{
  "uploads": {
    "<example_upload_id>": {
      "upload_create_time": {"m_request": {"directive": "plain"}},
      "entries": {
        "<example_entry_id>": {
          "entry_id": {"m_request": {"directive": "plain"}},
          "entry_create_time": {"m_request": {"directive": "plain"}}
        }
      }
    }
  }
}
```

Here the special token `entries` is used to navigate from the upload to the entry.
If needed, one can further navigate from the entry to the archive, or from the upload to the file system, etc.
This is the essence of the graph: to link data structures together via edges, allowing for complex queries and data retrieval.

??? note "Technical Note"
      These special tokens do not exist in the original documents stored in MongoDB, but are defined by the graph API to establish the relationships between the data structures.

### Fuzzy Fetching

Imagine we start with an upload with a known ID `<example_upload_id>`, and we want to find all entries that belong to this upload.
How can we achieve this without knowing the exact entry IDs?

One can use the special key `*` to represent all entries under the upload as follows:

```json hl_lines="5"
{
  "uploads": {
    "<example_upload_id>": {
      "entries": {
        "*": {
          "entry_id": {"m_request": {"directive": "plain"}},
          "entry_create_time": {"m_request": {"directive": "plain"}}
        }
      }
    }
  }
}
```

!!! warning "Wildcard Usage"
    The `*` wildcard is not universal and only works for **homogeneous** data.
    This means it can only be used to represent `upload_id`, `entry_id`, `dataset_id`, etc., for data that follows a fixed schema (e.g., MongoDB).
    It won't work for archive data, the corresponding metainfo (definitions), and alike.

### Fuzzy Querying

The request configuration allows one to perform fuzzy queries to further filter data before fetching via the `query` and `pagination` fields:

```py hl_lines="4-24"
class RequestConfig(BaseModel):
    # ... other fields omitted for brevity ...

    pagination: None | dict = Field(
        None,
        description="""
        The pagination configuration used for MongoDB search.
        This setting does not propagate to its children.
        For Token.ENTRIES, Token.UPLOADS and Token.DATASETS, different validation rules apply.
        Please refer to `DatasetPagination`, `UploadProcDataPagination`, `MetadataPagination` for details.
        """,
    )
    query: None | dict = Field(
        None,
        description="""
        The query configuration used for either mongo or elastic search.
        This setting does not propagate to its children.
        It can only be defined at the root levels including Token.ENTRIES, Token.UPLOADS and 'm_datasets'.
        For Token.ENTRIES, the query is used in elastic search. It must comply with `WithQuery`.
        For Token.UPLOADS, the query is used in mongo search. It must comply with `UploadProcDataQuery`.
        For Token.DATASETS, the query is used in mongo search. It must comply with `DatasetQuery`.
        For Token.GROUPS, the query is used in mongo search. It must comply with `UserGroupQuery`.
        """,
    )

    # ... other fields omitted for brevity ...
```

!!! note
    To avoid performance issues, the server will paginate the results by default.

To instruct the server to perform a query, one needs to attach a request config with valid `query` and `pagination` (optional) alongside the `m_request` key under the **root** level.
The **root** level is the top-level following the **special tokens**, such as `uploads`, `entries`, etc.

Combined with fuzzy fetching, one can perform filter and fetch.
For example, if one wants to fetch all entries under an upload with a specific parser name, the request would be:

```json hl_lines="6"
{
  "uploads":{
    "<example_upload_id>":{
      "entries":{
        "m_request":{ "query":{ "parser_name":"desired_parser" } },
        "*":{
          "entry_id":{ "m_request":{ "directive":"plain" } },
          "entry_create_time":{ "m_request":{ "directive":"plain" } }
        }
      }
    }
  }
}
```

Both the query and the pagination fields must comply with the underlying models, depending on the specific token.
Details can be found in standard REST documentation, as these models are used in conventional REST endpoints.
