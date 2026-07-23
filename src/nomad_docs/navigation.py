"""Navigation helpers for documentation macros.

This module provides the ``nav_link`` and ``nav_list`` macros used on overview
pages. They resolve links, labels, breadcrumbs, list membership, and list order
through ``mkdocs.yml`` instead of duplicating navigation structure in Markdown.
The navigation index rejects entries without explicit titles, detects duplicate
page paths, and can preserve manually authored per-page descriptions.
"""

from __future__ import annotations

import posixpath
from collections.abc import Mapping, Sequence
from dataclasses import dataclass, field
from typing import Any
from urllib.parse import urlsplit


class NavigationError(ValueError):
    """Raised when the configured navigation cannot resolve a documentation page."""


@dataclass
class NavigationNode:
    """A section or page in the MkDocs navigation tree."""

    title: str
    source_path: str | None = None
    children: list["NavigationNode"] = field(default_factory=list)
    parent: "NavigationNode | None" = None

    @property
    def is_page(self) -> bool:
        return self.source_path is not None


class NavigationIndex:
    """Index page titles and breadcrumbs from ``mkdocs.yml`` navigation."""

    def __init__(self, nav: object):
        self._root = NavigationNode("root")
        self._titles: dict[str, str] = {}
        self._breadcrumbs: dict[str, tuple[str, ...]] = {}
        self._pages: dict[str, NavigationNode] = {}
        self._visit_root(nav)

    def title_for(self, source_path: str) -> str:
        """Return the configured navigation title for a documentation source path."""

        normalized_path = _normalize_source_path(source_path, "Navigation target")
        try:
            return self._titles[normalized_path]
        except KeyError as exc:
            raise NavigationError(
                f"Documentation page '{normalized_path}' is not present in mkdocs.yml nav."
            ) from exc

    def label_for(self, source_path: str) -> str:
        """Return a full or abbreviated navigation breadcrumb for a page."""

        normalized_path = _normalize_source_path(source_path, "Navigation target")
        try:
            breadcrumb = self._breadcrumbs[normalized_path]
        except KeyError as exc:
            raise NavigationError(
                f"Documentation page '{normalized_path}' is not present in mkdocs.yml nav."
            ) from exc

        intermediate_sections = breadcrumb[1:-1]
        if len(intermediate_sections) > 1:
            return " > ".join((breadcrumb[0], "...", breadcrumb[-1]))
        return " > ".join(breadcrumb)

    def link(
        self,
        source_path: str,
        current_source_path: str | None,
        breadcrumb: bool = False,
    ) -> str:
        """Render a Markdown link to a navigation page from the current page."""

        normalized_target = _normalize_source_path(source_path, "Navigation target")
        normalized_current = _normalize_source_path(
            current_source_path, "Current page source URI"
        )
        label = (
            self.label_for(normalized_target)
            if breadcrumb
            else self.title_for(normalized_target)
        )
        current_directory = posixpath.dirname(normalized_current) or "."
        relative_target = posixpath.relpath(
            normalized_target, start=current_directory
        )
        markdown_target = (
            f"<{relative_target}>"
            if any(character in relative_target for character in " ()")
            else relative_target
        )
        return f"[{_escape_markdown_label(label)}]({markdown_target})"

    def list(
        self,
        target: str | None,
        current_source_path: str | None,
        descriptions: Mapping[str, str] | None = None,
    ) -> str:
        """Render a Markdown list from a navigation section or page.

        If ``target`` is omitted, the current page's navigation section is
        rendered. If ``target`` is a Markdown path, a single page is rendered.
        Otherwise, ``target`` must match one direct child section of the current
        navigation section.
        """

        normalized_current = _normalize_source_path(
            current_source_path, "Current page source URI"
        )
        current_node = self._page_for(normalized_current)
        current_section = current_node.parent
        if current_section is None:
            raise NavigationError(
                f"Documentation page '{normalized_current}' has no navigation section."
            )

        if target is None:
            target_node = current_section
        elif isinstance(target, str) and _is_document_path(target):
            target_node = self._page_for(target)
        elif isinstance(target, str):
            target_node = self._find_child_section(current_section, target)
        else:
            raise NavigationError(
                "Navigation list target must be a section title or Markdown path."
            )

        normalized_descriptions = self._normalize_descriptions(descriptions)
        excluded_path = normalized_current if target_node is current_section else None
        rendered_paths = set(self._descendant_page_paths(target_node, excluded_path))
        unknown_descriptions = sorted(normalized_descriptions.keys() - rendered_paths)
        if unknown_descriptions:
            raise NavigationError(
                "Navigation descriptions include pages outside the rendered list: "
                + ", ".join(unknown_descriptions)
            )

        lines = self._render_list_node(
            target_node,
            normalized_current,
            normalized_descriptions,
            excluded_path=excluded_path,
            render_section_title=False,
        )
        if not lines:
            target_label = "current section" if target is None else repr(target)
            raise NavigationError(f"Navigation list for {target_label} is empty.")
        return "\n".join(lines)

    def _visit_root(self, nav: object) -> None:
        if not _is_sequence(nav):
            raise NavigationError("mkdocs.yml nav must be a list of navigation items.")
        self._visit_items(nav, self._root, ())

    def _visit_items(
        self,
        items: Sequence[object],
        parent: NavigationNode,
        parent_titles: tuple[str, ...],
    ) -> None:
        for item in items:
            if isinstance(item, str):
                if _is_document_path(item):
                    normalized_path = _normalize_source_path(
                        item, "Navigation source path"
                    )
                    raise NavigationError(
                        f"Navigation page '{normalized_path}' has no explicit title. "
                        "Use 'Title: path.md' in mkdocs.yml."
                    )
                continue

            if not isinstance(item, Mapping):
                raise NavigationError(
                    "mkdocs.yml nav items must be page paths or title mappings."
                )

            for title, target in item.items():
                if not isinstance(title, str) or not title.strip():
                    raise NavigationError("Navigation titles must be non-empty strings.")
                normalized_title = title.strip()

                if _is_sequence(target):
                    section = NavigationNode(normalized_title, parent=parent)
                    parent.children.append(section)
                    self._visit_items(
                        target, section, (*parent_titles, normalized_title)
                    )
                elif isinstance(target, str):
                    if _is_document_path(target):
                        self._add_page(
                            normalized_title, target, parent, parent_titles
                        )
                else:
                    raise NavigationError(
                        f"Navigation item '{title}' must point to a page or subsection."
                    )

    def _add_page(
        self,
        title: str,
        source_path: str,
        parent: NavigationNode,
        parent_titles: tuple[str, ...],
    ) -> None:
        normalized_path = _normalize_source_path(
            source_path, "Navigation source path"
        )
        if normalized_path in self._titles:
            raise NavigationError(
                f"Documentation page '{normalized_path}' occurs more than once "
                "in mkdocs.yml nav."
            )
        self._titles[normalized_path] = title
        self._breadcrumbs[normalized_path] = (*parent_titles, title)
        node = NavigationNode(title, source_path=normalized_path, parent=parent)
        parent.children.append(node)
        self._pages[normalized_path] = node

    def _page_for(self, source_path: str) -> NavigationNode:
        normalized_path = _normalize_source_path(source_path, "Navigation target")
        try:
            return self._pages[normalized_path]
        except KeyError as exc:
            raise NavigationError(
                f"Documentation page '{normalized_path}' is not present in mkdocs.yml nav."
            ) from exc

    def _find_child_section(
        self, section: NavigationNode, title: str
    ) -> NavigationNode:
        if not isinstance(title, str) or not title.strip():
            raise NavigationError("Navigation section target must be a non-empty string.")

        normalized_title = title.strip()
        matches = [
            child
            for child in section.children
            if not child.is_page and child.title == normalized_title
        ]
        if not matches:
            raise NavigationError(
                f"Navigation section '{normalized_title}' is not a child of "
                f"'{section.title}'."
            )
        if len(matches) > 1:
            raise NavigationError(
                f"Navigation section '{normalized_title}' is ambiguous under "
                f"'{section.title}'."
            )
        return matches[0]

    def _normalize_descriptions(
        self, descriptions: Mapping[str, str] | None
    ) -> dict[str, str]:
        if descriptions is None:
            return {}
        if not isinstance(descriptions, Mapping):
            raise NavigationError("Navigation descriptions must be a mapping.")

        normalized_descriptions: dict[str, str] = {}
        for source_path, description in descriptions.items():
            normalized_path = _normalize_source_path(
                source_path, "Navigation description path"
            )
            self._page_for(normalized_path)
            if not isinstance(description, str) or not description.strip():
                raise NavigationError(
                    f"Navigation description for '{normalized_path}' "
                    "must be a non-empty string."
                )
            normalized_descriptions[normalized_path] = description.strip()
        return normalized_descriptions

    def _descendant_page_paths(
        self, node: NavigationNode, excluded_path: str | None
    ) -> list[str]:
        if node.is_page:
            assert node.source_path is not None
            return [] if node.source_path == excluded_path else [node.source_path]

        paths: list[str] = []
        for child in node.children:
            paths.extend(self._descendant_page_paths(child, excluded_path))
        return paths

    def _render_list_node(
        self,
        node: NavigationNode,
        current_source_path: str,
        descriptions: Mapping[str, str],
        excluded_path: str | None,
        render_section_title: bool,
        depth: int = 0,
    ) -> list[str]:
        if node.is_page:
            assert node.source_path is not None
            if node.source_path == excluded_path:
                return []
            link = self.link(node.source_path, current_source_path)
            description = descriptions.get(node.source_path)
            suffix = f": {description}" if description else ""
            return [f"{'    ' * depth}- {link}{suffix}"]

        lines: list[str] = []
        if render_section_title:
            lines.append(
                f"{'    ' * depth}- **{_escape_markdown_label(node.title)}**"
            )
            child_depth = depth + 1
        else:
            child_depth = depth

        for child in node.children:
            lines.extend(
                self._render_list_node(
                    child,
                    current_source_path,
                    descriptions,
                    excluded_path,
                    render_section_title=True,
                    depth=child_depth,
                )
            )
        return lines


