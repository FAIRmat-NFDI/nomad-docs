# Documentation Scripts

This directory contains scripts for automating documentation tasks.

## generate_plugin_registry.py

Automatically generates the [Plugin Registry](../docs/examples/plugin_registry.md) page by querying the NOMAD API for all plugins owned by the FAIRmat-NFDI and nomad-coe GitHub organizations.

### Features

- Queries the NOMAD Oasis API for plugin metadata
- Filters plugins by GitHub organization (default: FAIRmat-NFDI)
- Generates statistics (total plugins, PyPI availability, deployment status, plugin types)
- Creates a quick reference table with key metadata
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
uv run --with requests python scripts/generate_plugin_registry.py
```

The script will:
1. Query the NOMAD API at `https://nomad-lab.eu/prod/v1/oasis/api/v1/entries/query`
2. Extract and process plugin metadata
3. Generate the markdown file at `docs/examples/plugin_registry.md`

### Automation

The plugin registry is automatically updated via GitHub Actions workflow:
- **Schedule**: Monthly on the 1st at 00:00 UTC
- **Workflow**: `.github/workflows/update-plugin-registry.yml`
- **Manual trigger**: Available via GitHub Actions UI

The workflow will:
1. Run the generation script
2. Check for changes
3. Commit and push updates to the repository
4. Create a pull request for scheduled runs (for review before deployment)

### Configuration

To change the GitHub organizations being queried, modify the `GITHUB_ORGS` list in the script:

```python
GITHUB_ORGS = ["FAIRmat-NFDI", "nomad-coe"]  # Add or remove organizations as needed
```

To change the NOMAD API endpoint (e.g., for different deployments):

```python
NOMAD_API_URL = "https://nomad-lab.eu/prod/v1/oasis/api/v1"  # Modify as needed
```

### Dependencies

- `requests`: For HTTP API calls to NOMAD

These are automatically provided by `uv run --with requests` in the workflow.
