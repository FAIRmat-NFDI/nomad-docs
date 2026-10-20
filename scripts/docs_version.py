#!/usr/bin/env python3
"""Map a release tag to the mike version it is deployed as.

Only tags of the form ``vMAJOR.MINOR.PATCH`` are released. Starting from
v2.0.0, each minor release gets one entry in the version selector, which
every patch release replaces (``v2.0.3`` is deployed as ``2.0``). Older
releases keep one entry per patch version (``v1.4.3`` is ``1.4.3``).
The exact patch version (``2.0.3``) is kept as a mike alias that redirects
to the shared entry, so links to ``/2.0.3/...`` keep working.

Usage::

    git ls-remote --tags origin | sed 's|.*refs/tags/||' \\
        | python3 scripts/docs_version.py v2.0.3 >> "$GITHUB_OUTPUT"

The release tags of the repository are read from stdin and the result is
written to stdout as GitHub Actions step outputs:

- ``version``: the mike version name, e.g. ``2.0``
- ``alias``: the exact version, e.g. ``2.0.3``; empty if it equals ``version``
- ``stable``: ``true`` if the tag is the newest release overall
- ``deploy``: ``true`` unless a newer patch release already owns the version
"""

from __future__ import annotations

import argparse
import re
import sys
from collections.abc import Iterable


TAG_PATTERN = re.compile(r'^v(\d+)\.(\d+)\.(\d+)$')

# First release whose patch versions share a single "MAJOR.MINOR" entry.
FIRST_MINOR_SERIES_RELEASE = (2, 0, 0)

Release = tuple[int, int, int]


def parse_tag(tag: str) -> Release | None:
    match = TAG_PATTERN.match(tag)
    if match is None:
        return None
    major, minor, patch = (int(part) for part in match.groups())
    return major, minor, patch


def version_name(release: Release) -> str:
    major, minor, patch = release
    if release < FIRST_MINOR_SERIES_RELEASE:
        return f'{major}.{minor}.{patch}'
    return f'{major}.{minor}'


def resolve(tag: str, tags: Iterable[str]) -> dict[str, str]:
    release = parse_tag(tag)
    if release is None:
        raise ValueError(f'Invalid tag: {tag!r}; expected v<major>.<minor>.<patch>')

    releases = {r for r in (parse_tag(t.strip()) for t in tags) if r is not None}
    releases.add(release)

    # Re-deploying an older patch must not overwrite the docs of a newer one.
    newest_in_version = max(
        r for r in releases if version_name(r) == version_name(release)
    )

    version = version_name(release)
    exact_version = '.'.join(str(part) for part in release)

    return {
        'version': version,
        'alias': exact_version if exact_version != version else '',
        'stable': str(release == max(releases)).lower(),
        'deploy': str(release == newest_in_version).lower(),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('tag', help='the release tag to deploy, e.g. v2.0.3')
    args = parser.parse_args()

    try:
        outputs = resolve(args.tag, sys.stdin)
    except ValueError as e:
        print(f'::error::{e}', file=sys.stderr)
        sys.exit(1)

    for key, value in outputs.items():
        print(f'{key}={value}')


if __name__ == '__main__':
    main()
