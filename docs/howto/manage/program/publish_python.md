# How to manage data with Python

In this guide, you will use Python's `requests` package to create and manage a
NOMAD project through direct calls to the NOMAD API. You will add files,
monitor processing, update metadata, publish the project, and optionally assign
a DOI.

The GUI calls the user-facing container a *project*, while the API represents
the same container as an *upload* resource. Consequently, API paths and fields
use names such as `uploads` and `upload_id`.

## Before you begin

Install `requests` in your Python environment:

```sh
pip install requests
```

[Create a personal access token](./auth.md#create-a-pat) with the
`uploads:read`, `uploads:write`, and `uploads:publish` scopes, then
[save it in the `NOMAD_PAT` environment variable](./auth.md#use-a-pat).
Assigning a DOI also requires the `uploads:assign_doi` scope.

The examples below use the NOMAD test deployment. Change `api_url` only when
you are ready to work with another deployment.

```python
api_url = 'https://nomad-lab.eu/prod/v1/test/api/v1'
```

!!! warning
    Publishing is irreversible. Use the test deployment while developing and
    validating your script. Publish on NOMAD Central only when you have the
    rights to the data and can release them under the required license.

## Define the API functions

Create a file named `nomad_api.py` containing these functions:

```python
import os
import time
from pathlib import Path

import requests


def auth_headers():
    return {'Authorization': f'Bearer {os.environ["NOMAD_PAT"]}'}


def create_project(api_url, file_path):
    """Create a project and add a file or compressed file to it."""
    path = Path(file_path)
    with path.open('rb') as file_object:
        response = requests.post(
            f'{api_url}/uploads',
            params={'file_name': path.name},
            headers=auth_headers(),
            data=file_object,
            timeout=60,
        )
    response.raise_for_status()
    return response.json()['upload_id']


def get_project(api_url, upload_id):
    """Return the backend metadata for a project."""
    response = requests.get(
        f'{api_url}/uploads/{upload_id}',
        headers=auth_headers(),
        timeout=30,
    )
    response.raise_for_status()
    return response.json()['data']


def wait_for_processing(api_url, upload_id, interval=2):
    """Wait until the current project operation has finished."""
    while True:
        project = get_project(api_url, upload_id)
        if not project['process_running']:
            return project
        time.sleep(interval)


def edit_project_metadata(api_url, upload_id, metadata):
    """Update project metadata and shared metadata for its entries."""
    response = requests.post(
        f'{api_url}/uploads/{upload_id}/edit',
        headers=auth_headers(),
        json={'metadata': metadata},
        timeout=60,
    )
    response.raise_for_status()
    return response.json()


def publish_project(api_url, upload_id):
    """Publish a project."""
    response = requests.post(
        f'{api_url}/uploads/{upload_id}/action/publish',
        headers=auth_headers(),
        timeout=30,
    )
    response.raise_for_status()
    return response.json()


def assign_project_doi(api_url, upload_id):
    """Assign a DOI to a published project."""
    response = requests.post(
        f'{api_url}/uploads/{upload_id}/action/assign-doi',
        headers=auth_headers(),
        timeout=30,
    )
    response.raise_for_status()
    return response.json()
```

Calling `raise_for_status()` makes `requests` raise an exception when NOMAD
returns an unsuccessful HTTP status. For production scripts, catch
`requests.HTTPError` and report the response body so that API errors remain
visible.

## Create a project

Import the functions and add a file or compressed file. NOMAD creates the
project and returns its backend `upload_id`:

```python
from nomad_api import create_project, wait_for_processing

upload_id = create_project(api_url, 'test_data.zip')
print('Project ID:', upload_id)
```

The `upload_id` is the value displayed as **Project ID** under **SETTINGS** in
the GUI. If the supplied files contain parser-supported mainfiles, NOMAD
creates and processes the corresponding entries automatically.

Wait for processing and inspect its outcome:

```python
project = wait_for_processing(api_url, upload_id)
print('Process status:', project['process_status'])
print('Errors:', project['errors'])
print('Warnings:', project['warnings'])
```

Confirm that `process_status` is `SUCCESS`, review all warnings, and resolve any
errors before continuing.

## Update the metadata

The `/uploads/{upload_id}/edit` endpoint can update project-level metadata and
metadata shared by the entries in the project. This example sets the project
name and adds a comment and reference to its entries:

```python
from nomad_api import edit_project_metadata

metadata = {
    'upload_name': 'API example project',
    'comment': 'Created using direct requests to the NOMAD API.',
    'references': ['https://doi.org/xx.xxxx/example'],
    'embargo_length': 0,
}

response = edit_project_metadata(api_url, upload_id, metadata)
print(response)
```

Use NOMAD user IDs when setting collaborators through fields such as
`coauthors` or `reviewers`. See the interactive API documentation for all
metadata fields accepted by this endpoint.

## Publish the project

Before publishing, ensure that every intended entry was processed successfully
and that its metadata and files are complete and correct. Then request
publication:

```python
from nomad_api import publish_project, wait_for_processing

publish_project(api_url, upload_id)
project = wait_for_processing(api_url, upload_id)

print('Process status:', project['process_status'])
print('Published:', project['published'])
print('Errors:', project['errors'])
print('Warnings:', project['warnings'])
```

The publication request starts an asynchronous operation. Confirm that its
final `process_status` is `SUCCESS`, `published` is `True`, and `errors` is
empty.

## Optionally assign a DOI

DOI assignment is available on NOMAD Central and on NOMAD Oasis deployments
with DataCite integration enabled. The project must be published, contain at
least one entry, and be owned by the authenticated user.

!!! warning
    DOI assignment is irreversible. The DOI remains permanently associated
    with the project.

```python
from nomad_api import assign_project_doi

response = assign_project_doi(api_url, upload_id)
print(response['data']['doi'])
```

The NOMAD test deployment normally has no DataCite integration, so run this
step only against a deployment where DOI assignment is configured.

## Related pages

- {{ nav_link("tutorial/upload_publish.md", breadcrumb=True) }}
- {{ nav_link("tutorial/upload_publish_api.md", breadcrumb=True) }}
- {{ nav_link("howto/manage/program/api.md", breadcrumb=True) }}
- {{ nav_link("howto/manage/program/auth.md", breadcrumb=True) }}
- [NOMAD Utility Workflows > How-to Guides > Perform API Calls](https://fairmat-nfdi.github.io/nomad-utility-workflows/how_to/use_api_functions.html){:target="_blank" rel="noopener"}
