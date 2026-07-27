from nomad.config.models.ui import RowActionNorth, RowActions, RowActionURL, Rows

rows = Rows(
    actions=RowActions(
        items=[
            RowActionURL(icon='launch', path='data.url', description='Open a link.'),
            RowActionNorth(
                icon='launch',
                filepath='data.filepath',
                tool_name='jupyter',
                description="Open file in Jupyter"
            )
        ]
    )
)
