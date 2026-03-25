"""
Make sure all external links in markdown have `{:target="_blank" rel="noopener"}`,
and internal links don't have them.
"""

import sys
from pathlib import Path

import regex

# Match [text](http/https...) or [text](/internal...) with optional {attrs}
# Group 1 = the markdown link [text](url)
# Group 2 = the url itself
# Group 3 = the optional attrs block, including any leading spaces
LINK_PATTERN = regex.compile(
    r"""
    (                               # Group 1: full link including [text](url)
      \[[^\]]+\]                    # [text]
      \(                            # opening paren of URL
        (                           # Group 2: the url inside the parens
          (?:[^()\s]+|              # non-parens
             \((?:[^()]+|(?2))*\)   # balanced (...) recursing group 2
          )*
        )
      \)                            # closing paren of Markdown link
    )
    ([ \t]*\{[^\}]*\})?             # Group 3: optional space + attrs
    """,
    regex.VERBOSE,
)


def normalize_attrs(attrs: str | None, is_external: bool) -> str:
    """Ensure target and rel are correctly applied or removed."""
    if not attrs:
        if is_external:
            return '{:target="_blank" rel="noopener"}'
        return ""

    inner: str = attrs.strip()[1:-1].strip()  # remove { }

    # Strip optional leading colon commonly used in MkDocs/Markdown attributes
    if inner.startswith(":"):
        inner = inner[1:].strip()

    parts: list[str] = inner.split()
    attrs_dict: dict[str, str | None] = {}

    for part in parts:
        if "=" in part:
            k, v = part.split("=", 1)
            attrs_dict[k] = v.strip("\"'")
        else:
            attrs_dict[part] = None

    if is_external:
        attrs_dict["target"] = "_blank"
        attrs_dict["rel"] = "noopener"
    else:
        attrs_dict.pop("target", None)
        attrs_dict.pop("rel", None)

    if not attrs_dict:
        return ""

    res_parts: list[str] = []
    for k, v in attrs_dict.items():
        if v is not None:
            res_parts.append(f'{k}="{v}"')
        else:
            res_parts.append(k)

    return "{:" + " ".join(res_parts) + "}"


def process_file(path: Path) -> int:
    """Process one file. Return number of actual changes."""
    text: str = path.read_text(encoding="utf-8")
    changes_in_file = 0

    def repl(match: regex.Match) -> str:
        nonlocal changes_in_file
        original = match.group(0)
        full_link = match.group(1)
        url = match.group(2)
        attrs = match.group(3)

        if attrs is not None:
            attrs = attrs.lstrip()

        is_external = url.startswith(("http://", "https://", "ftp://"))
        new_attrs = normalize_attrs(attrs, is_external)

        replacement = full_link + new_attrs
        if replacement != original:
            changes_in_file += 1

        return replacement

    new_text = LINK_PATTERN.sub(repl, text)

    if changes_in_file > 0:
        print(f"Updated {changes_in_file} link(s) in {path}")
        path.write_text(new_text, encoding="utf-8")

    return changes_in_file


def main(root: str = "docs") -> int:
    """Process all markdown files under the given root directory."""
    total_changes = 0
    for md_file in Path(root).rglob("*.md"):
        total_changes += process_file(md_file)
    return total_changes


if __name__ == "__main__":
    changes = main()
    if changes > 0:
        print(f"\n✗ Found and fixed {changes} issues.")
        sys.exit(1)

    print("\n✓ All links are correctly annotated.")
    sys.exit(0)
