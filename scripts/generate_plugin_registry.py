#!/usr/bin/env python3
"""
Generate plugin registry documentation from NOMAD API.

This script queries the NOMAD API for all plugin entries
and generates a markdown table with plugin metadata.
"""

from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import regex
import requests

NOMAD_API_URL = 'https://nomad-lab.eu/prod/v1/api/v1'
NOMAD_OASIS_API_URL = 'https://nomad-lab.eu/prod/v1/oasis/api/v1'
OWNER_SCOPES = ['public', 'visible']
FAIRMAT_OWNERS = {'fairmat-nfdi', 'nomad-coe', 'nomadcoe'}

# Link pattern for fixing external links
LINK_PATTERN = regex.compile(
    r"""
    (                               # Group 1: [text](url)
      \[[^\]]+\]                    # [text]
      \(                             # opening paren of URL
        (?:https?|ftp)://            # protocol
        (?:[^()\s]+|                 # non-parens
           \((?:[^()]+|(?R))*\)      # balanced (...)
        )+
      \)                             # closing paren of Markdown link
    )
    (\{[^\}]*\})?                   # Group 2: optional {attrs}
    """,
    regex.VERBOSE,
)


def query_plugins_from_endpoint(base_url: str, owner_scope: str) -> list[dict[str, Any]]:
    """
    Query a NOMAD API endpoint for all plugin entries.

    Returns:
        List of plugin data dictionaries
    """
    query_payload = {
        'owner': owner_scope,
        'query': {'entry_type:all': ['Plugin']},
        'pagination': {
            'order_by': 'upload_create_time',
            'order': 'desc',
            'page_size': 100,
        },
        'required': {'exclude': ['quantities', 'sections', 'files']},
    }

    url = f'{base_url}/entries/query'
    all_plugins = []

    try:
        response = requests.post(url, json=query_payload, timeout=30)
        if not response.ok:
            print(f'API Error Response: {response.text}')
        response.raise_for_status()
        data = response.json()

        all_plugins.extend(data.get('data', []))
        total = data.get('pagination', {}).get('total', 0)

        # Handle pagination if there are more results
        page = 1
        while len(all_plugins) < total:
            page += 1
            query_payload['pagination']['page'] = page
            response = requests.post(url, json=query_payload, timeout=30)
            response.raise_for_status()
            data = response.json()
            all_plugins.extend(data.get('data', []))

    except requests.exceptions.RequestException as e:
        print(f'Error querying {base_url} (owner="{owner_scope}"): {e}')
        return []

    return all_plugins


def query_plugins() -> list[dict[str, Any]]:
    """Query multiple API routes/scopes and merge plugin results."""
    endpoints = [NOMAD_API_URL, NOMAD_OASIS_API_URL]
    seen_entry_ids = set()
    merged_plugins = []

    for endpoint in endpoints:
        for owner_scope in OWNER_SCOPES:
            plugins = query_plugins_from_endpoint(endpoint, owner_scope)
            if not plugins:
                continue
            for plugin in plugins:
                entry_id = plugin.get('entry_id') or plugin.get('entryid')
                if entry_id and entry_id in seen_entry_ids:
                    continue
                if entry_id:
                    seen_entry_ids.add(entry_id)
                merged_plugins.append(plugin)

        if merged_plugins:
            # If primary endpoint yields data, no need to rely on fallback endpoint.
            break

    return merged_plugins


