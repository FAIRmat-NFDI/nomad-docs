import pytest
from fastapi.testclient import TestClient

from nomad.app.main import app
from nomad.config import config

@pytest.fixture(scope='session')
def user_molds():
    """Return a dict: user labels -> user data (dict)."""
    return {f'user{i}': user for i, user in enumerate(users.values())}

@pytest.fixture(scope='module')
def api_v1(monkeysession, user_molds):
    """
    This fixture provides an HTTP client with Python requests interface that accesses
    the fast api. The have to provide URLs that start with out leading '/' after '.../api/v1.
    This fixture also patches the actual requests. If some code is using requests to
    connect to the NOMAD v1 at ``nomad.config.client.url``, the patch will redirect to the
    fast api under test.
    """
    test_client = TestClient(app, base_url='http://testserver/api/v1/')

    def call_test_client(method, url, *args, **kwargs):
        url = url.replace(f'{config.client.url}/v1/', '')
        url = url.replace('/api/v1/', '')
        return getattr(test_client, method)(url, *args, **kwargs)

    monkeysession.setattr(
        'requests.get', lambda *args, **kwargs: call_test_client('get', *args, **kwargs)
    )
    monkeysession.setattr(
        'requests.put', lambda *args, **kwargs: call_test_client('put', *args, **kwargs)
    )
    monkeysession.setattr(
        'requests.post',
        lambda *args, **kwargs: call_test_client('post', *args, **kwargs),
    )
    monkeysession.setattr(
        'requests.delete',
        lambda *args, **kwargs: call_test_client('delete', *args, **kwargs),
    )

    def __call__(self, request):
        for user in user_molds.values():
            if user['username'] == self.user or user['email'] == self.user:
                request.headers['Authorization'] = f'Bearer {user["user_id"]}'
        return request

    monkeysession.setattr('nomad.client.api.Auth.__call__', __call__)

    return test_client


@pytest.fixture(scope='module')
def client_with_api_v1(api_v1, monkeysession):
    def call_requests(method, path, *args, **kwargs):
        return getattr(api_v1, method)(path, *args, **kwargs)

    monkeysession.setattr('nomad.client.api._call_requests', call_requests)

@pytest.fixture(scope='session')
def client():
    return TestClient(app, base_url='http://testserver/')
