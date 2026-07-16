#
# Copyright The NOMAD Authors.
#
# This file is part of NOMAD. See https://nomad-lab.eu for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import pytest
from fastapi.testclient import TestClient
from nomad.app.main import app
from nomad.config import config


@pytest.fixture(scope="session")
def client():
    return TestClient(app, base_url="http://testserver/")


def test_docs(client):
    app_base = config.services.api_base_path
    rv = client.get(f"{app_base}/docs/index.html")
    assert rv.status_code == 200
    assert (
        f"max-age={config.services.html_resource_http_max_age}, must-revalidate"
        in rv.headers["Cache-Control"]
    )
    assert "Etag" in rv.headers

    rv = client.get(f"{app_base}/docs/assets/favicon.png")
    assert rv.status_code == 200
    assert (
        f"max-age={config.services.image_resource_http_max_age}, must-revalidate"
        in rv.headers["Cache-Control"]
    )
    assert "Etag" in rv.headers

    etag = rv.headers["Etag"]
    rv = client.get(
        f"{app_base}/docs/assets/favicon.png", headers={"If-None-Match": etag}
    )
    assert rv.status_code == 304
    rv = client.get(
        f"{app_base}/docs/assets/favicon.png", headers={"If-None-Match": f"W/{etag}"}
    )
    assert rv.status_code == 304