def extract_plugin_metadata(plugin_entry: dict[str, Any]) -> dict[str, Any]:
    """
    Extract relevant metadata from a plugin entry.

    Args:
        plugin_entry: Raw plugin entry from NOMAD API

    Returns:
        Dictionary with extracted metadata
    """
    data = plugin_entry.get('data', {})

    # Extract plugin entry points and their types
    entry_points = data.get('plugin_entry_points', [])
    entry_point_types = set()
    entry_point_names = []

    for ep in entry_points:
        if ep_type := ep.get('type'):
            entry_point_types.add(ep_type)
        if ep_name := ep.get('name'):
            entry_point_names.append(ep_name)

    # Format authors
    authors = data.get('authors', [])
    author_list = []
    for author in authors:
        if name := author.get('name'):
            author_list.append(name)

    # Format maintainers
    maintainers = data.get('maintainers', [])
    maintainer_list = []
    for maintainer in maintainers:
        if name := maintainer.get('name'):
            maintainer_list.append(name)

    # Check for GitHub Pages documentation
    repo_url = data.get('repository', '')
    docs_url = check_github_pages_exists(repo_url)
    
    return {
        'name': data.get('name', 'Unknown'),
        'description': data.get('description', ''),
        'repository': repo_url,
        'docs_url': docs_url,
        'owner': data.get('owner', ''),
        'stars': data.get('stars', 0),
        'created': data.get('created', ''),
        'last_updated': data.get('last_updated', ''),
        'on_central': data.get('on_central', False),
        'on_example_oasis': data.get('on_example_oasis', False),
        'on_pypi': data.get('on_pypi', False),
        'entry_point_types': sorted(entry_point_types),
        'entry_point_names': entry_point_names,
        'authors': author_list,
        'maintainers': maintainer_list,
        'plugin_dependencies': [
            dep.get('name', '') for dep in data.get('plugin_dependencies', [])
        ],
    }


def check_github_pages_exists(repo_url: str) -> str | None:
    """
    Check if GitHub Pages documentation exists for a repository.
    
    Args:
        repo_url: GitHub repository URL (e.g., https://github.com/owner/repo)
    
    Returns:
        GitHub Pages URL if it exists, None otherwise
    """
    if not repo_url or 'github.com' not in repo_url:
        return None
    
    try:
        # Extract owner and repo name from GitHub URL
        # Expected format: https://github.com/owner/repo
        parts = repo_url.rstrip('/').split('github.com/')[-1].split('/')
        if len(parts) < 2:
            return None
        
        owner, repo = parts[0], parts[1]
        
        # Construct GitHub Pages URL
        # Convert owner to lowercase for GitHub Pages URL
        gh_pages_url = f'https://{owner.lower()}.github.io/{repo}/'
        
        # Make a HEAD request to check if the page exists
        response = requests.head(gh_pages_url, timeout=5, allow_redirects=True)
        
        # Consider 200 and 301/302 (redirects) as success
        if response.status_code in (200, 301, 302):
            return gh_pages_url
        
    except (requests.exceptions.RequestException, IndexError, ValueError):
        pass
    
    return None


def format_date(iso_date: str) -> str:
    """Format ISO date string to readable format."""
    try:
        dt = datetime.fromisoformat(iso_date.replace('Z', '+00:00'))
        return dt.strftime('%Y-%m-%d')
    except (ValueError, AttributeError):
        return iso_date


def is_fairmat_owner(owner: str) -> bool:
    """Return True if owner should be grouped under FAIRmat."""
    return owner.strip().lower() in FAIRMAT_OWNERS


def normalize_attrs(attrs: str | None) -> str:
    """Ensure target and rel are both present in link attributes."""
    if not attrs:
        return '{:target="_blank" rel="noopener"}'

    inner: str = attrs.strip()[1:-1].strip()  # remove { }
    parts: list[str] = inner.split()
    attrs_dict: dict[str, str | None] = {}

    for part in parts:
        if '=' in part:
            k, v = part.split('=', 1)
            attrs_dict[k.strip(':')] = v.strip('"')
        else:
            attrs_dict[part.strip(':')] = None

    # Always enforce target and rel
    attrs_dict['target'] = '_blank'
    attrs_dict['rel'] = 'noopener'

    return (
        '{:' + ' '.join(f'{k}="{v}"' if v else k for k, v in attrs_dict.items()) + '}'
    )


def fix_external_links(text: str) -> str:
    """Fix external links to include target and rel attributes."""

    def repl(match: regex.Match) -> str:
        link, attrs = match.groups()
        return link + normalize_attrs(attrs)

    new_text, _ = LINK_PATTERN.subn(repl, text)
    return new_text


