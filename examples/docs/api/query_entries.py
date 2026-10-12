import os

import requests

api_url = os.getenv('NOMAD_API_URL', 'https://nomad-lab.eu/prod/v1/api/v1')
request_body = {
    'owner': 'public',
    'query': {
        'results.material.elements': {'all': ['Ti', 'O']},
    },
    'pagination': {'page_size': 3},
    'required': {
        'include': [
            'entry_id',
            'results.material.chemical_formula_hill',
        ],
    },
}

response = requests.post(
    f'{api_url}/entries/query',
    json=request_body,
    timeout=30,
)
response.raise_for_status()
payload = response.json()

print(f'Total matching Entries: {payload["pagination"]["total"]}')
for entry in payload['data']:
    formula = entry['results']['material']['chemical_formula_hill']
    print(entry['entry_id'], formula)
