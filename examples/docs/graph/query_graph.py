import json
import os

import requests

api_url = os.environ.get('NOMAD_API_URL', 'https://nomad-lab.eu/backend/api/v1')
request_body = {
    'search': {
        'm_request': {
            'query': {
                'owner': 'public',
                'query': {},
                'pagination': {'page_size': 2},
                'required': {'include': ['entry_id', 'upload_id']},
            },
        },
        '*': {
            'entry_id': '*',
            'entry': {
                'upload': {
                    'upload_name': '*',
                    'upload_create_time': '*',
                },
                'archive': {
                    'metadata': {'entry_id': '*', 'mainfile': '*'},
                },
            },
        },
    },
}


def main():
    response = requests.post(
        f'{api_url.rstrip("/")}/graph/query', json=request_body, timeout=60
    )
    response.raise_for_status()
    payload = response.json()
    # Inspect m_errors as well as the HTTP status: a graph can succeed only partly.
    print(json.dumps(payload, indent=2))


if __name__ == '__main__':
    main()
