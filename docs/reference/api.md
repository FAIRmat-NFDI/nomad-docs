# REST API

This reference summarizes conventions used by the built-in NOMAD API. The
deployment's OpenAPI document is the authoritative source for individual
endpoint paths, request models, and response models.

## API discovery and base URLs

The GUI's [APIs page]({{ nomad_url() }}/../gui/v2/apis){:target="_blank" rel="noopener"}
lists the built-in NOMAD API and APIs contributed by installed plugins. Plugin
APIs vary between deployments.

The built-in NOMAD API is documented through:

- an [interactive OpenAPI dashboard]({{ nomad_url() }}/v1/){:target="_blank" rel="noopener"}; and
- its [OpenAPI JSON document]({{ nomad_url() }}/v1/openapi.json){:target="_blank" rel="noopener"}.

The built-in NOMAD API uses a base URL ending in `/api/v1`. For example:

```text
https://nomad-lab.eu/backend/api/v1
https://nomad-lab.eu/develop/backend/api/v1
https://<oasis-host>/<optional-prefix>/api/v1
```

Do not construct another deployment's URL by replacing only its hostname. A
deployment can use a different path prefix; obtain its URL from that
deployment's API dashboard.

## Core resources

| Resource | Purpose |
| --- | --- |
| `entries` | Search Entry metadata and retrieve an Entry's raw files or processed archive. |
| `uploads` | Backend representation of GUI Projects, including files, processing, collaborators, publication, and DOI actions. |
| `groups` | Create, inspect, update, and delete user groups. |
| `users` | Look up NOMAD users and their IDs. |
| `auth` | Obtain and manage supported authentication tokens. |
| `datasets` | Retained backend resources for existing legacy collections. New publication and DOI workflows operate on Projects. |

Many resources support both a collection path, such as `/entries`, and an
individual-resource path, such as `/entries/{entry_id}`. Consult the OpenAPI
dashboard to determine which HTTP methods each path supports.

## Request conventions

Use the HTTP method declared by the endpoint. `GET` operations normally encode
inputs as URL query parameters. `POST` operations normally use a JSON request
body:

```http
Content-Type: application/json
Accept: application/json
```

Authenticated requests carry a bearer token:

```http
Authorization: Bearer <token>
```

Create personal access tokens with only the scopes required by the operation.
For the available scopes and how they control access, see
{{ nav_link("explanation/auth.md", breadcrumb=True) }}.

## Response layout

Many collection and query operations return an object with these fields:

| Field | Meaning |
| --- | --- |
| `data` | The records returned for the current request or page. |
| `pagination` | Page size, ordering, total matches, and cursor information when the endpoint is paginated. |
| `owner` | The effective ownership scope when the operation supports ownership filtering. |
| `query` | The normalized query applied by the server when the operation supports queries. |
| `required` | The effective response-field or archive selection when the operation supports it. |

The exact envelope varies by endpoint. Some individual-resource operations
return their model directly; others wrap it in `data`. Use the endpoint's
declared response model to determine the response shape.

Error responses normally include a `detail` field. Validation errors can return
`detail` as a list containing the affected request locations and messages.

## Ownership scopes

Entry query endpoints use `owner` to restrict results by publication state and
the authenticated user's relationship to the Entry.

| Scope | Entries included |
| --- | --- |
| `public` | Published Entries without embargo. |
| `visible` | Public Entries plus unpublished Entries owned by or shared with the authenticated user. |
| `all` | Published Entries, including Entries under embargo, plus Entries owned by or shared with the authenticated user. |
| `shared` | Entries owned by or shared with the authenticated user. |
| `user` | Entries owned by the authenticated user. |
| `staging` | Unpublished Entries owned by or shared with the authenticated user. |
| `admin` | All Entries; available only to administrators. |

Use `public` for reproducible public-data scripts that do not need
authentication. Other ownership scopes require authentication to expose
non-public data, but selecting one cannot grant access beyond the authenticated
user's existing permissions.

## Entry queries

Entry query objects map searchable quantity paths to criteria. Different
criteria in one object are combined with logical AND:

```json
{
  "results.method.simulation.program_name": "VASP",
  "results.material.elements": ["Na", "Cl"]
}
```

For list-valued criteria, an unqualified list requires all supplied values.
Append an operator to a quantity path to change the comparison:

| Operator | Meaning |
| --- | --- |
| `:all` | Match every supplied value. |
| `:any` | Match at least one supplied value. |
| `:none` | Match none of the supplied values. |
| `:lt`, `:lte` | Match values less than, or less than or equal to, the criterion. |
| `:gt`, `:gte` | Match values greater than, or greater than or equal to, the criterion. |

For example:

```json
{
  "results.material.elements:any": ["Na", "K"],
  "upload_create_time:gte": "2026-01-01"
}
```

Comparison operators can instead be expressed as a nested object:

```json
{
  "upload_create_time": {
    "gte": "2026-01-01",
    "lt": "2027-01-01"
  }
}
```

Use `and`, `or`, and `not` for explicit logical combinations:

```json
{
  "and": [
    {
      "or": [
        {"results.material.elements": ["Na", "Cl"]},
        {"results.material.elements": ["H", "O"]}
      ]
    },
    {
      "not": {"results.material.symmetry.crystal_system": "cubic"}
    }
  ]
}
```

