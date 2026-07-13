from types import SimpleNamespace

import pytest

from nomad_docs.navigation import NavigationError, NavigationIndex, register_nav_link


NAV = [
    {"Home": "index.md"},
    {
        "Tutorials": [
            {"Overview": "tutorial/overview.md"},
            {
                "Upload data": [
                    {"With the GUI": "tutorial/upload.md"},
                ]
            },
            {
                "Develop plugins": [
                    {
                        "Create a parser": [
                            {"Parser tutorial": "tutorial/parser.md"},
                        ]
                    }
                ]
            },
        ]
    },
    {"Reference": [{"Array [data]": "reference/index.md"}]},
    {"Project": "https://example.com"},
]


def test_navigation_index_extracts_titles_from_nested_navigation():
    navigation = NavigationIndex(NAV)

    assert navigation.title_for("tutorial/upload.md") == "With the GUI"
    assert navigation.title_for(r"reference\index.md") == "Array [data]"


@pytest.mark.parametrize(
    ("target", "expected"),
    [
        ("index.md", "Home"),
        ("tutorial/overview.md", "Tutorials > Overview"),
        ("tutorial/upload.md", "Tutorials > Upload data > With the GUI"),
        ("tutorial/parser.md", "Tutorials > ... > Parser tutorial"),
    ],
)
def test_navigation_index_formats_navigation_breadcrumbs(target, expected):
    navigation = NavigationIndex(NAV)

    assert navigation.label_for(target) == expected


@pytest.mark.parametrize(
    ("target", "current", "expected"),
    [
        ("tutorial/overview.md", "index.md", "[Overview](tutorial/overview.md)"),
        (
            "reference/index.md",
            "tutorial/overview.md",
            r"[Array \[data\]](../reference/index.md)",
        ),
        (
            r"tutorial\upload.md",
            r"reference\index.md",
            "[With the GUI](../tutorial/upload.md)",
        ),
    ],
)
def test_navigation_index_renders_relative_posix_links(target, current, expected):
    navigation = NavigationIndex(NAV)

    assert navigation.link(target, current) == expected


@pytest.mark.parametrize(
    ("target", "expected"),
    [
        ("tutorial/overview.md", "[Tutorials > Overview](tutorial/overview.md)"),
        (
            "tutorial/upload.md",
            "[Tutorials > Upload data > With the GUI](tutorial/upload.md)",
        ),
        (
            "tutorial/parser.md",
            "[Tutorials > ... > Parser tutorial](tutorial/parser.md)",
        ),
    ],
)
def test_navigation_index_renders_breadcrumb_links(target, expected):
    navigation = NavigationIndex(NAV)

    assert navigation.link(target, "index.md", breadcrumb=True) == expected


def test_navigation_index_wraps_markdown_targets_containing_spaces():
    navigation = NavigationIndex([{"Page": "topic/page name.md"}])

    assert navigation.link("topic/page name.md", "index.md") == (
        "[Page](<topic/page name.md>)"
    )


def test_navigation_index_rejects_duplicate_source_paths():
    with pytest.raises(NavigationError, match="occurs more than once"):
        NavigationIndex(
            [
                {"First": "topic/page.md"},
                {"Second": r"topic\page.md"},
            ]
        )


def test_navigation_index_rejects_pages_without_explicit_titles():
    with pytest.raises(NavigationError, match="has no explicit title"):
        NavigationIndex(["topic/page.md"])


def test_navigation_index_rejects_missing_target():
    navigation = NavigationIndex(NAV)

    with pytest.raises(NavigationError, match="is not present"):
        navigation.link("tutorial/missing.md", "index.md")


@pytest.mark.parametrize("current", [None, "", "../outside.md", "/absolute.md"])
def test_navigation_index_rejects_invalid_current_page(current):
    navigation = NavigationIndex(NAV)

    with pytest.raises(NavigationError, match="Current page source URI"):
        navigation.link("index.md", current)


class MacroEnvironment:
    def __init__(self, src_uri="tutorial/overview.md"):
        self.conf = {"nav": NAV}
        self.page = SimpleNamespace(file=SimpleNamespace(src_uri=src_uri))
        self.macros = {}

    def macro(self, function):
        self.macros[function.__name__] = function
        return function


def test_register_nav_link_uses_the_current_page_source_uri():
    env = MacroEnvironment()
    register_nav_link(env)

    assert env.macros["nav_link"]("reference/index.md") == (
        r"[Array \[data\]](../reference/index.md)"
    )
    assert env.macros["nav_link"]("reference/index.md", breadcrumb=True) == (
        r"[Reference > Array \[data\]](../reference/index.md)"
    )


def test_register_nav_link_requires_the_current_page_source_uri():
    env = MacroEnvironment()
    env.page = SimpleNamespace(file=SimpleNamespace())
    register_nav_link(env)

    with pytest.raises(NavigationError, match="requires the current page"):
        env.macros["nav_link"]("index.md")
