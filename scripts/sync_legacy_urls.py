#!/usr/bin/env python3
"""Copy the stable documentation into the unversioned site root.

The documentation is hosted on GitHub Pages, which cannot apply a wildcard
rewrite from ``/foo`` to ``/<version>/foo``.  This script therefore mirrors
the stable version into the root, while leaving mike's version directories
and metadata untouched.
"""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path, PurePosixPath


MANIFEST = ".legacy-root-files.json"
RESERVED_ROOT_FILES = {".nojekyll", "CNAME", "versions.json", MANIFEST}


def _safe_root_path(root: Path, relative: str) -> Path:
    """Return a root-relative path while rejecting path traversal."""

    path = PurePosixPath(relative)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError(f"Unsafe root path: {relative!r}")
    return root.joinpath(*path.parts)


def _stable_version(root: Path) -> str | None:
    versions_file = root / "versions.json"
    versions = json.loads(versions_file.read_text())
    for version in versions:
        if "(stable)" in version.get("title", ""):
            return version["version"]
    return None


def _read_manifest(root: Path) -> list[str]:
    manifest = root / MANIFEST
    if not manifest.exists():
        return []
    data = json.loads(manifest.read_text())
    return data.get("files", [])


def _remove_empty_parents(path: Path, root: Path) -> None:
    parent = path.parent
    while parent != root and parent.is_relative_to(root):
        try:
            parent.rmdir()
        except OSError:
            break
        parent = parent.parent


def _remove_previous_root_files(root: Path) -> None:
    for relative in _read_manifest(root):
        if relative in RESERVED_ROOT_FILES:
            continue
        path = _safe_root_path(root, relative)
        if path.is_file() or path.is_symlink():
            path.unlink()
            _remove_empty_parents(path, root)


def _copy_version_into_root(root: Path, version: str) -> list[str]:
    version_root = root / version
    if not version_root.is_dir():
        raise FileNotFoundError(f"Stable version directory does not exist: {version_root}")

    copied_files: list[str] = []
    for source in version_root.rglob("*"):
        if not source.is_file():
            continue
        relative = source.relative_to(version_root).as_posix()
        destination = _safe_root_path(root, relative)
        destination.parent.mkdir(parents=True, exist_ok=True)
        if destination.is_symlink() or destination.is_file():
            destination.unlink()
        elif destination.exists():
            raise IsADirectoryError(f"Cannot copy file over directory: {destination}")
        shutil.copy2(source, destination)
        copied_files.append(relative)

    # MkDocs uses use_directory_urls: false, but preserve the old section
    # URLs by making /tutorial/ (and similar sections) serve their overview.
    for source in version_root.rglob("overview.html"):
        section = source.relative_to(version_root).parent
        if section == Path("."):
            continue
        relative = (section / "index.html").as_posix()
        destination = _safe_root_path(root, relative)
        destination.parent.mkdir(parents=True, exist_ok=True)
        if destination.is_symlink() or destination.is_file():
            destination.unlink()
        elif destination.exists():
            raise IsADirectoryError(f"Cannot copy file over directory: {destination}")
        shutil.copy2(source, destination)
        copied_files.append(relative)

    return copied_files


def sync(root: Path) -> int:
    root = root.resolve()
    version = _stable_version(root)
    if version is None:
        print("No stable version found; skipping root mirror")
        return 0

    _remove_previous_root_files(root)
    copied_files = _copy_version_into_root(root, version)

    (root / MANIFEST).write_text(
        json.dumps({"version": version, "files": sorted(copied_files)}, indent=2) + "\n"
    )
    print(f"Copied {len(copied_files)} stable root files from {version}")
    return len(copied_files)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("gh_pages_root", type=Path)
    args = parser.parse_args()
    sync(args.gh_pages_root)


if __name__ == "__main__":
    main()
