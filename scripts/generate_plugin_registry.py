#!/usr/bin/env python3
"""
Generate plugin registry documentation from NOMAD API.

This script queries the NOMAD API for all plugins owned by FAIRmat-NFDI
and generates a markdown table with plugin metadata.
"""

import sys
from datetime import datetime
from pathlib import Path
from typing import Any

import requests


NOMAD_API_URL = "https://nomad-lab.eu/prod/v1/oasis/api/v1"
GITHUB_ORG = "FAIRmat-NFDI"


def query_plugins(owner_filter: str = GITHUB_ORG) -> list[dict[str, Any]]:
    """
    Query NOMAD API for all plugins owned by the specified GitHub organization.

    Args:
        owner_filter: GitHub organization name to filter by

    Returns:
        List of plugin data dictionaries
    """
    query_payload = {
        "owner": "visible",
        "query": {
            "and": [
                {
                    "data.owner#nomad_plugins.schema_packages.plugin.Plugin:any": [
                        owner_filter
                    ]
                },
                {"entry_type:all": ["Plugin"]},
            ]
        },
        "pagination": {
            "order_by": "upload_create_time",
            "order": "desc",
            "page_size": 100,
        },
        "required": {"exclude": ["quantities", "sections", "files"]},
    }

    url = f"{NOMAD_API_URL}/entries/query"
    all_plugins = []

    print(f"Querying NOMAD API for {owner_filter} plugins...")

    try:
        response = requests.post(url, json=query_payload, timeout=30)
        if not response.ok:
            print(f"API Error Response: {response.text}")
        response.raise_for_status()
        data = response.json()

        all_plugins.extend(data.get("data", []))
        total = data.get("pagination", {}).get("total", 0)

        print(f"Found {total} plugins")

        # Handle pagination if there are more results
        page = 1
        while len(all_plugins) < total:
            page += 1
            query_payload["pagination"]["page"] = page
            response = requests.post(url, json=query_payload, timeout=30)
            response.raise_for_status()
            data = response.json()
            all_plugins.extend(data.get("data", []))
            print(f"Fetched page {page}, total plugins: {len(all_plugins)}")

    except requests.exceptions.RequestException as e:
        print(f"Error querying NOMAD API: {e}")
        sys.exit(1)

    return all_plugins


def extract_plugin_metadata(plugin_entry: dict[str, Any]) -> dict[str, Any]:
    """
    Extract relevant metadata from a plugin entry.

    Args:
        plugin_entry: Raw plugin entry from NOMAD API

    Returns:
        Dictionary with extracted metadata
    """
    data = plugin_entry.get("data", {})

    # Extract plugin entry points and their types
    entry_points = data.get("plugin_entry_points", [])
    entry_point_types = set()
    entry_point_names = []

    for ep in entry_points:
        if ep_type := ep.get("type"):
            entry_point_types.add(ep_type)
        if ep_name := ep.get("name"):
            entry_point_names.append(ep_name)

    # Format authors
    authors = data.get("authors", [])
    author_list = []
    for author in authors:
        if name := author.get("name"):
            author_list.append(name)

    # Format maintainers
    maintainers = data.get("maintainers", [])
    maintainer_list = []
    for maintainer in maintainers:
        if name := maintainer.get("name"):
            maintainer_list.append(name)

    return {
        "name": data.get("name", "Unknown"),
        "description": data.get("description", ""),
        "repository": data.get("repository", ""),
        "owner": data.get("owner", ""),
        "stars": data.get("stars", 0),
        "created": data.get("created", ""),
        "last_updated": data.get("last_updated", ""),
        "on_central": data.get("on_central", False),
        "on_example_oasis": data.get("on_example_oasis", False),
        "on_pypi": data.get("on_pypi", False),
        "entry_point_types": sorted(entry_point_types),
        "entry_point_names": entry_point_names,
        "authors": author_list,
        "maintainers": maintainer_list,
        "plugin_dependencies": [
            dep.get("name", "") for dep in data.get("plugin_dependencies", [])
        ],
    }