def register_nav_link(env: Any) -> None:
    """Register navigation macros in a MkDocs Macros environment."""

    navigation = NavigationIndex(env.conf.get("nav"))

    @env.macro
    def nav_link(source_path: str, breadcrumb: bool = False) -> str:
        """Render a link whose title and target come from ``mkdocs.yml``."""

        try:
            current_source_path = env.page.file.src_uri
        except AttributeError as exc:
            raise NavigationError(
                "The nav_link macro requires the current page file.src_uri."
            ) from exc
        return navigation.link(
            source_path, current_source_path, breadcrumb=breadcrumb
        )

    @env.macro
    def nav_list(
        target: str | None = None, descriptions: Mapping[str, str] | None = None
    ) -> str:
        """Render a nav-ordered Markdown list for a page or subsection."""

        try:
            current_source_path = env.page.file.src_uri
        except AttributeError as exc:
            raise NavigationError(
                "The nav_list macro requires the current page file.src_uri."
            ) from exc
        return navigation.list(target, current_source_path, descriptions=descriptions)


def _normalize_source_path(source_path: str | None, description: str) -> str:
    if not isinstance(source_path, str) or not source_path.strip():
        raise NavigationError(f"{description} must be a non-empty string.")

    path = source_path.strip().replace("\\", "/")
    parsed = urlsplit(path)
    if parsed.scheme or parsed.netloc or parsed.query or parsed.fragment:
        raise NavigationError(
            f"{description} '{source_path}' must be a documentation source path."
        )

    normalized_path = posixpath.normpath(parsed.path)
    if (
        normalized_path in {"", ".", ".."}
        or posixpath.isabs(normalized_path)
        or normalized_path.startswith("../")
        or not normalized_path.endswith(".md")
    ):
        raise NavigationError(
            f"{description} '{source_path}' must be a relative Markdown path."
        )
    return normalized_path


def _is_document_path(target: str) -> bool:
    parsed = urlsplit(target.replace("\\", "/"))
    return (
        not parsed.scheme
        and not parsed.netloc
        and not parsed.query
        and not parsed.fragment
        and parsed.path.endswith(".md")
    )


def _is_sequence(value: object) -> bool:
    return isinstance(value, Sequence) and not isinstance(value, (str, bytes))


def _escape_markdown_label(label: str) -> str:
    return label.replace("\\", "\\\\").replace("[", "\\[").replace("]", "\\]")
