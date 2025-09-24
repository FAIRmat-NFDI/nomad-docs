# How to make Graph-Style API Calls

## What you will learn

- How to implement flexible and accurate data fetching with a [GraphQL](https://graphql.org/)-like API.

## Recommended preparation

- [Tutorial > Accessing data via API](../../../tutorial/access_api.md)
- [API Overview](./api.md)

## Further resources
- [GraphQL](https://graphql.org/){:target="_blank"}

## Overview

While REST works well for simple data fetching, it often requires multiple requests when building complex pages, since each endpoint provides only fixed data. GraphQL addresses this by letting clients request exactly the fields they need across related resources in a single query, reducing round trips and avoiding over- or under-fetching.

NOMAD mimics this behaviour with a GraphQL-like API, available at the `/graph/query` endpoint (see the [NOMAD API Dashboard](https://nomad-lab.eu/prod/v1/api/v1/extensions/docs){:target="_blank"}).

??? note "Technical Note"
    The implementation can be categorized as a GraphQL-like API implemented within the REST-style framework FastAPI.
    Because GraphQL requires static, explicitly defined schemas ahead of time while NOMAD supports data with dynamic schema,
    it cannot be implemented directly using existing GraphQL tools.
    As a result, there are unfortunately no GUI tools available at this time.

## Basic Data Fetching

Imagine there is an example upload with the upload ID `<example_upload_id>`. The metadata of this upload is stored in MongoDB.

If one uses the endpoint `/uploads/{upload_id}` to fetch the upload metadata (see [NOMAD API Dashboard](https://nomad-lab.eu/prod/v1/api/v1/extensions/docs){:target="_blank"}),
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

The complete definition of `RequestConfig` can be found in [`nomad/graph/model.py`](https://github.com/FAIRmat-NFDI/nomad/blob/develop/nomad/graph/model.py){:target="_blank"}.

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

There are a few existing data resources (called documents) stored in MongoDB (see [NOMAD API Dashboard](https://nomad-lab.eu/prod/v1/api/v1/extensions/docs){:target="_blank"} for more details):

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