def format_date(iso_date: str) -> str:
    """Format ISO date string to readable format."""
    try:
        dt = datetime.fromisoformat(iso_date.replace("Z", "+00:00"))
        return dt.strftime("%Y-%m-%d")
    except (ValueError, AttributeError):
        return iso_date


def generate_markdown_table(plugins: list[dict[str, Any]]) -> str:
    """
    Generate markdown table from plugin metadata.

    Args:
        plugins: List of plugin metadata dictionaries

    Returns:
        Markdown formatted table
    """
    if not plugins:
        return "No plugins found.\n"

    # Sort plugins by name
    plugins_sorted = sorted(plugins, key=lambda x: x["name"].lower())

    markdown = []
    markdown.append(
        "| Plugin | Description | Type(s) | PyPI | Central | Repository | Stars |"
    )
    markdown.append(
        "|--------|-------------|---------|------|---------|------------|-------|"
    )

    for plugin in plugins_sorted:
        name = plugin["name"]
        description = (
            plugin["description"][:80] + "..."
            if len(plugin["description"]) > 80
            else plugin["description"]
        )
        description = description.replace("|", "\\|").replace("\n", " ")

        # Format entry point types
        types = (
            ", ".join(plugin["entry_point_types"])
            if plugin["entry_point_types"]
            else "—"
        )

        # Format boolean indicators
        pypi = "✓" if plugin["on_pypi"] else "—"
        central = "✓" if plugin["on_central"] else "—"

        # Format repository link
        repo_url = plugin["repository"]
        repo_name = (
            repo_url.split("github.com/")[-1] if "github.com" in repo_url else repo_url
        )
        repo_link = f"[{repo_name}]({repo_url})" if repo_url else "—"

        stars = plugin["stars"]

        markdown.append(
            f"| **{name}** | {description} | {types} | {pypi} | {central} | {repo_link} | {stars} |"
        )

    return "\n".join(markdown)


def generate_detailed_list(plugins: list[dict[str, Any]]) -> str:
    """
    Generate detailed list view of plugins with all metadata.

    Args:
        plugins: List of plugin metadata dictionaries

    Returns:
        Markdown formatted detailed list
    """
    if not plugins:
        return "No plugins found.\n"

    # Sort plugins by name
    plugins_sorted = sorted(plugins, key=lambda x: x["name"].lower())

    markdown = []

    for plugin in plugins_sorted:
        markdown.append(f"\n### {plugin['name']}")
        markdown.append("")

        if plugin["description"]:
            markdown.append(plugin["description"])
            markdown.append("")

        # Repository and metadata
        if plugin["repository"]:
            markdown.append(
                f"**Repository:** [{plugin['repository']}]({plugin['repository']})"
            )

        markdown.append(f"**Owner:** {plugin['owner']}")
        markdown.append(f"**Stars:** ⭐ {plugin['stars']}")
        markdown.append(f"**Created:** {format_date(plugin['created'])}")
        markdown.append(f"**Last Updated:** {format_date(plugin['last_updated'])}")
        markdown.append("")

        # Deployment status
        deployments = []
        if plugin["on_pypi"]:
            deployments.append("PyPI")
        if plugin["on_central"]:
            deployments.append("NOMAD Central")
        if plugin["on_example_oasis"]:
            deployments.append("Example Oasis")

        if deployments:
            markdown.append(f"**Available on:** {', '.join(deployments)}")
            markdown.append("")

        # Entry points
        if plugin["entry_point_types"]:
            markdown.append(
                f"**Plugin Types:** {', '.join(plugin['entry_point_types'])}"
            )
            markdown.append("")

        if plugin["entry_point_names"]:
            markdown.append("**Entry Points:**")
            for ep_name in plugin["entry_point_names"]:
                markdown.append(f"- `{ep_name}`")
            markdown.append("")

        # Authors and maintainers
        if plugin["authors"]:
            authors_str = ", ".join(plugin["authors"])
            markdown.append(f"**Authors:** {authors_str}")
            markdown.append("")

        if plugin["maintainers"]:
            maintainers_str = ", ".join(plugin["maintainers"])
            markdown.append(f"**Maintainers:** {maintainers_str}")
            markdown.append("")

        # Dependencies
        if plugin["plugin_dependencies"]:
            markdown.append("**Plugin Dependencies:**")
            for dep in plugin["plugin_dependencies"]:
                markdown.append(f"- {dep}")
            markdown.append("")

        markdown.append("---")

    return "\n".join(markdown)


