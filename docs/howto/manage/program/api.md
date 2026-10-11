# How to use the API

In this guide, you will use Python's `requests` package to call NOMAD's REST
API directly. You will search public Entries, limit the returned metadata, and
request the next page of results. The same request structure applies to other
REST API resources and NOMAD deployments.

The GUI calls the user-facing file container a *Project*. The REST API
represents the same container as an *upload* resource, so endpoint paths and
fields retain backend names such as `uploads` and `upload_id`.

## Before you begin

Install `requests` in your Python environment:

```sh
pip install requests
```

The examples use public data and do not require authentication. They connect
to NOMAD Central by default. To test against another deployment, set its API v1
URL before running the scripts. For the NOMAD develop deployment, use:

```sh
export NOMAD_API_URL="https://nomad-lab.eu/develop/backend/api/v1"
```

## Send an Entry search request

Create `query_entries.py` with the following content:

<!-- fmt: off -->
```python
--8<-- "examples/docs/api/query_entries.py"
```
<!-- fmt: on -->

Run the script:

```sh
python query_entries.py
```

The request body has four independent controls:

- `owner` limits the search by publication state and the authenticated user's
  relationship to the Entries. `public` selects published Entries without an
  embargo.
- `query` selects Entries whose normalized material contains both titanium and
  oxygen.
- `pagination` limits this response to three Entries.
- `required` limits the returned metadata to each Entry's ID and chemical
  formula.

Calling `raise_for_status()` makes the script stop on an unsuccessful HTTP
response instead of trying to interpret an error as a successful result.

The response contains the matching records under `data` and information about
the complete result set under `pagination`. Entry IDs and the order of results
can change as the deployment's data changes; scripts should consume the
response rather than depend on copied output.

## Request the next page

The first response contains `pagination.next_page_after_value` when more
results are available. Pass that opaque value as `page_after_value` in the next
request:

```python
next_value = payload['pagination'].get('next_page_after_value')

if next_value:
    request_body['pagination']['page_after_value'] = next_value
    response = requests.post(
        f'{api_url}/entries/query',
        json=request_body,
        timeout=30,
    )
    response.raise_for_status()
    next_payload = response.json()
```

Continue until `next_page_after_value` is absent. Prefer this cursor-based
method when iterating through a result set because page numbers and offsets
have endpoint-specific restrictions.

A complete pagination example is available in
[`examples/docs/api/pagination.py`](https://github.com/FAIRmat-NFDI/nomad-docs/blob/develop/examples/docs/api/pagination.py){:target="_blank" rel="noopener"}.

## Authenticate a request

Public Entry searches do not need a token. To access non-public data or perform
write operations, create a personal access token with the minimum required
scopes and store it in `NOMAD_PAT`. Add it to the request headers:

```python
import os

headers = {
    'Authorization': f'Bearer {os.environ["NOMAD_PAT"]}',
    'Accept': 'application/json',
}

response = requests.post(
    f'{api_url}/entries/query',
    headers=headers,
    json=request_body,
    timeout=30,
)
response.raise_for_status()
```

See {{ nav_link("howto/manage/program/auth.md", breadcrumb=True) }} for token
creation, scopes, and secure handling.

## Discover available endpoints

Each deployment provides interactive API documentation generated from its
current OpenAPI contract. Open the [core API dashboard]({{ nomad_url() }}/v1/){:target="_blank" rel="noopener"}
to inspect request and response models or try an operation in the browser.

The GUI's [APIs page]({{ nomad_url() }}/../gui/v2/apis){:target="_blank" rel="noopener"}
also lists the core API and APIs supplied by installed plugins. The available
plugin APIs therefore depend on the NOMAD deployment.

## Choose the next workflow

| Goal | Continue with |
| --- | --- |
| Understand shared REST request and response fields | {{ nav_link("reference/api.md", breadcrumb=True) }} |
| Download Projects, raw files, or processed archives | {{ nav_link("howto/manage/program/download.md", breadcrumb=True) }} |
| Query processed archives as schema-aware Python objects | {{ nav_link("howto/manage/program/archive_query.md", breadcrumb=True) }} |
| Create, update, or publish Projects with Python | {{ nav_link("howto/manage/program/publish_python.md", breadcrumb=True) }} |
| Traverse related NOMAD resources in one request | {{ nav_link("howto/manage/program/graph_api.md", breadcrumb=True) }} |
| Create or update user groups | [Reference > REST API > User groups](../../../reference/api.md#user-groups) |

## Related pages

- {{ nav_link("reference/api.md", breadcrumb=True) }} — base URLs, resources, query syntax, ownership, pagination, errors, and limits.
- {{ nav_link("explanation/data.md", breadcrumb=True) }} — the relationship between Projects, Entries, archives, and schemas.
- {{ nav_link("explanation/auth.md", breadcrumb=True) }} — authentication and authorization concepts.