def fix_markdown_lint_issues(text: str) -> str:
    """Fix common markdownlint issues in the generated content."""
    lines = text.split('\n')
    fixed_lines = []

    for i, line in enumerate(lines):
        # Fix MD044: Replace "Nomad" with "nomad" (but not in URLs or "NOMAD")
        # Only replace standalone "Nomad" that's not part of "NOMAD"
        if 'Nomad' in line and 'NOMAD' not in line:
            line = line.replace('Nomad', 'nomad')

        # Fix MD034: Wrap bare URLs in angle brackets (look for URLs not in markdown links or HTML)
        # Pattern: URL not preceded by ]( or href=" and not followed by " (for HTML)
        import re

        # Find bare URLs that are not already in markdown links or HTML href attributes
        # Negative lookbehind: not preceded by ]( or href=" or href='
        # Negative lookahead: not followed by " or '
        bare_url_pattern = re.compile(
            r'(?<!\]\()(?<!href=")(?<!href=\')https?://[^\s<>\[\]"\']+(?!["\'])'
        )
        line = bare_url_pattern.sub(lambda m: f'<{m.group(0)}>', line)

        fixed_lines.append(line)

    # Fix MD032: Ensure blank lines around lists
    final_lines = []
    for i, line in enumerate(fixed_lines):
        # Check if current line starts a list
        is_list_start = line.strip().startswith(('- ', '* ', '1. '))
        # Check if previous line exists and is not blank and not a list item
        prev_line = fixed_lines[i - 1] if i > 0 else ''
        prev_is_blank = not prev_line.strip()
        prev_is_list = prev_line.strip().startswith(('- ', '* ', '1. '))

        # Add blank line before list if needed
        if is_list_start and not prev_is_blank and not prev_is_list and i > 0:
            final_lines.append('')

        final_lines.append(line)

    # Fix MD012: Remove multiple consecutive blank lines
    result_lines = []
    blank_count = 0
    for line in final_lines:
        if not line.strip():
            blank_count += 1
            if blank_count <= 1:
                result_lines.append(line)
        else:
            blank_count = 0
            result_lines.append(line)

    return '\n'.join(result_lines)


