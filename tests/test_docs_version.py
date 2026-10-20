import importlib.util
from pathlib import Path

import pytest


spec = importlib.util.spec_from_file_location(
    'docs_version', Path(__file__).parents[1] / 'scripts' / 'docs_version.py'
)
docs_version = importlib.util.module_from_spec(spec)
spec.loader.exec_module(docs_version)


TAGS = ['v0.1.4', 'v1.4.2', 'v1.4.3', 'v2.0.0', 'v2.0.1', 'v2.1.0', 'v2.1.0rc1']


@pytest.mark.parametrize(
    'tag, expected',
    [
        pytest.param(
            'v1.4.2',
            {'version': '1.4.2', 'alias': '', 'stable': 'false', 'deploy': 'true'},
            id='pre-2.0-keeps-patch-version',
        ),
        pytest.param(
            'v2.0.1',
            {'version': '2.0', 'alias': '2.0.1', 'stable': 'false', 'deploy': 'true'},
            id='newest-patch-replaces-minor-series',
        ),
        pytest.param(
            'v2.0.0',
            {
                'version': '2.0',
                'alias': '2.0.0',
                'stable': 'false',
                'deploy': 'false',
            },
            id='older-patch-does-not-overwrite-newer',
        ),
        pytest.param(
            'v2.1.0',
            {'version': '2.1', 'alias': '2.1.0', 'stable': 'true', 'deploy': 'true'},
            id='newest-release-is-stable',
        ),
        pytest.param(
            'v2.1.1',
            {'version': '2.1', 'alias': '2.1.1', 'stable': 'true', 'deploy': 'true'},
            id='tag-missing-from-remote-list',
        ),
    ],
)
def test_resolve(tag, expected):
    assert docs_version.resolve(tag, TAGS) == expected


def test_versions_sort_numerically():
    tags = ['v2.9.0', 'v2.10.0']
    assert docs_version.resolve('v2.10.0', tags)['stable'] == 'true'
    assert docs_version.resolve('v2.9.0', tags)['stable'] == 'false'


@pytest.mark.parametrize(
    'tag', ['v2.1.0rc1', 'v2.1', 'v2', '2.1.0', 'v2.1.0-beta', 'vfoo']
)
def test_invalid_tag(tag):
    with pytest.raises(ValueError):
        docs_version.resolve(tag, TAGS)