The searchable quantities depend on the endpoint and installed schema
packages. Use the request model and searchable-quantity information exposed by
the deployment to identify which quantities are indexed and available for
queries.

Entry search also accepts an `optimade_filter` criterion using OPTIMADE filter
syntax:

```json
{
  "optimade_filter": "nelements >= 2 AND elements HAS ALL 'Ti', 'O'"
}
```

## Response-field selection

Entry metadata search endpoints accept `required.include` and
`required.exclude` lists. For example:

```json
{
  "required": {
    "include": [
      "entry_id",
      "results.material.chemical_formula_hill"
    ]
  }
}
```

Archive endpoints use a hierarchical `required` tree that follows the archive
schema. `"*"` selects an entire branch:

```json
{
  "required": {
    "metadata": {
      "entry_id": "*",
      "mainfile": "*"
    },
    "workflow2": {
      "results": {
        "calculation_result_ref": {
          "energy": {"total": "*"},
          "system_ref": {"chemical_composition_reduced": "*"}
        }
      }
    }
  }
}
```

Selecting a branch through a reference implicitly includes the selected target
data. Use `"include-resolved"` to include a complete referenced branch. Set
`"resolve-inplace": true` at the root of `required` to replace returned
references with their target data instead of retaining the targets at their
original archive paths.

Request only the fields you need. Narrow selections reduce server work,
transfer size, and memory use.

## Pagination

Paginated requests and responses can contain:

| Field | Meaning |
| --- | --- |
| `page_size` | Maximum records returned in one response. `0` returns no records and can be useful for aggregation-only requests. |
| `order_by` | Quantity used to order the result. Accepted quantities depend on the endpoint. |
| `order` | `asc` or `desc`. |
| `page_after_value` | Opaque cursor after which the requested page begins. |
| `next_page_after_value` | Cursor returned by the server for the next request; absent when no later page exists. |
| `page` | One-based page number, where supported. |
| `page_offset` | Number of records skipped before the page, where supported. |
| `total` | Total records matching the query independently of the current page. |

Only one of `page_after_value`, `page`, and `page_offset` can be supplied. Page
numbers and offsets have endpoint-specific restrictions and generally cannot
address results beyond the first 10,000 records. To iterate through a complete
result set, begin without `page_after_value` and pass each returned
`next_page_after_value` into the following request.

Treat cursor values as opaque. Their format depends on the endpoint and
ordering and can change when either changes.

## User groups

The `groups` resource uses these core endpoints:

| Operation | Endpoint | Required scope |
| --- | --- | --- |
| List groups | `GET /groups` | `groups:read` |
| Inspect a group | `GET /groups/{group_id}` | `groups:read` |
| Create a group | `POST /groups` | `groups:write` |
| Update a group | `POST /groups/{group_id}/edit` | `groups:write` |
| Delete a group | `DELETE /groups/{group_id}` | `groups:delete` |

Create and update bodies use `members_info`, which contains the complete
membership list and each member's role:

```json
{
  "group_name": "Example research group",
  "description": "Collaborators on the example project",
  "members_info": [
    {"user_id": "<owner-user-id>", "role": "owner"},
    {"user_id": "<maintainer-user-id>", "role": "maintainer"},
    {"user_id": "<member-user-id>", "role": "member"}
  ]
}
```

The list must contain unique user IDs and exactly one owner. When creating a
group, the owner must be the authenticated user. Owners and maintainers can
update the group; only its owner or an administrator can delete it. The older
`members` field is deprecated.

Use the `users` endpoints to look up user IDs. Use a group's `group_id` when
assigning the group as a Project collaborator through an upload API request.

## Status codes, errors, and service limits

Common HTTP status categories are:

| Status | Meaning |
| --- | --- |
| `200`, `201`, `204` | Successful retrieval, creation, or operation without a response body. |
| `400`, `422` | Invalid request syntax, values, or model validation. Inspect `detail`. |
| `401` | Missing, expired, or invalid authentication. |
| `403` | Authenticated, but missing the required scope or resource permission. |
| `404` | Resource or endpoint not found. |
| `429` | Request rate limit exceeded. |
| `503` | Service unavailable, which can include a concurrency or temporary-capacity limit. |

Page-size, request-rate, and concurrency limits are deployment and endpoint
specific. Do not assume that limits observed on one deployment apply to
another. When the server applies a limit, reduce concurrency or page size as
appropriate and retry temporary responses with bounded backoff. Respect
`Retry-After` when the response provides it.

Clients should set timeouts, call `raise_for_status()` or perform equivalent
status handling, and report the response body when a request fails.

## Related pages

- {{ nav_link("howto/manage/program/api.md", breadcrumb=True) }} — send and paginate a public Entry query.
- {{ nav_link("howto/manage/program/auth.md", breadcrumb=True) }} — create and use access tokens.
- {{ nav_link("howto/manage/program/download.md", breadcrumb=True) }} — download Projects, files, and processed archives.
- {{ nav_link("howto/manage/program/archive_query.md", breadcrumb=True) }} — use the Python `ArchiveQuery` client.
- {{ nav_link("explanation/data.md", breadcrumb=True) }} — understand Projects, Entries, archives, and schemas.
