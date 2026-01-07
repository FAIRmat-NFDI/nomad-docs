from nomad.config.models.ui import Column

columns = [
    Column(quantity='entry_id', selected=True),
    Column(
        quantity='data.mysection.myquantity#nomad_example.schema_packages.mypackage.MySchema',
        label='My Quantity Name',
        selected=True,
    ),
    Column(quantity='upload_create_time'),
]
