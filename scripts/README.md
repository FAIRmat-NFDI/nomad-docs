# Documentation Scripts

This directory contains scripts for automating documentation tasks.

## generate_plugin_registry.py

Automatically generates the [Plugin Registry](../docs/examples/plugin_registry.md) page by querying the NOMAD API for all available plugin entries.

### Features

- Queries the NOMAD API for plugin metadata
- Retrieves all plugin entries from NOMAD (no owner restriction)
- Creates a quick reference table with key metadata
- Adds interactive filtering:
  - Multi-select entry point type (`Containing`)
  - Multi-select owner (`FAIRmat`, `Non-FAIRmat`, and non-FAIRmat owners with 5+ plugins)
- Adds interactive sorting:
  - Name (A→Z / Z→A)
  - Stars (high→low)
- Adds two dynamic pie charts that update with all active filters:
  - Entry Point Type distribution
  - Owner distribution (with non-major non-FAIRmat owners grouped as `Other`)
- Adds a dynamic status notice between filters and charts:
  - Warning when any non-FAIRmat plugin is included
  - Success message when only FAIRmat plugins are shown
- Provides detailed information for each plugin including:
  - Description and repository links
  - Stars, creation/update dates
  - Deployment status (PyPI, NOMAD Central, Example Oasis)
  - Entry point types and names
  - Authors and maintainers
  - Plugin dependencies

### Usage

```bash
# Run directly
python scripts/generate_plugin_registry.py

# Or with uv
uv run python scripts/generate_plugin_registry.py
```

The script will:
1. Query the NOMAD API at `https://nomad-lab.eu/prod/v1/api/v1/entries/query` (and fall back to `.../oasis/...` if needed)
2. Extract and process plugin metadata
3. Generate the interactive registry markup at `docs/examples/plugin_registry.md`

### Automation

The plugin registry is automatically updated via GitHub Actions workflow:
- **Schedule**: Monthly on the 1st at 00:00 UTC
- **Workflow**: `.github/workflows/update-plugin-registry.yml`
- **Manual trigger**: Available via GitHub Actions UI

The workflow will:
1. Run the generation script
2. Check for changes
3. Create a pull request with any changes for review before merging

### Configuration

To change the NOMAD API endpoint (e.g., for different deployments):

```python
NOMAD_API_URL = "https://nomad-lab.eu/prod/v1/api/v1"  # Modify as needed
```
