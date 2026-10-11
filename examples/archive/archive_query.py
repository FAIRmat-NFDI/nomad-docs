from nomad.client import ArchiveQuery
from nomad.metainfo import units

query = ArchiveQuery(
    owner='public',
    query={
        'results.method.simulation.program_name': 'VASP',
        'results.material.elements': {'all': ['Ti', 'O']},
    },
    required={
        'workflow2': {
            'results': {
                'calculation_result_ref': {
                    'energy': {'total': '*'},
                    'system_ref': {'chemical_composition_reduced': '*'},
                },
            },
        },
    },
    results_max=5,
    page_size=5,
)

for archive in query.download():
    calculation = archive.workflow2.results.calculation_result_ref

    if not calculation or not calculation.system_ref:
        continue

    formula = calculation.system_ref.chemical_composition_reduced
    if calculation.energy.total:
        total_energy = calculation.energy.total.value.to(units.eV)
    else:
        total_energy = 'N/A'
    print(f'{formula}: {total_energy}')

# Convert the retrieved typed archives into a pandas dataframe.
dataframe = query.entries_to_dataframe(
    keys_to_filter=['workflow2.results.calculation_result_ref']
)
print(dataframe)
