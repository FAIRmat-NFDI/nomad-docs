from nomad.config.models.plugins import AppEntryPoint
from nomad.config.models.ui import (
    App,
    Axis,
    Column,
    Dashboard,
    Format,
    Layout,
    Menu,
    MenuItemHistogram,
    MenuItemPeriodicTable,
    MenuItemTerms,
    WidgetHistogram,
)

schema = 'nomad_example.schema_packages.mypackage.MySchema'
myapp = AppEntryPoint(
    name='MyApp',
    description='App defined using the new plugin mechanism.',
    app=App(
        # Label of the App
        label='My App',
        # Path used in the URL, must be unique
        path='myapp',
        # Used to categorize apps in the explore menu
        category='Theory',
        # Brief description used in the app menu
        description='An app customized for me.',
        # Longer description that can also use markdown
        readme='Here is a much longer description of this app.',
        # Controls which columns are shown in the results table
        columns=[
            Column(search_quantity='entry_id', selected=True),
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
            Column(search_quantity='upload_create_time'),
        ],
        # Dictionary of search filters that are always enabled for queries made
        # within this app. This is especially important to narrow down the
        # results to the wanted subset. Any available search filter can be
        # targeted here. This example makes sure that only entries that use
        # MySchema are included.
        filters_locked={'section_defs.definition_qualified_name': [schema]},
        # Controls the menu shown on the left
        menu=Menu(
            title='Material',
            items=[
                Menu(
                    title='elements',
                    items=[
                        MenuItemPeriodicTable(
                            search_quantity='results.material.elements',
                        ),
                        MenuItemTerms(
                            search_quantity='results.material.chemical_formula_hill',
                            width=6,
                            options=0,
                        ),
                        MenuItemTerms(
                            search_quantity='results.material.chemical_formula_iupac',
                            width=6,
                            options=0,
                        ),
                        MenuItemHistogram(
                            x='results.material.n_elements',
                        ),
                    ],
                )
            ],
        ),
        # Controls the default dashboard shown in the search interface
        dashboard=Dashboard(
            widgets=[
                WidgetHistogram(
                    title='Histogram Title',
                    show_input=False,
                    autorange=True,
                    nbins=30,
                    scale='linear',
                    x=Axis(search_quantity=f'data.mysection.myquantity#{schema}'),
                    layout={'lg': Layout(w=12, h=4, x=0, y=0)},
                )
            ]
        ),
    ),
)