def generate_registry_page(plugins: list[dict[str, Any]], output_path: Path) -> None:
    """
    Generate the complete plugin registry markdown page.

    Args:
        plugins: List of plugin metadata dictionaries
        output_path: Path to write the markdown file
    """
    plugin_metadata = [extract_plugin_metadata(p) for p in plugins]

    # Generate statistics
    total_plugins = len(plugin_metadata)
    on_pypi = sum(1 for p in plugin_metadata if p["on_pypi"])
    on_central = sum(1 for p in plugin_metadata if p["on_central"])

    entry_point_type_counts = {}
    for plugin in plugin_metadata:
        for ep_type in plugin["entry_point_types"]:
            entry_point_type_counts[ep_type] = (
                entry_point_type_counts.get(ep_type, 0) + 1
            )

    # Build the page
    page_content = []
    page_content.append("# NOMAD Plugin Registry")
    page_content.append("")
    page_content.append(
        f"This page provides an overview of all NOMAD plugins maintained by the **{GITHUB_ORG}** organization."
    )
    page_content.append("")
    page_content.append(
        f"**Last Updated:** {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}"
    )
    page_content.append("")

    # Statistics section
    page_content.append("## Statistics")
    page_content.append("")
    page_content.append(f"- **Total Plugins:** {total_plugins}")
    page_content.append(f"- **Available on PyPI:** {on_pypi}")
    page_content.append(f"- **Deployed on NOMAD Central:** {on_central}")
    page_content.append("")

    if entry_point_type_counts:
        page_content.append("**Plugin Types:**")
        page_content.append("")
        for ep_type, count in sorted(entry_point_type_counts.items()):
            page_content.append(f"- {ep_type}: {count}")
        page_content.append("")

    # Quick reference table
    page_content.append("## Plugin Overview")
    page_content.append("")
    page_content.append("Quick reference table of all available plugins:")
    page_content.append("")
    page_content.append(generate_markdown_table(plugin_metadata))
    page_content.append("")

    # Detailed listings
    page_content.append("## Detailed Plugin Information")
    page_content.append("")
    page_content.append(generate_detailed_list(plugin_metadata))
    page_content.append("")

    # Footer
    page_content.append("---")
    page_content.append("")
    page_content.append('!!! info "About this page"')
    page_content.append(
        "    This page is automatically generated from the NOMAD API and updated weekly."
    )
    page_content.append(
        f"    The data includes all plugins owned by the {GITHUB_ORG} GitHub organization."
    )
    page_content.append(
        "    For more information about NOMAD plugins, see the [plugin documentation](../howto/plugins/plugins.md)."
    )
    page_content.append("")

    # Write to file
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(page_content), encoding="utf-8")
    print(f"Plugin registry written to {output_path}")


def main():
    """Main entry point."""
    # Determine output path
    script_dir = Path(__file__).parent
    docs_dir = script_dir.parent / "docs" / "examples"
    output_path = docs_dir / "plugin_registry.md"

    # Query plugins
    plugins = query_plugins(GITHUB_ORG)

    if not plugins:
        print("Warning: No plugins found!")
        # Still generate the page with a message
        output_path.write_text(
            "# NOMAD Plugin Registry\n\n"
            f"No plugins found for organization: {GITHUB_ORG}\n\n"
            f"Last checked: {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}\n",
            encoding="utf-8",
        )
        return

    # Generate the registry page
    generate_registry_page(plugins, output_path)

    print(f"Successfully generated plugin registry with {len(plugins)} plugins")


if __name__ == "__main__":
    main()