def generate_markdown_table(plugins: list[dict[str, Any]]) -> str:
    """
    Generate markdown table from plugin metadata with embedded details dropdown.

    Args:
        plugins: List of plugin metadata dictionaries

    Returns:
        Markdown formatted HTML table with collapsible details
    """
    if not plugins:
        return 'No plugins found.\n'

    # Sort plugins by name
    plugins_sorted = sorted(plugins, key=lambda x: x['name'].lower())

    markdown = []
    all_entry_point_types = sorted(
        {
            ep_type
            for plugin in plugins_sorted
            for ep_type in plugin.get('entry_point_types', [])
        }
    )
    owner_display_by_normalized = {}
    owner_counts_by_normalized = {}
    for plugin in plugins_sorted:
        owner = (plugin.get('owner') or '').strip()
        if not owner:
            continue
        normalized = owner.lower()
        owner_counts_by_normalized[normalized] = (
            owner_counts_by_normalized.get(normalized, 0) + 1
        )
        if normalized not in owner_display_by_normalized:
            owner_display_by_normalized[normalized] = owner

    has_fairmat_owners = any(
        is_fairmat_owner(owner) for owner in owner_display_by_normalized
    )
    has_non_fairmat_owners = any(
        not is_fairmat_owner(owner) for owner in owner_display_by_normalized
    )
    other_owner_labels = sorted(
        (
            label
            for normalized, label in owner_display_by_normalized.items()
            if (
                not is_fairmat_owner(normalized)
                and owner_counts_by_normalized.get(normalized, 0) >= 5
            )
        ),
        key=str.lower,
    )

    markdown.append('<div class="plugin-registry-filter" data-plugin-registry-filter>')
    markdown.append('<label class="plugin-registry-filter__label plugin-registry-filter__label--type">Containing</label>')
    markdown.append('<select class="plugin-registry-filter__select plugin-registry-filter__type">')
    markdown.append('<option value="">All entry point types</option>')
    for ep_type in all_entry_point_types:
        markdown.append(f'<option value="{ep_type}">{ep_type}</option>')
    markdown.append('</select>')
    markdown.append('<label class="plugin-registry-filter__label plugin-registry-filter__label--owner">Owner</label>')
    markdown.append('<select class="plugin-registry-filter__select plugin-registry-filter__owner">')
    markdown.append('<option value="">All owners</option>')
    if has_fairmat_owners:
        markdown.append('<option value="__fairmat__">FAIRmat</option>')
    if has_non_fairmat_owners:
        markdown.append('<option value="__non_fairmat__">Non-FAIRmat</option>')
    for owner_label in other_owner_labels:
        markdown.append(f'<option value="{owner_label}">{owner_label}</option>')
    markdown.append('</select>')
    markdown.append('<label class="plugin-registry-filter__label plugin-registry-filter__label--sort">Sort</label>')
    markdown.append('<select class="plugin-registry-filter__select plugin-registry-filter__sort">')
    markdown.append('<option value="name_asc">Name (A→Z)</option>')
    markdown.append('<option value="name_desc">Name (Z→A)</option>')
    markdown.append('<option value="stars_desc">Stars (high→low)</option>')
    markdown.append('</select>')
    markdown.append(
        '<button class="plugin-registry-filter__clear" type="button">Clear</button>'
    )
    markdown.append(
        '<span class="plugin-registry-filter__count" aria-live="polite"></span>'
    )
    markdown.append('</div>')
    markdown.append('')
    markdown.append(
        '<div class="plugin-registry-notice" data-plugin-registry-notice aria-live="polite"></div>'
    )
    markdown.append('')
    markdown.append('<div class="plugin-registry-chart" data-plugin-registry-chart>')
    markdown.append('<p class="plugin-registry-chart__title"><strong>Filtered Distributions</strong></p>')
    markdown.append('<div class="plugin-registry-chart__panels">')
    markdown.append('<section class="plugin-registry-chart__panel" data-chart-kind="type">')
    markdown.append('<p class="plugin-registry-chart__panel-title"><strong>Entry Point Type</strong></p>')
    markdown.append('<div class="plugin-registry-chart__panel-content">')
    markdown.append('<div class="plugin-registry-chart__pie-wrap">')
    markdown.append(
        '<div class="plugin-registry-chart__pie" role="img" aria-label="Plugin type distribution pie chart">'
    )
    markdown.append('<span class="plugin-registry-chart__pie-total">0</span>')
    markdown.append('</div>')
    markdown.append('</div>')
    markdown.append('<div class="plugin-registry-chart__legend"></div>')
    markdown.append('</div>')
    markdown.append('</section>')
    markdown.append('<section class="plugin-registry-chart__panel" data-chart-kind="owner">')
    markdown.append('<p class="plugin-registry-chart__panel-title"><strong>Owner</strong></p>')
    markdown.append('<div class="plugin-registry-chart__panel-content">')
    markdown.append('<div class="plugin-registry-chart__pie-wrap">')
    markdown.append(
        '<div class="plugin-registry-chart__pie" role="img" aria-label="Plugin owner distribution pie chart">'
    )
    markdown.append('<span class="plugin-registry-chart__pie-total">0</span>')
    markdown.append('</div>')
    markdown.append('</div>')
    markdown.append('<div class="plugin-registry-chart__legend"></div>')
    markdown.append('</div>')
    markdown.append('</section>')
    markdown.append('</div>')
    markdown.append('</div>')
    markdown.append('')
    markdown.append('<table class="plugin-registry-table" data-plugin-registry="true">')
    markdown.append('<thead>')
    markdown.append(
        '<tr><th>Plugin</th><th>Description</th><th>Deployment</th><th>Links</th></tr>'
    )
    markdown.append('</thead>')
    markdown.append('<tbody>')

    for index, plugin in enumerate(plugins_sorted):
        name = plugin['name']
        description = plugin['description'] if plugin['description'].strip() else '—'
        description = description.replace('|', '\\|').replace('\n', ' ')

        # Format entry point types
        types = (
            ', '.join(plugin['entry_point_types'])
            if plugin['entry_point_types']
            else '—'
        )
        normalized_types = '|'.join(
            ep_type.strip().lower() for ep_type in plugin['entry_point_types']
        )
        owner = (plugin.get('owner') or '').strip()
        normalized_owner = owner.lower()
        owner_group = 'fairmat' if is_fairmat_owner(normalized_owner) else 'other'
        safe_name = name.replace('"', '&quot;')
        safe_owner = owner.replace('"', '&quot;')
        row_id = f'plugin-registry-row-{index}'

        # Format deployment status
        deployments = []
        if plugin['on_pypi']:
            deployments.append('PyPI')
        if plugin['on_central']:
            deployments.append('NOMAD')
        if plugin['on_example_oasis']:
            deployments.append('Example Oasis')
        deployment_text = '<br> '.join(deployments) if deployments else '—'

        # Format repository and documentation links
        repo_url = plugin['repository']
        # Strip angle brackets if present (e.g., <https://...> becomes https://...)
        if repo_url:
            repo_url = repo_url.strip('<>').strip()
        
        docs_url = plugin.get('docs_url')
        
        if repo_url and docs_url:
            links = f'<a href="{repo_url}" target="_blank" rel="noopener">Code</a> | <a href="{docs_url}" target="_blank" rel="noopener">Docs</a>'
        elif repo_url:
            links = f'<a href="{repo_url}" target="_blank" rel="noopener">Code</a>'
        else:
            links = '—'

        stars = plugin['stars']

        # Main row
        markdown.append(
            f'<tr class="plugin-registry-row plugin-registry-row--main" data-plugin-row-id="{row_id}" data-entry-point-types="{normalized_types}" data-owner="{safe_owner}" data-owner-group="{owner_group}" data-plugin-name="{safe_name}" data-stars="{stars}">'
        )
        markdown.append(
            f'<td><strong>{name} </strong>(⭐ {stars})<br><small>{types}</small></td>'
        )
        markdown.append(f'<td>{description}</td>')
        markdown.append(f'<td><small>{deployment_text}</small></td>')
        markdown.append(f'<td>{links}</td>')
        markdown.append('</tr>')

        # Detailed information in dropdown
        markdown.append(
            f'<tr class="plugin-registry-row plugin-registry-row--details" data-plugin-row-id="{row_id}">'
        )
        markdown.append('<td colspan="4" style="padding: 0; border-top: none;">')
        markdown.append('<details style="margin: 0; padding: 12px 16px; border: 0px">')
        markdown.append(
            '<summary style="cursor: pointer; font-weight: 600; color: #1976d2; list-style: none; user-select: none;">View Details</summary>'
        )
        markdown.append('<div style="margin-top: 12px; padding-top: 12px;">')
        markdown.append('<p>')

        # Owner
        markdown.append(f"<strong>Owner:</strong> {plugin['owner']}<br>")

        # Authors
        if plugin['authors']:
            authors_str = ', '.join(plugin['authors'])
            markdown.append(f'<strong>Authors:</strong> {authors_str}<br>')

        # Maintainers
        if plugin['maintainers']:
            maintainers_str = ', '.join(plugin['maintainers'])
            markdown.append(f'<strong>Maintainers:</strong> {maintainers_str}<br>')

        # Entry points
        if plugin['entry_point_names']:
            entry_points_str = ', '.join(
                f'<code>{ep}</code>' for ep in plugin['entry_point_names']
            )
            markdown.append(f'<strong>Entry Points:</strong> {entry_points_str}<br>')

        # Plugin dependencies
        if plugin['plugin_dependencies']:
            deps_str = ', '.join(
                f'<code>{dep}</code>' for dep in plugin['plugin_dependencies']
            )
            markdown.append(f'<strong>Plugin Dependencies:</strong> {deps_str}<br>')

        # Dates
        created = format_date(plugin['created'])
        updated = format_date(plugin['last_updated'])
        markdown.append(
            f'<strong>Created:</strong> {created} | <strong>Last Updated:</strong> {updated}'
        )

        markdown.append('</p>')
        markdown.append('</div>')
        markdown.append('</details>')
        markdown.append('</td>')
        markdown.append('</tr>')

    markdown.append('</tbody>')
    markdown.append('</table>')

    return '\n'.join(markdown)


