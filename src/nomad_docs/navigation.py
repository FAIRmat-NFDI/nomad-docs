"""Navigation helpers for documentation macros.

This module provides the ``nav_link`` macro used on overview pages. It resolves
links through ``mkdocs.yml`` instead of duplicating titles in Markdown, rejects
navigation entries without explicit titles, detects duplicate page paths, and
can render breadcrumb labels for cross-section links.
"""

from __future__ import annotations

import posixpath
from collections.abc import Mapping, Sequence
from typing import Any
from urllib.parse import urlsplit


class NavigationError(ValueError):
    """Raised when the configured navigation cannot resolve a documentation page."""


class NavigationIndex:
    """Index page titles and breadcrumbs from ``mkdocs.yml`` navigation."""

    def __init__(self, nav: object):
        self._titles: dict[str, str] = {}
        self._breadcrumbs: dict[str, tuple[str, ...]] = {}
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

    def _visit_root(self, nav: object) -> None:
        if not _is_sequence(nav):
            raise NavigationError("mkdocs.yml nav must be a list of navigation items.")
        self._visit_items(nav, ())

    def _visit_items(
        self, items: Sequence[object], parent_titles: tuple[str, ...]
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
                    self._visit_items(target, (*parent_titles, normalized_title))
                elif isinstance(target, str):
                    if _is_document_path(target):
                        self._add_page(normalized_title, target, parent_titles)
                else:
                    raise NavigationError(
                        f"Navigation item '{title}' must point to a page or subsection."
                    )

    def _add_page(
        self,
        title: str,
        source_path: str,
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


def register_nav_link(env: Any) -> None:
    """Register the ``nav_link`` macro in a MkDocs Macros environment."""

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
