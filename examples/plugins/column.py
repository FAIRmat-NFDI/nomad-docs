from nomad.config.models.ui import Column

columns = [
    Column(
        search_quantity='data.mysection.myquantity#nomad_example.schema_packages.mypackage.MySchema',
        label='My Quantity Name',
        selected=True,
    ),
]
