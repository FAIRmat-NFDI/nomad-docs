from nomad.config.models.ui import (
    Axis,
    Dashboard,
    Layout,
    WidgetBoxPlot,
    WidgetHistogram,
    WidgetPeriodicTable,
    WidgetScatterPlot,
    WidgetTerms,
)

schema = 'nomad_example.schema_packages.mypackage.MySchema'

dashboard = Dashboard(
    widgets=[
        WidgetPeriodicTable(
            title='Elements of the material',
            search_quantity='results.material.elements',
            scale='linear',
            layout={'lg': Layout(w=12, h=6, x=0, y=0)},
        ),
        WidgetTerms(
            title='Widget Terms Title',
            search_quantity=f'data.mysection.myquantity#{schema}',
            showinput=True,
            scale='linear',
            layout={'lg': Layout(w=12, h=6, x=0, y=6)},
        ),
        WidgetBoxPlot(
            title='Widget Box Plot Title',
            y=Axis(
                search_quantity=f'data.mysection.mynumericalquantity#{schema}',
                title='quantity y',
            ),
            autorange=True,
            subgroup_by_size=5,
            subgroup_by='data.mysection.mycategoricalquantity#{schema}',
            group_by_size=5,
            group_by='data.mysection.myothercategoricalquantity#{schema}',
            show_points=True,
            sample_size=1000,
            layout={'lg': Layout(w=12, h=6, x=0, y=12)},
        ),
        WidgetHistogram(
            title='Histogram Title',
            show_input=False,
            autorange=True,
            nbins=30,
            scale='linear',
            x=Axis(search_quantity=f'data.mysection.myquantity#{schema}'),
            layout={'lg': Layout(w=12, h=6, x=0, y=18)},
        ),
        WidgetScatterPlot(
            title='Scatterplot title',
            autorange=True,
            x=Axis(
                search_quantity=f'data.mysection.mynumericalquantity#{schema}',
                title='quantity x',
            ),
            y=Axis(search_quantity=f'data.mysection.myothernumericalquantity#{schema}'),
            color=f'data.mysection.myquantity#{schema}',  # optional, if set has to be scalar value
            size=1000,  # maximum number of entries loaded
            layout={'lg': Layout(w=12, h=6, x=0, y=24)},
        ),
    ]
)
