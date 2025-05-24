# Querying Archive

In the previous page, we explained how to fetch data from different data resources (mainly `MongoDB` documents).
They are mostly flat (with only a few levels of nesting) and relatively easy to query and fetch.

The very idea can be extended to fetching archives that are stored on the file system.

## Accessing Archives

An archive is the processed data of an entry, which is stored on the file system as a binary file.
Each archive thus corresponds to an entry, and the corresponding entry ID can be used as the unique identifier to access the archive.
In the graph system, the archive is linked to the corresponding entry via the special token `archive`.
Thus, to access the archive of an entry with ID `example_entry_id`, one can use the following query.

```json hl_lines="4-6"
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
Replacing `example_entry_id` with a valid entry ID will make it ready to be executed.

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

??? note "a valid example"
    The following is a valid `curl` command that fetches the archive of a random entry `x36WdKPMctUOkjXMyV8oQq2zWcSx`.

    ```bash
    curl -X 'POST' \
    'https://nomad-lab.eu/prod/v1/api/v1/graph/query' \
    -H 'accept: application/json' \
    -H 'Content-Type: application/json' \
    -d '{
    "entries":{ "x36WdKPMctUOkjXMyV8oQq2zWcSx":{ "archive":{ "m_request":{ "directive":"plain" } } } }
    }'
    ```

## Nested Fetching

The archive is `JSON` compatible, which means it is effectively a `JSON` object (with tree-like structure).
Thus, one can apply the exact same logic and 'express' the intention in the request by using a tree-like structure.
For example, if one wants to fetch the `n_quantities` under `metadata` in the archive, the request would look like this.

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

The following is the response of the above request.
It can be noted that the response and the request have the same structure, and the intended data is returned.

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

## Advanced Customization

### List Slicing

If the target data is a list, it is possible to extract a slice of the list by using the `index` field in the request configuration.

The following request fetches the **second** (0-indexed) element of the `processing_logs` list in the archive of the entry with ID `x36WdKPMctUOkjXMyV8oQq2zWcSx`.

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
Since the first element is not requested, it will be `null` in the response.

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
For example, the above request can be equivalently written as follows.

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

!!! tip "range slicing"
    It is possible to assign both start and end indices to the `index` field.
    For example, `index: [1, 3]` will return the second to the fourth elements (both inclusive).
    Using the indexing key, it is equivalent to `key[1:3]`.

### Limiting Depth

Sometimes, it is only necessary to know what the archive contains, without needing to fetch all the data.
In such cases, one can limit the depth of the request by using the `depth` field in the request configuration.
The following request fetches the archive of the entry `x36WdKPMctUOkjXMyV8oQq2zWcSx` with a depth limit of 1.

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

There is one exception.
If the value is a primitive (like a string, number, boolean, etc.), it is always returned as is.
This is because generating internal reference strings for primitive values makes little sense and often has a negative impact on performance.

### Limiting Container Size

Some archives may contain large lists or dictionaries, and not all of them may be needed.
In such cases, one can limit the size of containers by using `max_list_size` and `max_dict_size` fields in the request configuration.
The following request fetches the data with a maximum list size of 3.

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

The response will contain only lists with a maximum of 3 elements.
Longer lists will be replaced by internal reference strings.

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

The `max_dict_size` field works similarly for dictionaries: if the dictionary has more than the specified number of keys, it will be replaced by an internal reference string.

### Filtering Unknown Keys

By providing either `include` or `exclude` fields in the request configuration, one can filter the keys of the archive.
Both fields accept a list of keys to include or exclude, respectively.

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

The corresponding response looks like this.

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

Note that glob patterns are expected.
Thus, if  the `include` field is set to `*elements`, it will include all keys that end with `elements`.

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

The corresponding response looks like this.
Note the field `elements_ratios` is not included any more.

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

!!! note
    Only one of the fields `include` and `exclude` can be used in a single request configuration.
    Both fields will not be passed to deeper levels of the archive.

### Resolving References

Archives may contain references that point to some other locations in the archive, or even to other entries.
Conceptually it is similar to the soft links in file systems.
By using a default request configuration, references will be returned as they are.
The following request fetches the third `calculations_ref` under the path `workflow2/results`.

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

The reference string `#/run/0/calculation/2` is returned, the data it points to is, however, not fetched.

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

To resolve the reference, one shall use the `resolved` directive instead of the default `plain` directive.
Note the following request also limits the size of the list to 2 elements such that the response has a reasonable length to be presented here.

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

The very first change is that the reference string is normalized to `uploads/RzWMitKESo2dQmuE6uQB-Q/entries/x36WdKPMctUOkjXMyV8oQq2zWcSx/archive/run/0/calculation/2`.
By default, the 'extra' data requested (here, the resolved data) will be added to the response under a fixed path: `uploads/<upload_id>/entries/<entry_id>/archive/<path_to_data>`.
This fixed path is not affected by any other factors, even if it is a reference to the same entry.
This is a valid path that can be used to access the data in the **same** response.
The motivation is to produce a response that is as self-contained as possible.

The second thing to note is that the target `calculation` contains a further reference `method_ref` that points to the method used for the calculation.
This reference is also resolved, and the corresponding data is fetched and included in the response.
As a matter of fact, all references will be recursively resolved such that the response contains all the data that is reachable from the original reference.

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

### Controlling Reference Resolution

However, it is **not always** desired to resolve all references.
It is possible to assign a `resolve_depth` field in the request configuration to control how deep the references should be resolved.
For example, the following request will resolve only one level of references.

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

As can be seen in the response, the first `method` is **not** resolved any more, since it is at the second level of references.
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
