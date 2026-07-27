from nomad.config.models.ui import Column, Format

columns = [
    Column(
        search_quantity='data.mysection.myquantity#nomad_example.schema_packages.mypackage.MySchema',
        label='My Quantity Name',
        unit='eV',
        align='left',
        format=Format(decimals= 2, mode='standard'),
        selected=True,
    ),
    Column(
        search_quantity='data.mysection.my_other_quantity#nomad_example.schema_packages.mypackage.MySchema',
        align='middle',
        selected=False,
    ),
]
