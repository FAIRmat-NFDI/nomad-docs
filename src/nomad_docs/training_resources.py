from __future__ import annotations

import html
import json
import re
from datetime import datetime, timezone
from typing import Any

_HTML_TAG_RE = re.compile(r"<[^>]+>")


def _strip_html(s: str) -> str:
    return _HTML_TAG_RE.sub("", s or "").replace("\n", " ").strip()


def _parse_dt(s: str | None) -> datetime:
    if not s:
        return datetime.min.replace(tzinfo=timezone.utc)
    t = s.strip()
    if t.endswith("Z"):
        t = t[:-1] + "+00:00"
    try:
        dt = datetime.fromisoformat(t)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt
    except Exception:
        return datetime.min.replace(tzinfo=timezone.utc)


def _pill(text: str) -> str:
    return f'<span class="tr-pill">{html.escape(text)}</span>'


def render_training_resources_table(
    full_json_path: str,
    preview_chars: int = 260,
) -> str:
    with open(full_json_path, "r", encoding="utf-8") as f:
        payload = json.load(f)

    items: list[dict[str, Any]] = payload.get("items", [])
    items = sorted(items, key=lambda it: _parse_dt(it.get("date_created")), reverse=True)

    out: list[str] = []
    out.append('<div class="training-resources-list">')

    for it in items:
        dt = _parse_dt(it.get("date_created"))
        date_txt = (
            dt.date().isoformat()
            if dt != datetime.min.replace(tzinfo=timezone.utc)
            else ""
        )

        title = (it.get("title") or "").strip()
        url = (it.get("identifier") or "").strip()

        full_desc = _strip_html(it.get("description") or "").strip()
        is_long = bool(preview_chars) and len(full_desc) > preview_chars

        subjects = it.get("subject") or []
        levels = it.get("educational_level") or []

        title_html = html.escape(title)
        if url:
            url_html = html.escape(url, quote=True)
            title_html = (
                f'<a href="{url_html}" target="_blank" rel="noopener">{title_html}</a>'
            )

        out.append('<div class="tr-item">')
        out.append(f'<div class="tr-date">{html.escape(date_txt)}</div>')
        out.append(f'<div class="tr-title">{title_html}</div>')

        if levels:
            out.append(
                '<div class="tr-meta-line tr-level">'
                '<span class="tr-meta-label">Level:</span>'
                '<span class="tr-pills">'
                + "".join(_pill(lv) for lv in levels if lv)
                + "</span></div>"
            )

        if subjects:
            out.append(
                '<div class="tr-meta-line tr-subjects">'
                '<span class="tr-meta-label">Subjects:</span>'
                '<span class="tr-pills">'
                + "".join(_pill(s) for s in subjects if s)
                + "</span></div>"
            )

        if full_desc:
            if is_long:
                out.append('<details class="tr-desc tr-desc-inline">')
                out.append(
                    f"<summary>"
                    f'<span class="tr-text">{html.escape(full_desc)}</span>'
                    f'<span class="tr-more tr-more-closed">…</span>'
                    f'<span class="tr-more tr-more-open">Show less</span>'
                    f"</summary>"
                )
                out.append("</details>")
            else:
                out.append(f'<div class="tr-desc-static">{html.escape(full_desc)}</div>')

        out.append("</div>")

    out.append("</div>")
    return "\n".join(out) + "\n"