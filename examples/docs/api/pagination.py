import os

import requests

api_url = os.getenv('NOMAD_API_URL', 'https://nomad-lab.eu/prod/v1/api/v1')
request_body = {
    'owner': 'public',
    'query': {'results.material.elements': {'all': ['Ti', 'O']}},
    'pagination': {'page_size': 10},
    'required': {
        'include': [
            'entry_id',
            'results.material.chemical_formula_hill',
        ],
    },
}

entries = []

while len(entries) < 100:
    request_body['pagination']['page_size'] = min(10, 100 - len(entries))
    response = requests.post(
        f'{api_url}/entries/query',
        json=request_body,
        timeout=30,
    )
    response.raise_for_status()
    payload = response.json()

    entries.extend(payload['data'])

    next_value = payload['pagination'].get('next_page_after_value')
    if not next_value:
        break
    request_body['pagination']['page_after_value'] = next_value

for entry in entries:
    formula = entry['results']['material']['chemical_formula_hill']
    print(entry['entry_id'], formula)