def generate_detailed_list(plugins: list[dict[str, Any]]) -> str:
    """
    Generate detailed list view of plugins with all metadata.

    Args:
        plugins: List of plugin metadata dictionaries

    Returns:
        Markdown formatted detailed list
    """
    if not plugins:
        return 'No plugins found.\n'

    # Sort plugins by name
    plugins_sorted = sorted(plugins, key=lambda x: x['name'].lower())

    markdown = []

    for plugin in plugins_sorted:
        markdown.append(f"\n### {plugin['name']}")
        markdown.append('')

        if plugin['description']:
            markdown.append(plugin['description'])
            markdown.append('')

        # Repository and metadata
        if plugin['repository']:
            markdown.append(
                f"**Repository:** [{plugin['repository']}]({plugin['repository']})"
            )

        markdown.append(f"**Owner:** {plugin['owner']}")
        markdown.append(f"**Stars:** {plugin['stars']}")
        markdown.append(f"**Created:** {format_date(plugin['created'])}")
        markdown.append(f"**Last Updated:** {format_date(plugin['last_updated'])}")
        markdown.append('')

        # Deployment status
        deployments = []
        if plugin['on_pypi']:
            deployments.append('PyPI')
        if plugin['on_central']:
            deployments.append('NOMAD Central')
        if plugin['on_example_oasis']:
            deployments.append('Example Oasis')

        if deployments:
            markdown.append(f"**Available on:** {', '.join(deployments)}")
            markdown.append('')

        # Entry points
        if plugin['entry_point_types']:
            markdown.append(
                f"**Plugin Types:** {', '.join(plugin['entry_point_types'])}"
            )
            markdown.append('')

        if plugin['entry_point_names']:
            markdown.append('**Entry Points:**')
            for ep_name in plugin['entry_point_names']:
                markdown.append(f'- `{ep_name}`')
            markdown.append('')

        # Authors and maintainers
        if plugin['authors']:
            authors_str = ', '.join(plugin['authors'])
            markdown.append(f'**Authors:** {authors_str}')
            markdown.append('')

        if plugin['maintainers']:
            maintainers_str = ', '.join(plugin['maintainers'])
            markdown.append(f'**Maintainers:** {maintainers_str}')
            markdown.append('')

        # Dependencies
        if plugin['plugin_dependencies']:
            markdown.append('**Plugin Dependencies:**')
            for dep in plugin['plugin_dependencies']:
                markdown.append(f'- {dep}')
            markdown.append('')

        markdown.append('---')

    return '\n'.join(markdown)


