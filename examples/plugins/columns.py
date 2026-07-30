from nomad.config.models.ui import Column, Format

schema = 'nomad_example.schema_packages.mypackage.MySchema'
columns = [
    Column(
        search_quantity=f'data.mysection.myquantity#{schema}',
        label='My Quantity Name',
        unit='eV',
        align='left',
        format=Format(decimals=2, mode='standard'),
        selected=True,
    ),
    Column(
        search_quantity=f'data.my_repeated_section[*].myquantity#{schema}',
        align='middle',
        selected=False,
    ),
]
