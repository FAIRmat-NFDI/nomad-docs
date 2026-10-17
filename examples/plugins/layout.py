from nomad.config.models.ui import Dashboard, Layout, WidgetPeriodicTable, WidgetTerms

dashboard = Dashboard(
    widgets=[
        WidgetPeriodicTable(
            search_quantity='results.material.elements',
            layout={
                'lg': Layout(x=0, y=0, w=12, h=6),  # Desktop: left half
                'sm': Layout(x=0, y=0, w=12, h=6),  # Phone: full width, on top
            },
        ),
        WidgetTerms(
            search_quantity='results.method.simulation.program_name',
            layout={
                'lg': Layout(x=12, y=0, w=12, h=6),  # Desktop: right half
                'sm': Layout(x=0, y=6, w=12, h=6),  # Phone: full width, below
            },
        ),
    ]
)
