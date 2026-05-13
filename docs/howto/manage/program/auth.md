# Authentication and authorization

NOMAD uses tokens to authenticate requests and enforce access control.

For programmatic API usage (scripts, notebooks, CLI workflows, CI jobs),
the recommended approach is to use **Personal Access Tokens (PATs)**.

NOMAD supports [multiple token types](../../../explanation/auth.md#access-tokens):

- Personal Access Tokens (PATs) — **recommended** for programmatic use
- Keycloak access tokens — mainly for interactive or legacy workflows

## Personal Access Tokens

[Personal Access Tokens (PATs)](../../../explanation/auth.md#personal-access-tokens-pats) are
the [preferred way for programmatic access](../../../explanation/auth.md#personal-access-tokens-pats) to the API.

!!! note
    GUI management page for PATs is coming soon.

### Create a PAT

A PAT can be created via the API with the [keycloak access token](#keycloak-access-tokens). For example:

!!! warning
    Always grant the **minimum required scopes** when creating a PAT.
    Avoid unnecessary permissions (e.g. write access if only read is needed).

!!! note
    The raw token is **only returned once** when the token is created.
    Store it securely.

```python
import requests

response = requests.post(
    "{{ nomad_url() }}/v1/auth/pats",
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

Once created, we recommend storing it in an environment variable:

```bash
export NOMAD_PAT="<personal-access-token>"
```

Use the PAT in subsequent requests:

```python
import os
import requests

response = requests.get(
    "{{ nomad_url() }}/v1/uploads",
    headers={"Authorization": f"Bearer {os.environ["NOMAD_PAT"]}"},
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
import os
import requests

response = requests.get(
    "{{ nomad_url() }}/v1/auth/pats",
    headers={"Authorization": f"Bearer {os.environ["NOMAD_PAT"]}"},
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
```

You can filter and sort PATs using query parameters, see the API dashboard for available options and examples.

### Inspect a PAT

You can retrieve metadata for a specific PAT with its ID:

```python
import requests

pat_id = "<pat-id>"

response = requests.get(
    f"{{ nomad_url() }}/v1/auth/pats/{pat_id}",
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
    f"{{ nomad_url() }}/v1/auth/pats/{pat_id}",
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
    f"{{ nomad_url() }}/v1/auth/pats/{pat_id}/rotate",
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

## App token

!!! info "Deprecated tokens"
    app token is deprecated and will be removed in a future release.
    They should not be used for new integrations. Use [**Personal Access Tokens (PATs)**](#personal-access-tokens) instead.

If the short-term expiration of the default *access token* does not suit your needs,
you can request an *app token* with a user-defined expiration. For example, you can
send the GET request `/auth/app_token?expires_in=86400` together with some way of
authentication, e.g. header `Authorization: Bearer <access token>`. The API will return
an app token, which is valid for 24 hours in subsequent request headers with the format
`Authorization: Bearer <app token>`. The request will be declined if the expiration is
larger than the maximum expiration defined by the API config.

!!! warning
    Despite the name, the app token is used to impersonate the user who requested it.
    It does not discern between different uses and will only become invalid once it
    expires (or when the API's secret is changed).
