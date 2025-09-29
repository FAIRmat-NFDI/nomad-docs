"""
Make sure all external links in markdown have `{:target="_blank" rel="noopener"}`.
"""

import sys
from pathlib import Path

import regex

# Match [text](http/https...) with optional {attrs}
# Handles links with balanced parentheses in the URL
# Group 1 = the markdown link (text + url)
# Group 2 = the optional {attrs}
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


def normalize_attrs(attrs: str | None) -> str:
    """Ensure target and rel are both present."""
    if not attrs:
        return '{:target="_blank" rel="noopener"}'

    inner: str = attrs.strip()[1:-1].strip()  # remove { }
    parts: list[str] = inner.split()
    attrs_dict: dict[str, str | None] = {}

    for part in parts:
        if "=" in part:
            k, v = part.split("=", 1)
            attrs_dict[k.strip(":")] = v.strip('"')
        else:
            attrs_dict[part.strip(":")] = None

    # Always enforce target and rel
    attrs_dict["target"] = "_blank"
    attrs_dict["rel"] = "noopener"

    return (
        "{:" + " ".join(f'{k}="{v}"' if v else k for k, v in attrs_dict.items()) + "}"
    )


def process_file(path: Path) -> int:
    """Process one file. Return number of changes."""
    text: str = path.read_text(encoding="utf-8")

    def repl(match: regex.Match) -> str:
        link, attrs = match.groups()
        return link + normalize_attrs(attrs)

    new_text, count = LINK_PATTERN.subn(repl, text)

    if count > 0 and new_text != text:
        print(f"Updated {count} link(s) in {path}")
        path.write_text(new_text, encoding="utf-8")
        return count
    return 0


def main(root="docs") -> int:
    total_changes = 0
    for md_file in Path(root).rglob("*.md"):
        total_changes += process_file(md_file)
    return total_changes


if __name__ == "__main__":
    changes = main()
    if changes > 0:
        print(f"\n✗ Found and fixed {changes} issues.")
        sys.exit(1)
    else:
        print("\n✓ All external links are correctly annotated.")
        sys.exit(0)
