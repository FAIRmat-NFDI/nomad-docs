import yaml
from nomad.config.models.ui import Dashboard

widgets_yaml = """
- type: periodic_table
  search_quantity: results.material.elements
  layout:
    lg: {x: 0, y: 0, w: 12, h: 6, minW: 3, minH: 3}  # Desktop: left half
    sm: {x: 0, y: 0, w: 12, h: 6, minW: 3, minH: 3}  # Phone: full width, on top
- type: terms
  search_quantity: results.method.simulation.program_name
  layout:
    lg: {x: 12, y: 0, w: 12, h: 6, minW: 3, minH: 3} # Desktop: right half
    sm: {x: 0, y: 6, w: 12, h: 6, minW: 3, minH: 3}  # Phone: full width, below
"""
dashboard = Dashboard.model_validate({'widgets': yaml.safe_load(widgets_yaml)})
