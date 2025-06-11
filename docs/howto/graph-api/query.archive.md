# Querying Archive

In the previous page, we explained how to fetch data from different data resources (mainly `MongoDB` documents).
They are mostly flat (with only a few levels of nesting) and relatively easy to query and fetch.

The very idea can be extended to fetching archives that are stored on the file system.

## Accessing Archives

An archive is the processed data of an entry, which is stored on the file system as a binary file.
Each archive thus corresponds to an entry, and the corresponding entry ID can be used as the unique identifier to access the archive.
In the graph system, the archive is linked to the corresponding entry via the special token `archive`.
Thus, to access the archive of an entry with ID `example_entry_id`, one can use the following query.

```json title="accessing archive" hl_lines="4"
{
  "entries":{
    "example_entry_id":{
      "archive":{
        "m_request":{ "directive":"plain" }
      }
    }
  }
}
```

The above query will return the contents of the target archive.

```json title="accessing archive" hl_lines="4"
{
  "entries":{
    "x2O9ezP2_P8YTE99Dj76JymtjQ-6":{
      "archive":{
        "m_request":{ "directive":"plain" }
      }
    }
  }
}
```

??? note "a valid example"
    The following is a valid `curl` command that fetches the archive of a random entry `x36WdKPMctUOkjXMyV8oQq2zWcSx`.

    ```bash
    curl -X 'POST' \
    'https://nomad-lab.eu/prod/v1/api/v1/graph/query' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{
    "entries":{
        "x36WdKPMctUOkjXMyV8oQq2zWcSx":{
        "archive":{
            "m_request":{ "directive":"plain" }
        }
        }
    }
    }'
    ```

## Nested Fetching

The archive is `JSON` compatible, which means it is effectively a `JSON` object (with tree-like structure).
Thus, one can apply the exact same logic and 'express' the intention in the request by using a tree-like structure.
For example, if one wants to fetch the `n_quantities` under `metadata` in the archive, the request would look like this.

```json title="fetching nested data from archive"
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

The following is the response of the above request.
It can be noted that the response and the request have the same structure, and the intended data is returned.

```json title="response of fetching nested data from archive"
{
  "entries":{
    "x2O9ezP2_P8YTE99Dj76JymtjQ-6":{
      "archive":{
        "metadata":{
          "n_quantities":69247
        }
      }
    }
  }
}
```

## Advanced Customization

### List Slicing

If the target data is a list, it is possible to extract a slice of the list by using the `index` field in the request configuration.

The following request fetches the **second** (0-indexed) element of the `processing_logs` list in the archive of the entry with ID `x36WdKPMctUOkjXMyV8oQq2zWcSx`.

```json title="request with list slicing"
{
  "entries":{
    "x36WdKPMctUOkjXMyV8oQq2zWcSx":{
      "archive":{
        "processing_logs":{
          "m_request":{ "directive":"plain", index: [1] }
        }
      }
    }
  }
}
```

The exact data will be returned in the corresponding position.
Since the first element is not requested, it will be `null` in the response.

```json title="response with list slicing"
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

### Limiting Depth

Sometimes, it is only necessary to know what the archive contains, without needing to fetch all the data.
In such cases, one can limit the depth of the request by using the `depth` field in the request configuration.
The following request fetches the archive of the entry `x36WdKPMctUOkjXMyV8oQq2zWcSx` with a depth limit of 1.

```json title="request with depth limiting"
{
  "entries":{
    "x36WdKPMctUOkjXMyV8oQq2zWcSx":{
      "archive":{
        "m_request":{ "directive":"plain", "depth": 1 }
      }
    }
  }
}
```

The response will contain only the top-level fields of the archive, without any nested data.

```json title="response with depth limiting"
{
  "entries":{
    "x2O9ezP2_P8YTE99Dj76JymtjQ-6":{
      "archive":{
        "processing_logs":"__INTERNAL__:../uploads/XGUaREsuRgSOi9NHB9ELbQ/archive/x2O9ezP2_P8YTE99Dj76JymtjQ-6#/processing_logs",
        "run":"__INTERNAL__:../uploads/XGUaREsuRgSOi9NHB9ELbQ/archive/x2O9ezP2_P8YTE99Dj76JymtjQ-6#/run",
        "workflow2":"__INTERNAL__:../uploads/XGUaREsuRgSOi9NHB9ELbQ/archive/x2O9ezP2_P8YTE99Dj76JymtjQ-6#/workflow2",
        "metadata":"__INTERNAL__:../uploads/XGUaREsuRgSOi9NHB9ELbQ/archive/x2O9ezP2_P8YTE99Dj76JymtjQ-6#/metadata",
        "results":"__INTERNAL__:../uploads/XGUaREsuRgSOi9NHB9ELbQ/archive/x2O9ezP2_P8YTE99Dj76JymtjQ-6#/results"
      }
    }
  }
}
```

The values of each field will be replaced by internal reference strings to indicate that the data is available but not fetched.

There is one exception.
If the value is a primitive (like a string, number, boolean, etc.), it is always returned as is.
This is because generating internal reference strings for primitive values makes little sense and often has a negative impact on performance.
