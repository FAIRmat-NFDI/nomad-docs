from nomad.client import ArchiveQuery

query = ArchiveQuery(
    owner='public',
    query={
        'results.method.simulation.program_name': 'VASP',
        'results.material.elements': {'all': ['Ti', 'O']},
    },
    required={
        'metadata': {
            'entry_id': '*',
            'mainfile': '*',
        },
        'results': {
            'material': {
                'chemical_formula_reduced': '*',
            },
        },
    },
    results_max=5,
    page_size=5,
)

for archive in query.download():
    print(
        archive.metadata.entry_id,
        archive.results.material.chemical_formula_reduced,
    )

# Convert the retrieved typed archives into a pandas dataframe.
dataframe = query.entries_to_dataframe(keys_to_filter=['metadata', 'results.material'])
print(dataframe)
