
from nomad.config import config


def test_docs(client):
    rv = client.get('/docs/index.html')
    assert rv.status_code == 200
    assert (
        f'max-age={config.services.html_resource_http_max_age}, must-revalidate'
        in rv.headers['Cache-Control']
    )
    assert 'Etag' in rv.headers

    rv = client.get('/docs/assets/favicon.png')
    assert rv.status_code == 200
    assert (
        f'max-age={config.services.image_resource_http_max_age}, must-revalidate'
        in rv.headers['Cache-Control']
    )
    assert 'Etag' in rv.headers

    etag = rv.headers['Etag']
    rv = client.get('/docs/assets/favicon.png', headers={'If-None-Match': etag})
    assert rv.status_code == 304
    rv = client.get('/docs/assets/favicon.png', headers={'If-None-Match': f'W/{etag}'})
    assert rv.status_code == 304
