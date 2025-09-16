# Miscellaneous Functionalities

Apart from the core functionalities that cover MongoDB database and archive data, there are additional resources that can be fetched.
In this page, we briefly summarize these functionalities.

## User Information

As all data are associated with the corresponding users, in our mental model, uploads, entries, datasets, etc., are connected to a user node.
Accordingly, there is a top level special token `users` that can be used to fetch user information.
Just like uploads/entires introduced previously, a user ID needs to be specified.

For example, to fetch the user information of a user with ID `57aaf068-cdd0-43c1-be51-99e0d425c131`, one can use the following query.

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

This will return the following response (some fields are omitted).

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

In most cases, one shall only get the user information of the user who is currently logged in.
This can be done conveniently by using the special token `me`.
Thus, the above query is equivalent to the following query if `57aaf068-cdd0-43c1-be51-99e0d425c131` is the user ID of the currently logged in user.

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

Starting from user information, it is possible to navigate to other resources (nodes).
For example, the following query will list all uploads of the currently logged in user.

```json hl_lines="4"
{
   "users":{
      "me":{
         "uploads":{ "m_request":{ "directive":"plain" } }
      }
   }
}
```

The response may look like the following.

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

Note it's nothing more than a plain list.
If one wishes, one can navigate to the corresponding upload to get more information with specific upload IDs, or with a wildcard `*`.

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

The above query will return the creation time of all uploads of the currently logged in user.

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

## Elasticsearch Metadata

Some of the entry metadata is also stored in `Elasticsearch` indices.
They are similar to the metadata in the MongoDB database, but with more information.
To fetch data from the `Elasticsearch` index, one can use the special token `search`.
The top-level request configuration also supports the `query` field.
This `query` field shall take a valid `Metadata` query object (which itself also contains a `query` field), see the endpoint `/entries/query` for more details.

The following example lists all entries created since 2025 that are visible to the logged in user.

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

Each record will be returned as entry metadata, from which one can navigate to the corresponding entry (MongoDB document) and get more information, or further navigate to the archive, etc.
The following example first queries the `Elasticsearch`, for each hit, it further fetches the `entry_create_time` from the MongoDB database via the `entry` special token.

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

The response will look like the following.
Note when a `query` field is provided, it will be returned in the `m_response` field.
Also, the `pagination` field will always be returned, even if not specified in the request.

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

??? note "data duplication"
    Some fields are both stored in the `MongoDB` database and the `Elasticsearch` index.
    And it is likely that the desired information can be directly fetched from `Elasticsearch`.
    In this case, there is no need to navigate to the `MongoDB` database.
    However, if the request needs to access archive, it has to use `entry -> archive` path if starting from `search`.

## Listing File Information

As each entry corresponds to a main file, and each upload corresponds to a folder, the graph API also provides a convenient way to fetch file information, similar to the `ls` command in Linux.
There are two ways to access the file system.

1. Inside an upload, use the token `files`.
2. Inside an entry, use the token `mainfile`.

For example, the following query uses the `mainfile` token to fetch the file information.

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

In the response, we see that the entry `-L073PFe_PxW90kci4UwxMgUO20O` has the corresponding main file `OUTCAR_K_nm_5`, which has a size of `47862593` bytes.

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

??? note "pagination"
    The file information listing is always paginated.
    This is particularly useful when listing files in an upload, as there can be many files.
