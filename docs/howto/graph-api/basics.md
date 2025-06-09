# The Graph(-style) API

A [GraphQL](https://graphql.org/)-like API is implemented to allow flexible and accurate data fetching.

??? note "technical details"
    It is categorized as a `GraphQL`-**like** API implemented within the `REST` style framework `FastAPI`.
    Because `GraphQL` requires static, explicitly defined schemas ahead of time while `NOMAD` supports data with dynamic schema,
    it cannot be implemented directly using existing `GraphQL` tools.
    As a result, there are no GUI tools available unfortunately.

## Overview

In general, `REST` is good for simple data fetching, while the project gets more complex, APIs in REST style become more complex and less flexible.
When building a complex page, often a single request is not enough, and multiple requests are needed to fetch all the necessary data.
`GraphQL` aims to solve this over-/under-fetching problem so that both performance and bandwidth can be optimized.

You walk into a restaurant, go through the menu, and order several dishes at once.
The kitchen prepares all the dishes and serves them to you, nothing more, nothing less.
This is effectively how `GraphQL` works.

In `NOMAD`, we mimic this behaviour with a `GraphQL`-like API.
The only endpoint involved is `/graph/query`.
All the magic happens there.
But before that, we shall first explain some basic concepts.

## Basic Data Fetching

Imagine there is an example upload with the upload ID `example_upload_id`.
The metadata of this upload is stored in `MongoDB`.
In our mental model, it is possible to organize all uploads in a tree structure, under the root `uploads`.
This better helps us to define interactions among different data structures (to be explained later).

If one uses the endpoint `/uploads/{upload_id}` to fetch the upload metadata,
the response would look like the following (after some restructuring according to the mental model).

```json title="an example upload"
{
  "uploads":{
    "example_upload_id":{
      "process_running":true,
      "current_process":"process_upload",
      "process_status":"WAITING_FOR_RESULT",
      "last_status_message":"Waiting for results (level 0)",
      "complete_time":"2025-05-27T10:03:54.115000",
      "upload_id":"example_upload_id",
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

How would one tell the server if, say, for example, only `upload_name` is needed?
With `GraphQL`, one simply needs to '__ask for what you need__', following the structure of the data.
To mimic this, the request may look like the following.

```json title="a naive request"
{
  "uploads":{
    "example_upload_id":{
      "upload_name":"I want this!",
    }
  }
}
```

But it is not practical to use a string to express potentially complex intentions.
Instead, we want to use a more structured way to express the request.
To this end, `NOMAD` defines a request configuration model (referred to as 'config').

```py title="request configuration model"
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

??? note "complete definition"
    The complete definition of the `RequestConfig` can be found in `nomad/graph/model.py`.

To fetch the desired field, one shall attach a `RequestConfig` under the key `m_request`.
The `plain` directive tells the server to include the field in the response.

```json title="the very first query" hl_lines="4"
{
  "uploads":{
    "example_upload_id":{
      "upload_name":{"m_request":{"directive":"plain"}}
    }
  }
}
```

Now it is possible to fetch whatever wanted from the upload metadata.
For example, if one wants to fetch the `upload_name` and `upload_create_time`, the request would look like this:

```json title="composing a query"
{
  "uploads":{
    "example_upload_id":{
      "upload_name":{"m_request":{"directive":"plain"}},
      "upload_create_time":{"m_request":{"directive":"plain"}}
    }
  }
}
```

## Existing Data Resources

As of this writing, there are a few existing data resources stored in `MongoDB`:

1. `uploads` (stored in MongoDB): The metadata of an upload, including, `upload_id`, `upload_name`, `main_author`, etc.
2. `entries` (stored in MongoDB): The metadata of an entry, including, `entry_id`, `entry_create_time`, `mainfile`, etc.
3. `datasets` (stored in MongoDB): The metadata of a dataset, including, `dataset_id`, `dataset_name`, `user_id`, etc.
4. `groups` (stored in MongoDB): The metadata of a user group, including, `owner`, `members`, etc.

One can apply the same logic to fetch data from these structures.
For example, to fetch the `entry_id` and `entry_create_time` of an entry with ID `example_entry_id`, the request would look like this:

```json title="fetching entry metadata"
{
  "entries":{
    "example_entry_id":{
      "entry_id":{"m_request":{"directive":"plain"}},
      "entry_create_time":{"m_request":{"directive":"plain"}}
    }
  }
}
```

This concludes the basic usage of the `/graph/query` endpoint.
