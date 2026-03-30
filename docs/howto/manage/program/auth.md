# Authentication and authorization

NOMAD uses tokens to authenticate requests and enforce access control.

For programmatic API usage (scripts, notebooks, CLI workflows, CI jobs),
the recommended approach is to use **Personal Access Tokens (PATs)**.

NOMAD supports [multiple token types](../../../explanation/auth.md#access-tokens):

- Personal Access Tokens (PATs) — **recommended** for programmatic use
- Keycloak access tokens — mainly for interactive or legacy workflows

## Personal Access Tokens

A [Personal Access Token (PAT)](../../../explanation/auth.md#personal-access-tokens-pats)
is tied to your user account and can be restricted to
[specific scopes](../../../explanation/auth.md#authorization-via-scopes).

PATs are preferred because they are:

- **Scoped** — limit access to specific resources/actions
- **Revocable** — can be invalidated at any time
- **Rotatable** — can be replaced without affecting your account
- **Time-limited** — can be configured with an explicit expiration to reduce long-term risk

!!! note
    GUI management page for PATs is coming soon.

### Create a PAT

A PAT can be created via the API. For example:

!!! warning
    Always grant the **minimum required scopes** when creating a PAT.
    Avoid unnecessary permissions (e.g. write access if only read is needed).

!!! note
    The raw token is **only returned once** when the token is created.
    Store it securely.

```python
import requests

response = requests.post(
    "{{ nomad_url() }}/v1/pats",
    headers={"Authorization": "Bearer <keycloak-access-token>"},
    json={
        "metadata": {
            "name": "My script token",
            "scopes": ["uploads:read", "uploads:write"]
        },
        "expires_in_days": 30
    },
)
response.raise_for_status()

pat = response.json()
raw_token = pat["raw_token"]
```

### Use a PAT in Python

Once created, use the PAT in subsequent requests:

```python
import requests

response = requests.get(
    "{{ nomad_url() }}/v1/uploads",
    headers={"Authorization": "Bearer <personal-access-token>"},
)
response.raise_for_status()

uploads = response.json()["data"]
```

### List your PATs

You can list all PATs for your account, and optionally filter, sort, and paginate the results.

For example, this request searches for PATs whose name matches `"ci"`,
filters for active tokens, sorts by most recently created first, and
returns the first page of results:

```python
import requests

response = requests.get(
    "{{ nomad_url() }}/v1/pats",
    headers={"Authorization": "Bearer <keycloak-access-token>"},
    params={
        "search": "ci",
        "state": "active",
        "order_by": "created_desc",
        "page_size": 20,
        "page": 1,
    },
)
response.raise_for_status()

result = response.json()

tokens = result["data"]
pagination = result["pagination"]
applied_query = result["query"]
```

The response has the following structure:

- data: the list of PATs
- pagination: pagination metadata such as total number of results, current page, and page size
- query: the filters applied to the request

You can **filter** PATs using the following query parameters:

<!-- TODO: here could dump `PATQuery` but need to add description first -->

- search: search by token name (case-insensitive)
- revoked: filter by explicit revoked status
- state: filter by token state, either active or inactive
- created_after, created_before: filter by creation time
- last_used_after, last_used_before: filter by last usage time
- expires_after, expires_before: filter by expiration time

You can **sort** the results with `order_by` using one of:

<!-- TODO: dump `PATSortOrder` to a UL -->

- created_asc
- created_desc
- expires_asc
- expires_desc
- last_used_asc
- last_used_desc
- name_asc
- name_desc

### Inspect a PAT

You can retrieve metadata for a specific PAT with its ID:

```python
import requests

pat_id = "<pat-id>"

response = requests.get(
    f"{{ nomad_url() }}/v1/pats/{pat_id}",
    headers={"Authorization": "Bearer <keycloak-access-token>"},
)
response.raise_for_status()

token_metadata = response.json()
```

### Revoke a PAT

To revoke a PAT:

```python
import requests

pat_id = "<pat-id>"

response = requests.delete(
    f"{{ nomad_url() }}/v1/pats/{pat_id}",
    headers={"Authorization": "Bearer <keycloak-access-token>"},
)
response.raise_for_status()
```

### Rotate a PAT

To replace an existing PAT with a new one:

```python
import requests

pat_id = "<pat-id>"

response = requests.post(
    f"{{ nomad_url() }}/v1/pats/{pat_id}/rotate",
    headers={"Authorization": "Bearer <keycloak-access-token>"},
)
response.raise_for_status()

new_pat = response.json()
new_raw_token = new_pat["raw_token"]
```

!!! warning
    Rotating a PAT **revokes the previous token** and returns a new raw token value,
    which is **only visible once**.

## Keycloak access tokens

NOMAD also supports [keycloak access tokens](../../../explanation/auth.md#keycloak-access-tokens) for authenticated API access.

For interactive use in the dashboard, use the **Authorize** button. The dashboard GUI
manages the keycloak access token automatically while you try out API operations.

!!! warning
    For new programmatic integrations, prefer **Personal Access Tokens (PATs)** over
    directly using account credentials to obtain keycloak access tokens.

Keycloak access tokens may also be used to call the API directly. For example:

```python
import os
import requests

response = requests.post(
    "{{ nomad_url() }}/v1/auth/token",
    data={
        "username": os.getenv("NOMAD_USERNAME"),
        "password": os.getenv("NOMAD_PASSWORD"),
        "grant_type": "password",
    },
)
response.raise_for_status()

token = response.json()["access_token"]

response = requests.get(
    "{{ nomad_url() }}/v1/uploads",
    headers={"Authorization": f"Bearer {token}"},
)
response.raise_for_status()

uploads = response.json()["data"]
```

If you have the [NOMAD Python package](../../../howto/oasis/install.md#how-to-install-the-nomad-python-library)
installed, you can also use the `nomad.client.Auth` helper:

!!! warning
  This username/password-based flow is kept mainly for compatibility and
  trusted first-party usage. For new programmatic integrations, prefer
  Personal Access Tokens (PATs) instead.

```python
import os
import requests
from nomad.client import Auth

response = requests.get(
    "{{ nomad_url() }}/v1/uploads",
    auth=Auth(
        user=os.getenv("NOMAD_USERNAME"),
        password=os.getenv("NOMAD_PASSWORD"),
    ),
)
response.raise_for_status()

uploads = response.json()["data"]
```
