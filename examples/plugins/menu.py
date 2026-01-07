from nomad.config.models.ui import Axis, Menu, MenuItemTerms, MenuItemHistogram

# This is a top level menu that is always visible. It shows two items: a terms
# item and a submenu beneath it.
menu = Menu(
    size='sm',
    items=[
        MenuItemTerms(search_quantity='authors.name', options=5),
        # This is a submenu whose items become visible once selected. It
        # contains three items: one full-width histogram and two terms items
        # which are displayed side-by-side.
        Menu(
            title='Submenu',
            size='md',
            items=[
                MenuItemHistogram(x=Axis(search_quantity='upload_create_time')),
                # These items target data from a custom schema
                MenuItemTerms(
                    width=6,
                    search_quantity='data.quantity1#nomad_example.schema_packages.mypackage.MySchema',
                ),
                MenuItemTerms(
                    width=6,
                    search_quantity='data.quantity2#nomad_example.schema_packages.mypackage.MySchema',
                ),
            ],
        ),
    ],
)
