import textwrap
from pathlib import Path

import nomad_docs.check_links as check_links
from nomad_docs.check_links import main


def test_process_file_adds_attrs(tmp_path: Path):
    mdfile = tmp_path / "example.md"
    mdfile.write_text(
        textwrap.dedent("""
        External without attrs: [Google](https://google.com)
        External without attrs (http): [Example](http://example.org)
        External partial attrs: [YouTube](https://youtube.com){:target="_blank"}
        External full attrs: [Docs](https://example.com){:target="_blank" rel="noopener"}
        Internal link: [Overview](./overview.md)
        Link with parentheses: [Wiki](https://en.wikipedia.org/wiki/Reentrancy_(computing))
        Link with classes: [nomad-neb-workflows Plugin Documentation](https://fairmat-nfdi.github.io/nomad-neb-workflows/index.html){ .md-button .nomad-button target="_blank" rel="noopener" }
    """)
    )

    changes = check_links.process_file(mdfile)

    # It should report changes
    assert changes > 0

    lines = mdfile.read_text().splitlines()

    assert (
        lines[1]
        == 'External without attrs: [Google](https://google.com){:target="_blank" rel="noopener"}'
    )
    assert (
        lines[2]
        == 'External without attrs (http): [Example](http://example.org){:target="_blank" rel="noopener"}'
    )
    assert (
        lines[3]
        == 'External partial attrs: [YouTube](https://youtube.com){:target="_blank" rel="noopener"}'
    )
    assert (
        lines[4]
        == 'External full attrs: [Docs](https://example.com){:target="_blank" rel="noopener"}'
    )
    assert lines[5] == "Internal link: [Overview](./overview.md)"
    assert (
        lines[6]
        == 'Link with parentheses: [Wiki](https://en.wikipedia.org/wiki/Reentrancy_(computing)){:target="_blank" rel="noopener"}'
    )
    assert (
        lines[7]
        == 'Link with classes: [nomad-neb-workflows Plugin Documentation](https://fairmat-nfdi.github.io/nomad-neb-workflows/index.html){:.md-button .nomad-button target="_blank" rel="noopener"}'
    )


def test_docs_external_links_clean():
    """Ensure external links have target and rel attributes."""
    docs = Path(__file__).resolve().parent.parent / "docs"
    changes = main(str(docs))
    assert changes == 0, 'docs contain external links without target/rel attributes. you should append `{:target="_blank" rel="noopener"}` to each external link.'
