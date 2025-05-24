# The Graph(-style) API

A [GraphQL](https://graphql.org/)-like API is implemented to allow flexible and accurate data fetching.

??? note "technical details"
    It is categorized as a GraphQL-**like** API implemented within the `REST` style framework `FastAPI`.
    Because GraphQL requires static explicitly defined schemas ahead of time while NOMAD supports data with dynamic schema,
    it cannot be implemented directly using existing GraphQL tools.
    As a result, there are no GUI tools available unfortunately.

## Overview

In general, `REST` is good for simple data fetching, while the project gets more complex, APIs in REST style become more complex and less flexible.
When building a complex page, often a single request is not enough, and multiple requests are needed to fetch all the necessary data.
`GraphQL` aims to solve this over-/under-fetching problem so that both performance and bandwidth can be optimized.

You walk into a restaurant, go through the menu, and order several dishes at once.
The kitchen prepares all the dishes and serves them to you, nothing more, nothing less.
This is effectively how `GraphQL` works.

In `NOMAD`, we mimic this behavior with a `GraphQL`-like API.
The only endpoint involved is `/graph/query`.
All the magic happens there.
But before that, we shall first explain some basic concepts.

## Existing Data Structures

As of this writing, there are a few existing data structures in NOMAD:

1. `upload` (MongoDB): The metadata of an upload, including, `upload_id`, `upload_name`, `main_author`, etc.
2. `entry` (MongoDB): The metadata of an entry, including, `entry_id`, `entry_create_time`, `mainfile`, etc.
3. `dataset` (MongoDB): The metadata of a dataset, including, `dataset_id`, `dataset_name`, `user_id`, etc.
4. `archive` (disk): The processed data of an entry archive.
