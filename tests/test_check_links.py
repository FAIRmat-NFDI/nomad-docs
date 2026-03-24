import textwrap
from pathlib import Path

import nomad_docs.check_links as check_links
from nomad_docs.check_links import main


def test_process_file_adds_attrs(tmp_path: Path) -> None:
    """External links should gain target/rel, while internal links should lose them."""
    mdfile = tmp_path / "example.md"
    mdfile.write_text(
        textwrap.dedent(
            """
            External without attrs: [Google](https://google.com)
            External without attrs (http): [Example](http://example.org)
            External partial attrs: [YouTube](https://youtube.com){:target="_blank"}
            External full attrs: [Docs](https://example.com){:target="_blank" rel="noopener"}
            Internal link: [Overview](./overview.md)
            Internal link bad attrs: [Bad](./bad.md){:target="_blank" rel="noopener"}
            Internal link mixed attrs: [Mixed](./mixed.md){:.my-class target="_blank"}
            Link with parentheses: [Wiki](https://en.wikipedia.org/wiki/Reentrancy_(computing))
            Link with classes: [nomad-neb-workflows Plugin Documentation](https://fairmat-nfdi.github.io/nomad-neb-workflows/index.html){ .md-button .nomad-button target="_blank" rel="noopener" }
            """
        ).lstrip(),
        encoding="utf-8",
    )

    changes = check_links.process_file(mdfile)

    assert changes > 0

    lines = mdfile.read_text(encoding="utf-8").splitlines()

    assert (
        lines[0]
        == 'External without attrs: [Google](https://google.com){:target="_blank" rel="noopener"}'
    )
    assert (
        lines[1]
        == 'External without attrs (http): [Example](http://example.org){:target="_blank" rel="noopener"}'
    )
    assert (
        lines[2]
        == 'External partial attrs: [YouTube](https://youtube.com){:target="_blank" rel="noopener"}'
    )
    assert (
        lines[3]
        == 'External full attrs: [Docs](https://example.com){:target="_blank" rel="noopener"}'
    )
    assert lines[4] == "Internal link: [Overview](./overview.md)"
    assert lines[5] == "Internal link bad attrs: [Bad](./bad.md)"
    assert lines[6] == "Internal link mixed attrs: [Mixed](./mixed.md){:.my-class}"
    assert (
        lines[7]
        == 'Link with parentheses: [Wiki](https://en.wikipedia.org/wiki/Reentrancy_(computing)){:target="_blank" rel="noopener"}'
    )
    assert (
        lines[8]
        == 'Link with classes: [nomad-neb-workflows Plugin Documentation](https://fairmat-nfdi.github.io/nomad-neb-workflows/index.html){:.md-button .nomad-button target="_blank" rel="noopener"}'
    )


def test_process_file_preserves_plain_space_after_internal_link(tmp_path: Path) -> None:
    """A normal prose space after an internal link must not be swallowed."""
    mdfile = tmp_path / "spacing.md"
    original = "Text before [Parser](../../reference/glossary.md#parser) code after.\n"
    mdfile.write_text(original, encoding="utf-8")

    changes = check_links.process_file(mdfile)

    assert changes == 0
    assert mdfile.read_text(encoding="utf-8") == original


def test_process_file_normalizes_attr_block_style(tmp_path: Path) -> None:
    """Attribute blocks may be normalized to the canonical `{:...}` form."""
    mdfile = tmp_path / "images.md"
    mdfile.write_text(
        textwrap.dedent(
            """
            ![Overview page](images/overview_page.png){.screenshot}
            ![Data page](images/data_page.png){.screenshot}
            """
        ).lstrip(),
        encoding="utf-8",
    )

    changes = check_links.process_file(mdfile)

    assert changes == 2

    lines = mdfile.read_text(encoding="utf-8").splitlines()
    assert lines[0] == "![Overview page](images/overview_page.png){:.screenshot}"
    assert lines[1] == "![Data page](images/data_page.png){:.screenshot}"


def test_docs_external_links_clean() -> None:
    """Ensure docs links are already correctly annotated or cleaned."""
    docs = Path(__file__).resolve().parent.parent / "docs"
    docs.mkdir(parents=True, exist_ok=True)

    changes = main(str(docs))
    assert changes == 0, (
        "docs contain incorrectly annotated links. Please run check_links.py to fix them."
    )