def generate_registry_page(plugins: list[dict[str, Any]], output_path: Path) -> None:
    """
    Generate the complete plugin registry markdown page.

    Args:
        plugins: List of plugin metadata dictionaries
        output_path: Path to write the markdown file
    """
    plugin_metadata = [extract_plugin_metadata(p) for p in plugins]

    # Build the page
    page_content = []
    page_content.append('# NOMAD Plugin Registry')
    page_content.append('')
    page_content.append(
        "This page contains information about all plugin entries currently listed in NOMAD. "
        "The information is automatically updated monthly. "
        f"**Last Updated:** {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}"
    )
    page_content.append('')
    page_content.append(
        '[Browse All Plugins in the NOMAD Plugins App](https://nomad-lab.eu/prod/v1/oasis/gui/search/plugins){ .md-button .nomad-button }'
    )
    page_content.append('')

    # Quick reference table
    page_content.append('## Available Plugins')
    page_content.append('')
    page_content.append('Quick reference table of all available plugins:')
    page_content.append('')
    page_content.append(generate_markdown_table(plugin_metadata))
    page_content.append('')

    # Write to file
    output_path.parent.mkdir(parents=True, exist_ok=True)
    content = '\n'.join(page_content)

    # Fix external links to include target and rel attributes
    content = fix_external_links(content)

    # Fix markdownlint issues
    content = fix_markdown_lint_issues(content)

    output_path.write_text(content, encoding='utf-8')
    print(f'Plugin registry written to {output_path}')


def main():
    """Main entry point."""
    # Determine output path
    script_dir = Path(__file__).parent
    docs_dir = script_dir.parent / 'docs' / 'examples'
    output_path = docs_dir / 'plugin_registry.md'

    # Query all plugins
    all_plugins = query_plugins()

    if not all_plugins:
        print('Warning: No plugins found!')
        # Still generate the page with a message
        output_path.write_text(
            "# NOMAD Plugin Registry\n\n"
            "No plugins found.\n\n"
            f"Last checked: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}\n",
            encoding='utf-8',
        )
        return

    # Remove duplicates based on plugin name (in case same plugin appears in multiple orgs)
    seen_names = set()
    unique_plugins = []
    for plugin in all_plugins:
        plugin_name = plugin.get('data', {}).get('name', '')
        if plugin_name and plugin_name not in seen_names:
            seen_names.add(plugin_name)
            unique_plugins.append(plugin)

    # Generate the registry page
    generate_registry_page(unique_plugins, output_path)

    print(
        f'Successfully generated plugin registry with {len(unique_plugins)} plugins (from {len(all_plugins)} total entries)'
    )


if __name__ == '__main__':
    main()
