# How to make Graph-Style API Calls

## What you will learn

- How to implement flexible and accurate data fetching with a [GraphQL](https://graphql.org/){:target="_blank" rel="noopener"}-like API.

## Recommended preparation

- [Tutorial > Accessing data via API](../../../tutorial/access_api.md)

- [API Overview](./api.md)

## Further resources

- [GraphQL](https://graphql.org/){:target="_blank" rel="noopener"}

## Overview

While REST works well for simple data fetching, it often requires multiple requests when building complex pages, since each endpoint provides a fixed response format. Hence queries may under- or over-fetch with respect to the requested data. GraphQL addresses this by letting clients request exactly the fields they need across related resources in a single query, reducing round trips.

NOMAD mimics this behaviour with a GraphQL-like API, available at the `/graph/query` endpoint (see the [NOMAD API Dashboard](https://nomad-lab.eu/prod/v1/api/v1/extensions/docs){:target="_blank" rel="noopener"}).

??? note "Technical Note"
    The implementation can be categorized as a GraphQL-like API powered by the REST-style framework FastAPI, rather than GraphQL itself.
    This architectural choice allows for NOMAD's support of dynamic schemas, circumventing GraphQL's static schema requirements.

## Basic Data Fetching

Imagine there is an example upload with the upload ID `<example_upload_id>`. The metadata of this upload is stored in MongoDB.

If one uses the endpoint `/uploads/{upload_id}` to fetch the upload metadata (see [NOMAD API Dashboard](https://nomad-lab.eu/prod/v1/api/v1/extensions/docs){:target="_blank" rel="noopener"}),
the response would look like:

```json
{
  "uploads":{
    "<example_upload_id>":{
      "process_running":true,
      "current_process":"process_upload",
      "process_status":"WAITING_FOR_RESULT",
      "last_status_message":"Waiting for results (level 0)",
      "complete_time":"2025-05-27T10:03:54.115000",
      "upload_id":"<example_upload_id>",
      "upload_name":"Free energy simulation",
      "upload_create_time":"2025-05-27T10:03:35.048000",
      "published":false,
      "with_embargo":false,
      "embargo_length":0,
      "license":"CC BY 4.0"
    }
  }
}
```

What if you would like the response to return only `upload_name`?
With GraphQL, one simply needs to '**ask for what you need**', following the structure of the data.
Such a request would look like:

```json
{
  "uploads":{
    "<example_upload_id>":{
      "upload_name":"I want this!",
    }
  }
}
```

But it is not practical to use a string to express potentially complex intentions.
Instead, we want to use a more structured way to express the request.
To this end, NOMAD defines a request configuration model ([RequestConfig]) (sometimes referred to as 'config' or 'request config'):

```py
class RequestConfig(BaseModel):
    """
    A class to represent the query configuration.
    An instance of `RequestConfig` shall be attached to each required field.
    The `RequestConfig` is used to determine the following.
        1. Whether the field should be included/excluded.
        2. For reference, whether the reference should be resolved, and how to resolve it.
    Each field can be handled differently.
    """

    directive: DirectiveType = Field(
        DirectiveType.plain,
        description="""
        Indicate whether to include or exclude the current quantity/section.
        References can be resolved using `resolved`.
        The `*` is a shortcut of `plain`.
        """,
    )

    # ... other fields omitted for brevity ...
```

The complete definition of `RequestConfig` can be found in [`nomad/graph/model.py`](https://github.com/FAIRmat-NFDI/nomad/blob/develop/nomad/graph/model.py){:target="_blank" rel="noopener"}.

To fetch the desired field, the `RequestConfig` can be attached under the key `m_request`:

```json hl_lines="4"
{
  "uploads":{
    "<example_upload_id>":{
      "upload_name":{"m_request":{"directive":"plain"}}
    }
  }
}
```

The `plain` directive tells the server to include the field in the response.

Now it is possible to fetch a collection of desired quantities from the upload metadata.
For example, if one wants to fetch the `upload_name` and `upload_create_time`, the request would be:

```json
{
  "uploads":{
    "<example_upload_id>":{
      "upload_name":{"m_request":{"directive":"plain"}},
      "upload_create_time":{"m_request":{"directive":"plain"}}
    }
  }
}
```

### Existing Data Resources

There are a few existing data resources (called documents) stored in MongoDB (see [NOMAD API Dashboard](https://nomad-lab.eu/prod/v1/api/v1/extensions/docs){:target="_blank" rel="noopener"} for more details):

1. `uploads`: The metadata of an upload, including, `upload_id`, `upload_name`, `main_author`, etc.
2. `entries`: The metadata of an entry, including, `entry_id`, `entry_create_time`, `mainfile`, etc.
3. `datasets`: The metadata of a dataset, including, `dataset_id`, `dataset_name`, `user_id`, etc.
4. `groups`: The metadata of a user group, including, `owner`, `members`, etc.

One can apply the same logic to fetch data from these structures.
For example, to fetch the `entry_id` and `entry_create_time` of an entry with ID `<example_entry_id>`, the request would look like this:

```json
{
  "entries":{
    "<example_entry_id>":{
      "entry_id":{"m_request":{"directive":"plain"}},
      "entry_create_time":{"m_request":{"directive":"plain"}}
    }
  }
}
```

The top-level keys should be one of `uploads`, `entries`, `datasets`, or `groups` to indicate which data resource to query.

## Navigating the Graph Structure

<!-- The previous sections cover how to fetch data from existing data structures, using only isolated "nodes".
To leverage the graph structure capabilities and navigate from one data structure to another, we need to introduce 'edges' to link 'nodes' together. -->

The data structures in NOMAD are inherently linked together.
For example, an upload is a collection of entries, an entry corresponding to an archive, a user group is a collection of users,
each user may be the owner of several uploads, etc.

Thus, it is natural to link these data structures together via **special tokens**, acting as edges of a graph containing the NOMAD data structures as nodes.
The following schematic illustrates this graph structure:

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

!!! warning "Attention"
    The `*` wildcard is not universal and only works for fixed, NOMAD-wide schemas.
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

Both the query and the pagination fields must comply with the underlying models, depending on the specific token (see [NOMAD API Dashboard](https://nomad-lab.eu/prod/v1/api/v1/extensions/docs){:target="_blank" rel="noopener"}).

## Accessing Archives

The [Basic Data Fetching](#basic-data-fetching) functionality can be extended to fetching NOMAD archives.
An archive is the processed data of an entry, which is stored on the file system as a binary file.
Each archive thus corresponds to an entry, and the corresponding entry ID can be used as the unique identifier to access the archive.
In the graph system, the archive is linked to the corresponding entry via the special token `archive`.
Thus, to fetch the contents of an archive with entry ID `<example_entry_id>`, one can use the following query:

```json hl_lines="4-6"
{
   "entries":{
      "<example_entry_id>":{
         "archive":{
            "m_request":{ "directive":"plain" }
         }
      }
   }
}
```

The `plain` directive means 'just return the data as it is'. Other directives are introduced in the following sections.

In the following, let's use the random entry id `x36WdKPMctUOkjXMyV8oQq2zWcSx` to make things more concrete. Our request to fetch the archive becomes:

```json hl_lines="3-6"
{
   "entries":{
      "x36WdKPMctUOkjXMyV8oQq2zWcSx":{
         "archive":{
            "m_request":{ "directive":"plain" }
         }
      }
   }
}
```

This request can be perform in practice with `curl`:

```bash
curl -X 'POST' \
'https://nomad-lab.eu/prod/v1/api/v1/graph/query' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
"entries":{ "x36WdKPMctUOkjXMyV8oQq2zWcSx":{ "archive":{ "m_request":{ "directive":"plain" } } } }
}'
```

### Nested Fetching

The archive is `JSON` compatible, which means it is effectively a `JSON` object, with a tree-like structure.
Thus, one can apply the exact same fetching logic as in [Accessing Archives](#accessing-archives), while 'expressing' the intention to fetch data from any level of the tree.
For example, if one wants to fetch `n_quantities` under `metadata`, a subsection of the archive root, the request would be:

```json hl_lines="6"
{
   "entries":{
      "x36WdKPMctUOkjXMyV8oQq2zWcSx":{
         "archive":{
            "metadata":{
               "n_quantities":{ "m_request":{ "directive":"plain" } }
            }
         }
      }
   }
}
```

The response of the above request is:

```json hl_lines="6"
{
   "entries":{
      "x36WdKPMctUOkjXMyV8oQq2zWcSx":{
         "archive":{
            "metadata":{
               "n_quantities":12427
            }
         }
      }
   }
}
```

Note that the response and the request have the same structure, with the intended data returned in lieu of the response config.

### Advanced Fetching

#### List Slicing

If the target data is a list, it is possible to extract a slice of the list by using the `index` field in the request configuration.

The following request fetches the **second** (0-indexed) element of the `processing_logs` list in the archive of the entry with ID `x36WdKPMctUOkjXMyV8oQq2zWcSx`:

```json hl_lines="6"
{
   "entries":{
      "x36WdKPMctUOkjXMyV8oQq2zWcSx":{
         "archive":{
            "processing_logs":{
               "m_request":{ "directive":"plain", "index":[ 1 ] }
            }
         }
      }
   }
}
```

The exact data will be returned in the corresponding position.
Since the first element is not requested, it will be `null` in the response:

```json hl_lines="6-17"
{
   "entries":{
      "x36WdKPMctUOkjXMyV8oQq2zWcSx":{
         "archive":{
            "processing_logs":[
               null,
               {
                  "event":"Reading force field from tpr not yet supported for Gromacs 2024. Interactions will not be stored",
                  "proc":"Entry",
                  "process":"process_entry",
                  "process_worker_id":"RhqUJg02RQ-06EReb8BWZA",
                  "parser":"atomisticparsers:gromacs_parser_entry_point",
                  "step":"atomisticparsers:gromacs_parser_entry_point",
                  "logger":"nomad.processing",
                  "timestamp":"2025-05-27 09:39.20",
                  "level":"WARNING"
               }
            ]
         }
      }
   }
}
```

Apart from using the `index` field, one can alternatively use the indexing syntax in the key.
For example, the above request can be equivalently written as:

```json hl_lines="5"
{
   "entries":{
      "x36WdKPMctUOkjXMyV8oQq2zWcSx":{
         "archive":{
            "processing_logs[1]":{ "m_request":{ "directive":"plain" } }
         }
      }
   }
}
```

This format allows flexible nesting.

!!! tip
    **Range Slicing:** It is possible to assign both start and end indices to the `index` field.
    For example, `index: [1, 3]` will return the second to the fourth elements (both inclusive).
    Using the indexing key, it is equivalent to `key[1:3]`.

#### Limiting Depth

Sometimes, it is only necessary to know what the archive contains, without needing to fetch all the data.
In such cases, one can limit the depth of the request by using the `depth` field in the request configuration.
The following request fetches the archive of the entry `x36WdKPMctUOkjXMyV8oQq2zWcSx` with a depth limit of 1:

```json hl_lines="7"
{
   "entries":{
      "x36WdKPMctUOkjXMyV8oQq2zWcSx":{
         "archive":{
            "m_request":{
               "directive":"plain",
               "depth":1
            }
         }
      }
   }
}
```

The response will contain only the top-level fields of the archive, without any nested data.

```json hl_lines="5-9"
{
   "entries":{
      "x36WdKPMctUOkjXMyV8oQq2zWcSx":{
         "archive":{
            "processing_logs":"__INTERNAL__:../uploads/RzWMitKESo2dQmuE6uQB-Q/archive/x36WdKPMctUOkjXMyV8oQq2zWcSx#/processing_logs",
            "run":"__INTERNAL__:../uploads/RzWMitKESo2dQmuE6uQB-Q/archive/x36WdKPMctUOkjXMyV8oQq2zWcSx#/run",
            "workflow2":"__INTERNAL__:../uploads/RzWMitKESo2dQmuE6uQB-Q/archive/x36WdKPMctUOkjXMyV8oQq2zWcSx#/workflow2",
            "metadata":"__INTERNAL__:../uploads/RzWMitKESo2dQmuE6uQB-Q/archive/x36WdKPMctUOkjXMyV8oQq2zWcSx#/metadata",
            "results":"__INTERNAL__:../uploads/RzWMitKESo2dQmuE6uQB-Q/archive/x36WdKPMctUOkjXMyV8oQq2zWcSx#/results"
         }
      }
   }
}
```

The values of each field will be replaced by internal reference strings to indicate that the data is available but not fetched.

There is one exception:
If the value is a primitive (like a string, number, boolean, etc.), it is always returned as is.
This is because generating internal reference strings for primitive values makes little sense and often has a negative impact on performance.

#### Limiting Container Size

Some archives may contain large lists or dictionaries, and not all of them may be needed.
In such cases, one can limit the size of containers by using `max_list_size` and `max_dict_size` fields in the request configuration.
The following request fetches the data with a maximum list size of 3:

```json hl_lines="9"
{
   "entries":{
      "x36WdKPMctUOkjXMyV8oQq2zWcSx":{
         "archive":{
            "metadata":{
               "optimade":{
                  "m_request":{
                     "directive":"plain",
                     "max_list_size":3
                  }
               }
            }
         }
      }
   }
}
```

The response will contain only lists with a maximum of 3 elements, with longer lists being replaced by internal reference strings:

```json hl_lines="44 46"
{
   "entries":{
      "x36WdKPMctUOkjXMyV8oQq2zWcSx":{
         "archive":{
            "metadata":{
               "optimade":{
                  "elements":[
                     "K",
                     "S",
                     "W"
                  ],
                  "nelements":3,
                  "elements_ratios":[
                     0.007425742574257425,
                     0.0024752475247524753,
                     0.9900990099009901
                  ],
                  "chemical_formula_descriptive":"K3SW400",
                  "chemical_formula_reduced":"K3SW400",
                  "chemical_formula_hill":"K3SW400",
                  "chemical_formula_anonymous":"A400B3C",
                  "dimension_types":[
                     1,
                     1,
                     1
                  ],
                  "lattice_vectors":[
                     [
                        35.59059935653863,
                        0,
                        0
                     ],
                     [
                        0,
                        35.59059935653863,
                        0
                     ],
                     [
                        0,
                        0,
                        38.11340132386931
                     ]
                  ],
                  "cartesian_site_positions":"__INTERNAL__:../uploads/RzWMitKESo2dQmuE6uQB-Q/archive/x36WdKPMctUOkjXMyV8oQq2zWcSx#/metadata/optimade/cartesian_site_positions",
                  "nsites":404,
                  "species_at_sites":"__INTERNAL__:../uploads/RzWMitKESo2dQmuE6uQB-Q/archive/x36WdKPMctUOkjXMyV8oQq2zWcSx#/metadata/optimade/species_at_sites",
                  "structure_features":[

                  ],
                  "species":[
                     {
                        "name":"W",
                        "chemical_symbols":[
                           "W"
                        ],
                        "concentration":[
                           1
                        ]
                     },
                     {
                        "name":"S",
                        "chemical_symbols":[
                           "S"
                        ],
                        "concentration":[
                           1
                        ]
                     },
                     {
                        "name":"K",
                        "chemical_symbols":[
                           "K"
                        ],
                        "concentration":[
                           1
                        ]
                     }
                  ]
               }
            }
         }
      }
   }
}
```

The `max_dict_size` field works similarly for dictionaries: If the dictionary has more than the specified number of keys, it will be replaced by an internal reference string.

#### Filtering Unknown Keys

By providing either `include` or `exclude` fields in the request configuration, one can filter the keys of the archive:

```json hl_lines="9"
{
   "entries":{
      "x36WdKPMctUOkjXMyV8oQq2zWcSx":{
         "archive":{
            "metadata":{
               "optimade":{
                  "m_request":{
                     "directive":"plain",
                     "include":[ "*element*" ]
                  }
               }
            }
         }
      }
   }
}
```

Both fields accept a list of keys to include or exclude. The corresponding response looks like:

```json
{
   "entries":{
      "x36WdKPMctUOkjXMyV8oQq2zWcSx":{
         "archive":{
            "metadata":{
               "optimade":{
                  "elements":[ "K", "S", "W" ],
                  "nelements":3,
                  "elements_ratios":[
                     0.007425742574257425,
                     0.0024752475247524753,
                     0.9900990099009901
                  ]
               }
            }
         }
      }
   }
}
```

!!! note
      `include` and `exclude` fields expect 'glob patterns'. Thus, if the `include` field is set to `*elements`, it will include all keys that end with `elements`.

```json hl_lines="9"
{
   "entries":{
      "x36WdKPMctUOkjXMyV8oQq2zWcSx":{
         "archive":{
            "metadata":{
               "optimade":{
                  "m_request":{
                     "directive":"plain",
                     "include":[ "*elements" ]
                  }
               }
            }
         }
      }
   }
}
```

The corresponding response will look like:

```json
{
   "entries":{
      "x36WdKPMctUOkjXMyV8oQq2zWcSx":{
         "archive":{
            "metadata":{
               "optimade":{
                  "elements":[ "K", "S", "W" ],
                  "nelements":3
               }
            }
         }
      }
   }
}
```

Note the field `elements_ratios` is not included any more.

<!-- TODO Clarify what deeper means exactly in the following note -->
!!! note
    Only one of the fields `include` and `exclude` can be used in a single request configuration.
    In either case, the field will not be passed to deeper levels of the archive.

#### Resolving References

Archives may contain references that point to some other locations in the archive, or even to other entries.
Conceptually it is similar to the soft links in file systems.
By using a default request configuration, references will be returned as they are.
The following request fetches the third `calculations_ref` under the path `workflow2/results`:

```json hl_lines="7"
{
   "entries":{
      "x36WdKPMctUOkjXMyV8oQq2zWcSx":{
         "archive":{
            "workflow2":{
               "results":{
                  "calculations_ref[2]":{ "m_request":{ "directive":"plain" } }
               }
            }
         }
      }
   }
}
```

The response will contain the reference string `#/run/0/calculation/2`, but not the data that it points to:

```json hl_lines="10"
{
   "entries":{
      "x36WdKPMctUOkjXMyV8oQq2zWcSx":{
         "archive":{
            "workflow2":{
               "results":{
                  "calculations_ref":[
                     null,
                     null,
                     "#/run/0/calculation/2"
                  ]
               }
            }
         }
      }
   }
}
```

??? note "various formats of references"
    The format of the reference string may vary, depending on whether it is a reference to the same entry or to another entry.

To resolve references, i.e., return the data that they point to, one should use the `resolved` directive instead of the default `plain` directive. For example:

```json hl_lines="9"
{
   "entries":{
      "x36WdKPMctUOkjXMyV8oQq2zWcSx":{
         "archive":{
            "workflow2":{
               "results":{
                  "calculations_ref[2]":{
                     "m_request":{
                        "directive":"resolved",
                        "max_list_size":2
                     }
                  }
               }
            }
         }
      }
   }
}
```

Note that, for presentation purposes, this request also limits the size of the returned list to 2 elements. The corresponding response is:

```json hl_lines="92 13 48-76"
{
   "uploads":{
      "RzWMitKESo2dQmuE6uQB-Q":{
         "entries":{
            "x36WdKPMctUOkjXMyV8oQq2zWcSx":{
               "archive":{
                  "run":[
                     {
                        "calculation":[
                           null,
                           null,
                           {
                              "method_ref":"uploads/RzWMitKESo2dQmuE6uQB-Q/entries/x36WdKPMctUOkjXMyV8oQq2zWcSx/archive/run/0/method/0",
                              "volume":4.8326900482177747e-26,
                              "density":996.3873291015625,
                              "pressure":-26484371.948242188,
                              "pressure_tensor":"__INTERNAL__:../uploads/RzWMitKESo2dQmuE6uQB-Q/archive/x36WdKPMctUOkjXMyV8oQq2zWcSx#/run/0/calculation/2/pressure_tensor",
                              "virial_tensor":"__INTERNAL__:../uploads/RzWMitKESo2dQmuE6uQB-Q/archive/x36WdKPMctUOkjXMyV8oQq2zWcSx#/run/0/calculation/2/virial_tensor",
                              "enthalpy":-1.473205588040599e-17,
                              "temperature":300.7535095214844,
                              "step":6000,
                              "time":1.2e-10,
                              "energy":{
                                 "total":{
                                    "value":-1.4736888308472856e-17
                                 },
                                 "electrostatic":{
                                    "value":0,
                                    "short_range":0
                                 },
                                 "van_der_waals":{
                                    "value":-1.724283145003578e-17,
                                    "short_range":-1.724283145003578e-17
                                 },
                                 "kinetic":{
                                    "value":2.5059431415629207e-18
                                 },
                                 "potential":{
                                    "value":-1.724283145003578e-17
                                 },
                                 "pressure_volume_work":{
                                    "value":4.832690154891482e-21
                                 }
                              },
                              "x_gromacs_thermodynamics_contributions":"__INTERNAL__:../uploads/RzWMitKESo2dQmuE6uQB-Q/archive/x36WdKPMctUOkjXMyV8oQq2zWcSx#/run/0/calculation/2/x_gromacs_thermodynamics_contributions"
                           }
                        ],
                        "method":[
                           {
                              "force_field":{
                                 "model":[
                                    {
                                       "contributions":[
                                          {
                                             "type":"bond",
                                             "n_interactions":5,
                                             "n_atoms":2,
                                             "atom_labels":"__INTERNAL__:../uploads/RzWMitKESo2dQmuE6uQB-Q/archive/x36WdKPMctUOkjXMyV8oQq2zWcSx#/run/0/method/0/force_field/model/0/contributions/0/atom_labels",
                                             "atom_indices":"__INTERNAL__:../uploads/RzWMitKESo2dQmuE6uQB-Q/archive/x36WdKPMctUOkjXMyV8oQq2zWcSx#/run/0/method/0/force_field/model/0/contributions/0/atom_indices"
                                          }
                                       ]
                                    }
                                 ],
                                 "force_calculations":{
                                    "vdw_cutoff":1.2e-9,
                                    "coulomb_type":"reaction_field",
                                    "coulomb_cutoff":1.2,
                                    "neighbor_searching":{
                                       "neighbor_update_frequency":40,
                                       "neighbor_update_cutoff":1.4e-9
                                    }
                                 }
                              },
                              "atom_parameters":"__INTERNAL__:../uploads/RzWMitKESo2dQmuE6uQB-Q/archive/x36WdKPMctUOkjXMyV8oQq2zWcSx#/run/0/method/0/atom_parameters"
                           }
                        ]
                     }
                  ]
               }
            }
         }
      }
   },
   "entries":{
      "x36WdKPMctUOkjXMyV8oQq2zWcSx":{
         "archive":{
            "workflow2":{
               "results":{
                  "calculations_ref":[
                     null,
                     null,
                     "uploads/RzWMitKESo2dQmuE6uQB-Q/entries/x36WdKPMctUOkjXMyV8oQq2zWcSx/archive/run/0/calculation/2"
                  ]
               }
            }
         }
      }
   }
}
```

The first thing to note here is that the reference string has been normalized to `uploads/RzWMitKESo2dQmuE6uQB-Q/entries/x36WdKPMctUOkjXMyV8oQq2zWcSx/archive/run/0/calculation/2`.
By default, the 'extra' data requested (here, the resolved data) will be added under the fixed response path: `uploads/<upload_id>/entries/<entry_id>/archive/<path_to_data>`.
This applies even when this path differs from the one specified in the original request, and is unaffected by any other factors, even if it is a reference to the same entry.
This is a valid path that can be used to access the data in the **same** response.
The motivation is to produce a response that is as self-contained as possible.

The second thing to note is that the target `calculation` contains a further reference `method_ref` that points to the method used for the calculation.
This reference is also resolved, and the corresponding data is fetched and included in the response.
In general, whenever the `resolved` directive is specified, all references will be recursively resolved such that the response contains all the data that is reachable from the original reference.

#### Controlling Reference Resolution

It is **not always** desired to resolve all references.
It is also possible to control how deep the references should be resolved by assigning a `resolve_depth` field in the request configuration.
For example, the following request will resolve only one level of references:

```json hl_lines="11"
{
   "entries":{
      "x36WdKPMctUOkjXMyV8oQq2zWcSx":{
         "archive":{
            "workflow2":{
               "results":{
                  "calculations_ref[2]":{
                     "m_request":{
                        "directive":"resolved",
                        "max_list_size":2,
                        "resolve_depth":1
                     }
                  }
               }
            }
         }
      }
   }
}
```

As can be seen in the response, the first `method` is no longer resolved, since it belongs to the second level of references.
Every resolution/redirection is counted as one level.

```json hl_lines="13"
{
   "uploads":{
      "RzWMitKESo2dQmuE6uQB-Q":{
         "entries":{
            "x36WdKPMctUOkjXMyV8oQq2zWcSx":{
               "archive":{
                  "run":[
                     {
                        "calculation":[
                           null,
                           null,
                           {
                              "method_ref":"#/run/0/method/0",
                              "volume":4.8326900482177747e-26,
                              "density":996.3873291015625,
                              "pressure":-26484371.948242188,
                              "pressure_tensor":"__INTERNAL__:../uploads/RzWMitKESo2dQmuE6uQB-Q/archive/x36WdKPMctUOkjXMyV8oQq2zWcSx#/run/0/calculation/2/pressure_tensor",
                              "virial_tensor":"__INTERNAL__:../uploads/RzWMitKESo2dQmuE6uQB-Q/archive/x36WdKPMctUOkjXMyV8oQq2zWcSx#/run/0/calculation/2/virial_tensor",
                              "enthalpy":-1.473205588040599e-17,
                              "temperature":300.7535095214844,
                              "step":6000,
                              "time":1.2e-10,
                              "energy":{
                                 "total":{
                                    "value":-1.4736888308472856e-17
                                 },
                                 "electrostatic":{
                                    "value":0,
                                    "short_range":0
                                 },
                                 "van_der_waals":{
                                    "value":-1.724283145003578e-17,
                                    "short_range":-1.724283145003578e-17
                                 },
                                 "kinetic":{
                                    "value":2.5059431415629207e-18
                                 },
                                 "potential":{
                                    "value":-1.724283145003578e-17
                                 },
                                 "pressure_volume_work":{
                                    "value":4.832690154891482e-21
                                 }
                              },
                              "x_gromacs_thermodynamics_contributions":"__INTERNAL__:../uploads/RzWMitKESo2dQmuE6uQB-Q/archive/x36WdKPMctUOkjXMyV8oQq2zWcSx#/run/0/calculation/2/x_gromacs_thermodynamics_contributions"
                           }
                        ]
                     }
                  ]
               }
            }
         }
      }
   },
   "entries":{
      "x36WdKPMctUOkjXMyV8oQq2zWcSx":{
         "archive":{
            "workflow2":{
               "results":{
                  "calculations_ref":[
                     null,
                     null,
                     "uploads/RzWMitKESo2dQmuE6uQB-Q/entries/x36WdKPMctUOkjXMyV8oQq2zWcSx/archive/run/0/calculation/2"
                  ]
               }
            }
         }
      }
   }
}
```

## Accessing Definitions

### Basic Usage

The NOMAD archives are collections of sections, each would have its schema/definition.
One may also want to access the corresponding definition to properly interpret the data.
To illustrate, we use the following sample archive with custom definition as an example.

```yaml
---
definitions:
  name: test_package_name
  section_definitions:
  - name: MySection
    base_sections:
    - nomad.datamodel.data.EntryData
    quantities:
    - name: my_quantity
      type:
        type_kind: python
        type_data: str
data:
  m_def: "#/definitions/section_definitions/0"
  my_quantity: test_value
```

A normal query would return the `my_quantity`.

```json
// query
{
   "entries":{
      "nBdYMQg4mFQED_q2QrKa8HYcGDyO":{
         "archive":{
            "data":{
               "m_request":{
                  "directive":"plain"
               }
            }
         }
      }
   }
}
// response
{
  "entries": {
    "nBdYMQg4mFQED_q2QrKa8HYcGDyO": {
      "archive": {
        "data": {
          "my_quantity": "test_value"
        }
      }
    }
  }
}
```

At the section level, one can use the special token `m_def` to access the corresponding definition.

```json hl_lines="6-10"
{
   "entries":{
      "nBdYMQg4mFQED_q2QrKa8HYcGDyO":{
         "archive":{
            "data":{
               "m_def":{
                  "m_request":{
                     "directive":"plain"
                  }
               },
               "m_request":{
                  "directive":"plain"
               }
            }
         }
      }
   }
}
```

The response would contain the definition.

```json hl_lines="7-27 38-41"
{
   "uploads":{
      "rcPhsTllSDSYTxuON7MA-w":{
         "entries":{
            "nBdYMQg4mFQED_q2QrKa8HYcGDyO":{
               "archive":{
                  "definitions":{
                     "section_definitions":[
                        {
                           "name":"MySection",
                           "base_sections":[
                              "metainfo/nomad.datamodel.data/section_definitions/1"
                           ],
                           "quantities":[
                              {
                                 "name":"my_quantity",
                                 "type":{
                                    "type_kind":"python",
                                    "type_data":"str"
                                 },
                                 "definition_id":"f0c41723ff303e23ad57d2ea032181f1ccf3518c"
                              }
                           ],
                           "definition_id":"c8722ec48248a465c28bd7511ddfad08969b1e9b"
                        }
                     ]
                  }
               }
            }
         }
      }
   },
   "entries":{
      "nBdYMQg4mFQED_q2QrKa8HYcGDyO":{
         "archive":{
            "data":{
               "my_quantity":"test_value",
               "m_def":{
                  "m_def":"uploads/rcPhsTllSDSYTxuON7MA-w/entries/nBdYMQg4mFQED_q2QrKa8HYcGDyO/archive/definitions/section_definitions/0",
                  "m_def_id":"c8722ec48248a465c28bd7511ddfad08969b1e9b"
               }
            }
         }
      }
   }
}
```

The definition of any section can also be deemed as a tree-like structure thus can be traversed.
By default, three lists: `base_sections`, `sub_sections` and `quantities` will be returned.
In this particular example, only `base_sections` and `quantities` are non-empty, the other is empty thus skipped.

Just like traversing data tree, it is possible to get whatever information available in the section definition.
For example, there is a list storing all base sections of the current section, named as `all_base_sections`, one can use the following to get it.

```json hl_lines="10-14"
{
   "entries":{
      "nBdYMQg4mFQED_q2QrKa8HYcGDyO":{
         "archive":{
            "data":{
               "m_def":{
                  "m_request":{
                     "directive":"plain"
                  },
                  "all_base_sections":{
                     "m_request":{
                        "directive":"plain"
                     }
                  }
               },
               "m_request":{
                  "directive":"plain"
               }
            }
         }
      }
   }
}
```

The response would contain the corresponding list as follows.
In principle, the default four lists should be sufficient for general usage.
Advanced users can retrieve rich information with a priori knowledge of the detailed structure of NOMAD metainfo system.

```json hl_lines="25-28"
{
   "uploads":{
      "rcPhsTllSDSYTxuON7MA-w":{
         "entries":{
            "nBdYMQg4mFQED_q2QrKa8HYcGDyO":{
               "archive":{
                  "definitions":{
                     "section_definitions":[
                        {
                           "name":"MySection",
                           "base_sections":[
                              "metainfo/nomad.datamodel.data/section_definitions/1"
                           ],
                           "quantities":[
                              {
                                 "name":"my_quantity",
                                 "type":{
                                    "type_kind":"python",
                                    "type_data":"str"
                                 },
                                 "definition_id":"f0c41723ff303e23ad57d2ea032181f1ccf3518c"
                              }
                           ],
                           "definition_id":"c8722ec48248a465c28bd7511ddfad08969b1e9b",
                           "all_base_sections":[
                              "metainfo/nomad.datamodel.data/section_definitions/0",
                              "metainfo/nomad.datamodel.data/section_definitions/1"
                           ]
                        }
                     ]
                  }
               }
            }
         }
      }
   },
   "entries":{
      "nBdYMQg4mFQED_q2QrKa8HYcGDyO":{
         "archive":{
            "data":{
               "my_quantity":"test_value",
               "m_def":{
                  "m_def":"uploads/rcPhsTllSDSYTxuON7MA-w/entries/nBdYMQg4mFQED_q2QrKa8HYcGDyO/archive/definitions/section_definitions/0",
                  "m_def_id":"c8722ec48248a465c28bd7511ddfad08969b1e9b"
               }
            }
         }
      }
   }
}
```

### Resolve Dependencies

The definition often contain other definitions, especially in `base_sections`.
Those are nothing but references to other sections, to further get information of those dependencies, one can use the `resolved` instead of `plain` and use `depth` or `resolve_depth` to control how deep to go.

```json hl_lines="8-9"
{
   "entries":{
      "nBdYMQg4mFQED_q2QrKa8HYcGDyO":{
         "archive":{
            "data":{
               "m_def":{
                  "m_request":{
                     "directive":"resolved",
                     "depth":1
                  }
               },
               "m_request":{
                  "directive":"plain"
               }
            }
         }
      }
   }
}
```

The response resolves one level deep and returns, as a result, `EntryData` is returned under the path `metainfo/nomad.datamodel.data/section_definitions/1`.
But it's dependency `metainfo/nomad.datamodel.data/section_definitions/0` is not returned.

```json hl_lines="12 36-44"
{
   "uploads":{
      "rcPhsTllSDSYTxuON7MA-w":{
         "entries":{
            "nBdYMQg4mFQED_q2QrKa8HYcGDyO":{
               "archive":{
                  "definitions":{
                     "section_definitions":[
                        {
                           "name":"MySection",
                           "base_sections":[
                              "metainfo/nomad.datamodel.data/section_definitions/1"
                           ],
                           "quantities":[
                              {
                                 "name":"my_quantity",
                                 "type":{
                                    "type_kind":"python",
                                    "type_data":"str"
                                 },
                                 "definition_id":"f0c41723ff303e23ad57d2ea032181f1ccf3518c"
                              }
                           ],
                           "definition_id":"c8722ec48248a465c28bd7511ddfad08969b1e9b"
                        }
                     ]
                  }
               }
            }
         }
      }
   },
   "metainfo":{
      "nomad.datamodel.data":{
         "section_definitions":[
            null,
            {
               "name":"EntryData",
               "description":"An empty base section definition. This can be used to add new top-level sections to an entry.",
               "base_sections":[
                  "metainfo/nomad.datamodel.data/section_definitions/0"
               ],
               "definition_id":"486f476f18785f5f4bcbac10db7304d7de35636b"
            }
         ]
      }
   },
   "entries":{
      "nBdYMQg4mFQED_q2QrKa8HYcGDyO":{
         "archive":{
            "data":{
               "my_quantity":"test_value",
               "m_def":{
                  "m_def":"uploads/rcPhsTllSDSYTxuON7MA-w/entries/nBdYMQg4mFQED_q2QrKa8HYcGDyO/archive/definitions/section_definitions/0",
                  "m_def_id":"c8722ec48248a465c28bd7511ddfad08969b1e9b"
               }
            }
         }
      }
   }
}
```

### Useful Settings

The `include` and `exclude` patterns can also be used in fetching definitions, however, they now apply to package names.

There is a flag `export_whole_package` that can be set to true under any section so that the corresponding package (that contains the target section) will be exported as a whole.
This could be convenient in some use cases.

## Miscellaneous Functionalities

Apart from the core functionalities that cover MongoDB database and archive data, there are additional resources that can be fetched.

### User Information

All data are associated with the corresponding users, uploads, entries, datasets, etc. are connected to a user node.
Accordingly, the special token `users` can be used to fetch user information.
Just like uploads and entries, a user ID needs to be specified.

For example, to fetch the user information of a user with ID `57aaf068-cdd0-43c1-be51-99e0d425c131`, one can use the query:

```json hl_lines="3"
{
   "users":{
      "57aaf068-cdd0-43c1-be51-99e0d425c131":{
         "m_request":{
            "directive":"plain"
         }
      }
   }
}
```

This will return the response (some fields are omitted):

```json
{
   "users":{
      "57aaf068-cdd0-43c1-be51-99e0d425c131":{
         "name":"Theodore Chang",
         "affiliation":"Humboldt-Universität zu Berlin",
         "user_id":"57aaf068-cdd0-43c1-be51-99e0d425c131",
         "created":"2022-02-12T22:14:25.151000+00:00",
         "is_admin":false,
         "is_oasis_admin":false
      }
   }
}
```

To retrieve your own user information, you can use the special token `me`, assuming you are logged in.
Thus, the above query is equivalent to the following if `57aaf068-cdd0-43c1-be51-99e0d425c131` is the user ID of the currently logged in user:

```json hl_lines="3"
{
   "users":{
      "me":{
         "m_request":{
            "directive":"plain"
         }
      }
   }
}
```

Starting from the user information, it is possible to navigate to other resources (nodes).
For example, the following query will list all uploads of the currently logged in user:

```json hl_lines="4"
{
   "users":{
      "me":{
         "uploads":{ "m_request":{ "directive":"plain" } }
      }
   }
}
```

The response, a plain list of upload IDs, will look something like:

```json
{
  "users": {
    "me": {
      "uploads": {
        "mBMHmsQuSgmgBuBlqaV5fQ": "mBMHmsQuSgmgBuBlqaV5fQ",
        "G7SMnJwZS5ajTT3eBROM-A": "G7SMnJwZS5ajTT3eBROM-A",
        "nMwp7V9cQJCZoCkA6Op8xg": "nMwp7V9cQJCZoCkA6Op8xg"
      }
    }
  }
}
```

One can retrieve specific data from each upload by navigating to the corresponding upload. This could be done in a second request using the retrieved upload IDs or, more efficiently, in the initial request with the wildcard `*`:

```json hl_lines="5-7"
{
   "users":{
      "me":{
         "uploads":{
            "*":{
               "upload_create_time":{ "m_request":{ "directive":"plain" } }
            }
         }
      }
   }
}
```

The response will contain the creation time of all uploads of the currently logged in user:

```json
{
   "users":{
      "me":{
         "uploads":{
            "mBMHmsQuSgmgBuBlqaV5fQ":{
               "upload_create_time":"2025-06-18T01:23:15.276000"
            },
            "G7SMnJwZS5ajTT3eBROM-A":{
               "upload_create_time":"2025-06-23T15:37:14.401000"
            },
            "nMwp7V9cQJCZoCkA6Op8xg":{
               "upload_create_time":"2025-06-23T16:07:53.100000"
            }
         }
      }
   }
}
```

### Elasticsearch Metadata

Some of the entry metadata is also stored in Elasticsearch indices.
They are similar to the metadata in the MongoDB database, but with more information.
To fetch data from the Elasticsearch index, one can use the special token `search`.
The top-level request configuration also supports the `query` field.
This `query` field shall take a valid `Metadata` query object (which itself also contains a `query` field), see the endpoint `/entries/query` on the [NOMAD API Dashboard](https://nomad-lab.eu/prod/v1/api/v1/extensions/docs){:target="_blank" rel="noopener"} for more details.

The following query fetches all entries created since 2025 that are visible to the logged in user:

```json hl_lines="5-8"
{
   "search":{
      "m_request":{
         "query":{
            "owner":"all",
            "query":{
               "upload_create_time":{ "gt":"2025-01-01" }
            }
         }
      }
   }
}
```

Each record will be returned as entry metadata (not shown here), from which one can navigate to the corresponding entry (MongoDB document) and get more information, or further navigate to the archive, etc.

As a more complex example, the following query first queries the Elasticsearch for the same list of entries then, for each hit, further fetches the `entry_create_time` from the MongoDB database via the `entry` special token.

```json hl_lines="11-19"
{
   "search":{
      "m_request":{
         "query":{
            "owner":"all",
            "query":{
               "upload_create_time":{ "gt":"2025-01-01" }
            }
         }
      },
      "*":{
         "entry":{
            "entry_create_time":{
               "m_request":{
                  "directive":"plain"
               }
            }
         }
      }
   }
}
```

The corresponding response will look like:

```json
{
   "search":{
      "m_response":{
         "include":[ "*" ],
         "query":{
            "owner":"all",
            "query":{
               "upload_create_time":{ "gt":"2025-01-01" }
            },
            "aggregations":{}
         },
         "pagination":{
            "page_size":10,
            "order_by":"entry_id",
            "order":"asc",
            "page_after_value":null,
            "page":1,
            "page_offset":null,
            "total":37,
            "next_page_after_value":"HcLSOzI89sGMCgYnhhfztI4Z1qxY",
            "page_url":null,
            "next_page_url":null,
            "prev_page_url":null,
            "first_page_url":null
         }
      },
      "-L073PFe_PxW90kci4UwxMgUO20O":{ "entry":{ "entry_create_time":"2025-06-23T16:34:50.684000" } },
      "3LGsPbtrFaiUHp_pG-j9WxLa24Gc":{ "entry":{ "entry_create_time":"2025-06-23T16:07:56.530000" } },
      "6EMY3osB1O7izLHlh1dXtoZYn0Ms":{ "entry":{ "entry_create_time":"2025-06-23T15:37:17.793000" } },
      "75dfpDPLnWz9k35aUBLuUb0StWz9":{ "entry":{ "entry_create_time":"2025-06-23T16:34:50.287000" } },
      "7YRYJDKWSNCTK5CRsBI-oopL0iep":{ "entry":{ "entry_create_time":"2025-06-23T16:07:56.256000" } },
      "8eYh9XB_vbKHMK8m_N7DK1U0dBlC":{ "entry":{ "entry_create_time":"2025-06-23T16:34:50.231000" } },
      "9OpqgAwjqWzr0URSnsRywqm1S52Q":{ "entry":{ "entry_create_time":"2025-06-23T16:07:56.586000" } },
      "AV12t0vir9EyCHNrmnXTlpROy5rz":{ "entry":{ "entry_create_time":"2025-06-23T16:34:50.060000" } },
      "FeuWgNCZ_YCevhwQyR-k5RJ1_uuY":{ "entry":{ "entry_create_time":"2025-06-18T01:23:16.343000" } },
      "HcLSOzI89sGMCgYnhhfztI4Z1qxY":{ "entry":{ "entry_create_time":"2025-06-23T16:07:56.364000" } }
   }
}
```

Note that when a `query` field is provided, it will be returned in the `m_response` field.
Also, the `pagination` field will always be returned, even if not specified in the request.

!!! tip
    Some fields are stored in both the MongoDB database and the Elasticsearch index. In this case, they can be fetched more directly from Elasticsearch.
    However, if the request needs to access an archive, the `entry -> archive` path must be used if starting from `search`.

### Listing File Information

As each entry corresponds to a main file, and each upload corresponds to a folder, the graph API also provides a convenient way to fetch file information, similar to the `ls` command in Linux.
There are two ways to access the file system.

1. Inside an upload, using the token `files`.
2. Inside an entry, using the token `mainfile`.

For example, the following query uses the `mainfile` token to fetch the file information:

```json hl_lines="13"
{
   "search":{
      "m_request":{
         "query":{
            "owner":"all",
            "query":{ "upload_create_time":{ "gt":"2025-01-01" } },
            "pagination":{ "page_size":1 }
         }
      },
      "*":{
         "entry":{
            "entry_create_time":{ "m_request":{ "directive":"plain" } },
            "mainfile":{ "m_request":{ "directive":"plain" } }
         }
      }
   }
}
```

In the response, we see that the entry `-L073PFe_PxW90kci4UwxMgUO20O` has the corresponding main file `OUTCAR_K_nm_5`, which has a size of `47862593` bytes:

```json hl_lines="32-48"
{
   "search":{
      "m_response":{
         "include":[ "*" ],
         "query":{
            "owner":"all",
            "query":{ "upload_create_time":{ "gt":"2025-01-01" } },
            "pagination":{
               "page_size":1,
               "order":"asc"
            },
            "aggregations":{}
         },
         "pagination":{
            "page_size":1,
            "order_by":"entry_id",
            "order":"asc",
            "page_after_value":null,
            "page":null,
            "page_offset":null,
            "total":37,
            "next_page_after_value":"-L073PFe_PxW90kci4UwxMgUO20O",
            "page_url":null,
            "next_page_url":null,
            "prev_page_url":null,
            "first_page_url":null
         }
      },
      "-L073PFe_PxW90kci4UwxMgUO20O":{
         "entry":{
            "entry_create_time":"2025-06-23T16:34:50.684000",
            "mainfile":{
               "OUTCAR_K_nm_5":{
                  "m_response":{
                     "directive":"plain",
                     "include":[ "*" ],
                     "pagination":{
                        "page":1,
                        "page_size":10,
                        "order":"asc",
                        "total":1
                     }
                  },
                  "path":"OUTCAR_K_nm_5",
                  "size":47862593,
                  "m_is":"File"
               }
            }
         }
      }
   }
}
```

<!-- TODO combine with previous pagination comment -->
??? note "Pagination for File Information"
    The file information listing is always paginated.
    This is particularly useful when listing files in an upload, as there can be many files.
