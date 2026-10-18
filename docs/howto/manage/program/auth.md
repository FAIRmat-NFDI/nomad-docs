# How to authenticate programmatically

In this guide, you will create a personal access token (PAT) in the NOMAD GUI
and use it to authenticate a Python or command-line API request. You will also
learn how to rotate a token if its secret is exposed, revoke it when an
integration no longer needs access, and replace it after it expires.

PATs are the recommended authentication method for scripts, notebooks, command-line
workflows, and CI jobs. Each PAT is restricted to explicitly selected scopes and
is accepted only by the NOMAD deployment that issued it.

## Before you begin

Sign in to the NOMAD deployment that your program will access. Identify the API
resources and operations it needs. PAT scopes use the form
`<resource>:<action>`; grant only the corresponding scopes to the token.

The examples below list your projects through the backend `uploads` resource
and therefore require the `uploads:read` scope. See
[Explanation > Authentication and authorization > Authorization via scopes](../../../explanation/auth.md#authorization-via-scopes)
for the complete list of available scopes.

## Create a PAT

1. In the NOMAD GUI, open your profile menu and select **Settings**.
2. Under **User Settings**, select **Tokens**.
3. Select **CREATE NEW TOKEN**.
4. Enter a token name and choose an expiration date. A description is optional.
   Available expiration options depend on the deployment configuration.
5. Select the scopes required by your program. For the examples on this page,
   select `uploads:read`.
6. Select **CREATE TOKEN**.
7. Select **COPY TOKEN** and store the token securely before closing the dialog.

!!! warning
    NOMAD displays the token secret only once. NOMAD cannot show it again after
    you close the dialog. If you lose the secret, rotate the token or create a
    replacement.

The **READ ONLY** shortcut selects all available read scopes. This is convenient
for a program that reads several kinds of NOMAD data, but a single
`uploads:read` scope is narrower and is sufficient for the examples below.

## Use a PAT

Store the secret in an environment variable rather than placing it directly in
source code. Also define the complete API v1 base URL for the deployment that
issued the token.

=== "Bash or Zsh"

    ```bash
    read -r -s NOMAD_PAT
    export NOMAD_PAT
    export NOMAD_API_URL="https://nomad-lab.eu/backend/api/v1"
    ```

=== "PowerShell"

    ```powershell
    $securePat = Read-Host 'NOMAD PAT' -AsSecureString
    $env:NOMAD_PAT = [System.Net.NetworkCredential]::new('', $securePat).Password
    $env:NOMAD_API_URL = 'https://nomad-lab.eu/backend/api/v1'
    ```

Paste the token when prompted and press Enter. Both methods prevent the secret
from being displayed or included in the command itself.

`NOMAD_PAT` is the example variable used explicitly by the `requests` and
`curl` commands below. Other clients may expect a specific variable; for
example, `ArchiveQuery` reads `NOMAD_CLIENT_ACCESS_TOKEN`. See
[How-to guides > ... > Access processed data > Access non-public entries](./archive_query.md#access-non-public-entries).

For a NOMAD Oasis, obtain its base URL from its API dashboard instead of replacing
only the hostname in the NOMAD Central URL.

### With Python `requests`

Pass the PAT as a bearer token in the `Authorization` header:

```python
import os

import requests

response = requests.get(
    f'{os.environ["NOMAD_API_URL"]}/uploads',
    headers={'Authorization': f'Bearer {os.environ["NOMAD_PAT"]}'},
    params={'page_size': 1},
    timeout=30,
)
response.raise_for_status()

projects = response.json()['data']
```

### With `curl`

Use the same header from the command line:

=== "Bash or Zsh"

    ```bash
    curl --fail-with-body --silent --show-error \
      "${NOMAD_API_URL}/uploads?page_size=1" \
      -H "Authorization: Bearer ${NOMAD_PAT}"
    ```

=== "PowerShell"

    ```powershell
    curl.exe --fail-with-body --silent --show-error `
      "${env:NOMAD_API_URL}/uploads?page_size=1" `
      -H "Authorization: Bearer ${env:NOMAD_PAT}"
    ```

Using an environment variable keeps the token out of the command text, but
other processes running as your user may still be able to inspect your
environment. Prefer the secret store provided by your CI system or execution
environment for unattended workflows.

Do not put a NOMAD authorization header in a global `.curlrc`: `curl` would send
the token to unrelated hosts unless the configuration is carefully scoped.

## Diagnose authentication and authorization failures

- **HTTP 401 Unauthorized (authentication failure):** check that `NOMAD_PAT` is
  set, contains the complete secret, has not expired or been revoked, and was
  issued by the deployment in `NOMAD_API_URL`.
- **HTTP 403 Forbidden (authorization failure):** inspect the response's
  `detail` field. The token is valid, but it may lack one or more scopes required
  by the endpoint, or your account may not have access to the requested resource.
- **Unexpected deployment:** verify the complete API base URL. Tokens are not
  transferable between NOMAD Central, its test or develop deployments, and
  NOMAD Oasis deployments.

The **Tokens** page shows each token's status and last use, which can help
identify an expired token or confirm that a request reached the deployment.

## Rotate or revoke a PAT

Return to **User Settings > Tokens** and find the token in the table.

- Select the **Rotate token** action to revoke the current secret and replace it
  with a new one. Copy the new secret before closing the dialog, then update
  every program or secret store that used the old value.
- Select the **Revoke token** action when an integration no longer needs access
  or when you suspect that the secret has been exposed.

Rotation and revocation take effect immediately and cannot be undone. Expired or
revoked tokens cannot be rotated; create a replacement instead.

## Use a Keycloak access token when required

The GUI and the interactive OpenAPI dashboard use short-lived Keycloak access
tokens. Some compatibility workflows also obtain one directly with a username
and password:

```python
import os

import requests

response = requests.post(
    f'{os.environ["NOMAD_API_URL"]}/auth/token',
    data={
        'username': os.environ['NOMAD_USERNAME'],
        'password': os.environ['NOMAD_PASSWORD'],
        'grant_type': 'password',
    },
    timeout=30,
)
response.raise_for_status()

access_token = response.json()['access_token']
```

This password-based flow works only when the deployment and account permit it.
It is unsuitable for many federated or multi-factor login configurations and
requires the program to handle an account password. Use a scoped PAT for new
programmatic integrations whenever possible.

Keycloak access tokens include the full user scope set, including the
token-management scopes required to manage PATs programmatically. PATs cannot
themselves be granted these scopes. The relevant endpoints are:

| Operation | Endpoint | Required scopes |
| --- | --- | --- |
| Create | `POST /auth/pats` | `tokens:create` |
| List or inspect | `GET /auth/pats`, `GET /auth/pats/{pat_id}` | `tokens:read` |
| Rotate | `POST /auth/pats/{pat_id}/rotate` | `tokens:create`, `tokens:delete` |
| Revoke | `DELETE /auth/pats/{pat_id}` | `tokens:delete` |

Creation and rotation return the new `raw_token` only once. Consult the
deployment's [OpenAPI dashboard]({{ nomad_url() }}/v1/){:target="_blank" rel="noopener"}
for the current request and response models.

## Do not use app tokens for new integrations

The legacy `/auth/app_token` endpoint still exists for compatibility, but app
tokens are deprecated. They grant broad user permissions, cannot be scoped for
one integration, and remain valid until they expire or the deployment's signing
secret changes. Migrate existing app-token workflows to PATs rather than using
an app token to avoid Keycloak-token expiration.

## Related pages

- {{ nav_link("howto/manage/program/api.md", breadcrumb=True) }} — send REST API requests and paginate results.
- {{ nav_link("explanation/auth.md", breadcrumb=True) }} — understand token types, scopes, and authorization decisions.
- {{ nav_link("howto/manage/program/publish_python.md", breadcrumb=True) }} — create, update, and publish projects with Python.
- {{ nav_link("howto/manage/program/download.md", breadcrumb=True) }} — download projects, files, and processed data.
