import subprocess
import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient
from nomad.app.main import app
from nomad.app.static import app as static_app
from nomad.config import config


@pytest.fixture(scope="session")
def built_docs_dir(tmp_path_factory: pytest.TempPathFactory) -> Path:
    repo_root = Path(__file__).resolve().parent.parent
    site_dir = tmp_path_factory.mktemp("site")
    subprocess.run(
        [
            sys.executable,
            "-m",
            "mkdocs",
            "build",
            "--strict",
            "--site-dir",
            str(site_dir),
        ],
        cwd=repo_root,
        check=True,
    )
    return site_dir


@pytest.fixture(scope="session")
def client(built_docs_dir: Path):
    docs_mount = next(
        route.app
        for route in static_app.routes
        if getattr(route, "path", None) == "/docs"
        and hasattr(route.app, "directory")
    )
    docs_mount.directory = str(built_docs_dir)
    docs_mount.all_directories = [str(built_docs_dir)]
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
