#
# Copyright The NOMAD Authors.
#
# This file is part of NOMAD. See https://nomad-lab.eu for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""
Definitions that are used in the documentation via mkdocs-macro-plugin.
"""

from pydantic.fields import FieldInfo
import yaml
import json
import os.path

from typing import get_args, cast

from inspect import isclass

from pydantic.fields import FieldInfo

from pydantic import BaseModel

from markdown.extensions.toc import slugify

from nomad.utils import strip
from nomad.config import config
from nomad import utils

from nomad_docs.pydantic import (
    exported_config_models,
    get_field_default,
    get_field_deprecated,
    get_field_description,
    get_field_options,
    get_field_type_info,
)
from nomad_docs.metainfo import (
    package_markdown_from_package,
)

from nomad.config.models.plugins import ParserEntryPoint, EntryPointType


class MyYamlDumper(yaml.Dumper):
    """
    A custom dumper that always shows objects in yaml and not json syntax
    even with default_flow_style=None.
    """

    def represent_mapping(self, *args, **kwargs):
        node = super().represent_mapping(*args, **kwargs)
        node.flow_style = False
        return node


def define_env(env):
    @env.macro
    def nomad_url():  # pylint: disable=unused-variable
        return config.api_url()

    @env.macro
    def doc_snippet(key):  # pylint: disable=unused-variable
        from nomad.app.v1.models import query_documentation, owner_documentation
        from nomad.app.v1.routers.entries import archive_required_documentation

        doc_snippets = {
            "query": query_documentation,
            "owner": owner_documentation,
            "archive-required": archive_required_documentation,
        }
        return doc_snippets[key]

    @env.macro
    def metainfo_data():  # pylint: disable=unused-variable
        return utils.strip(
            """
            You can browse the [NOMAD metainfo schema](https://nomad-lab.eu/prod/v1/gui/analyze/metainfo)
            or the archive of each entry (e.g. [a VASP example](https://nomad-lab.eu/prod/v1/gui/search/entries/entry/id/mIyITulZli0FPSoAB3OKt3WrsMTq))
            in the web-interface."""
        )

    @env.macro
    def file_contents(path):  # pylint: disable=unused-variable
        with open(path) as f:
            return f.read()

    @env.macro
    def yaml_snippet(path, indent, filter=None):  # pylint: disable=unused-variable
        """
        Produces a yaml string from a (partial) .json or .yaml file.

        Arguments:
            path: The path to the file relative to project root.
            indent: Additional indentation that is added to each line of the result string.
            filter:
                Optional comma separated list of keys that should be removed from
                the top-level object.
        """

        if ":" not in path:
            path = f"{path}:"

        file_path, json_path = path.split(":")
        file_path = os.path.join(os.path.dirname(__file__), "../..", file_path)

        with open(file_path) as f:
            if file_path.endswith(".yaml"):
                data = yaml.load(f, Loader=yaml.SafeLoader)
            elif file_path.endswith(".json"):
                data = json.load(f)
            else:
                raise NotImplementedError("Only .yaml and .json is supported")

        for segment in json_path.split("/"):
            if segment == "":
                continue
            try:
                segment = int(segment)
            except ValueError:
                pass
            data = data[segment]

        if filter is not None:
            filter = {item.strip() for item in filter.split(",")}
            to_remove = []
            for key in data.keys():
                if key in filter:
                    to_remove.append(key)
            for key in to_remove:
                del data[key]

        yaml_string = yaml.dump(
            data, sort_keys=False, default_flow_style=None, Dumper=MyYamlDumper
        )
        return f"\n{indent}".join(f"{indent}{yaml_string}".split("\n"))

    @env.macro
    def config_models(models=None):  # pylint: disable=unused-variable
        from nomad.config.models.config import Config

        results = ""
        for name, field in Config.model_fields.items():
            if models and name not in models:
                continue

            if not models and name in exported_config_models:
                continue

            results += pydantic_model_from_model(field.annotation, name)
            results += "\n\n"
        return results

    def pydantic_model_from_model(model, name=None, heading=None, hide=[]):
        if hasattr(model, "model_fields"):
            fields = model.model_fields
        else:
            fields = get_args(model)
        required_models = set()
        if not name:
            exported_config_models.add(model.__name__)  # type: ignore
            name = model.__name__  # type: ignore

        exported_config_models.add(name)

        def content(field):
            result = []
            description = get_field_description(field)
            if description:
                result.append(description)
            default = get_field_default(field)
            if default:
                result.append(f"*default:* {default}")
            options = get_field_options(field)
            if options:
                option_list = "*options:*<br/>"
                for name, desc in options.items():
                    option_list += f" - `{name}{f': {desc}' if desc else ''}`<br/>"
                result.append(option_list)
            if get_field_deprecated(field):
                result.append("**deprecated**")

            return "</br>".join(result)

        def field_row(name: str, field: FieldInfo):
            # The field is not shown in the docs if it has the 'hidden' flag set to True
            if (
                field.json_schema_extra
                and cast(dict, field.json_schema_extra).get("hidden", False) is True
            ):
                return ""
            if name.startswith("m_") or field is None:
                return ""
            type_name, classes = get_field_type_info(field)
            nonlocal required_models
            required_models |= {
                cls for cls in classes if isclass(cls) and issubclass(cls, BaseModel)
            }
            return f"|{name}|`{type_name}`|{content(field)}|\n"

        if heading is None:
            result = f"### {name}\n"
        else:
            result = heading + "\n"

        if model.__doc__ and model.__doc__ != "":
            result += utils.strip(model.__doc__) + "\n\n"

        result += "|name|type| |\n"
        result += "|----|----|-|\n"
        if isinstance(fields, tuple):
            # handling union types
            results: list[str] = []
            for field in fields:
                if hasattr(field, "model_fields"):
                    # if the field is a pydantic model, generate the documentation for that model
                    results.append(pydantic_model_from_model(field, name))
                elif "<class 'NoneType'>" not in str(field):
                    # the check is a bit awkward but checking for None directly falls through
                    results.append(field_row(name, field))
        else:
            results = [
                field_row(name, field)
                for name, field in fields.items()
                if name not in hide
            ]
        results = sorted(results, key=lambda x: "None" in x)
        result += "".join(results)

        for required_model in required_models:
            if required_model.__name__ not in exported_config_models:
                result += "\n\n"
                result += pydantic_model_from_model(required_model)  # type: ignore

        return result

    @env.macro
    def pydantic_model(path, heading=None, hide=[]):  # pylint: disable=unused-variable
        """
        Produces markdown code for the given pydantic model.

        Arguments:
            path: The python qualified name of the model class.
        """
        import importlib

        module_name, name = path.rsplit(".", 1)
        module = importlib.import_module(module_name)
        model = getattr(module, name)

        return pydantic_model_from_model(model, heading=heading, hide=hide)

    @env.macro
    def default_apps_list():  # pylint: disable=unused-variable
        result = ""
        for key, value in config.ui.apps.filtered_items():
            result += f" - `{key}`: {value.description}\n"
        return result

    @env.macro
    def parser_list():  # pylint: disable=unused-variable
        parsers = [
            plugin
            for _, plugin in config.plugins.entry_points.filtered_items()
            if isinstance(plugin, ParserEntryPoint) and hasattr(plugin, "code_name")
        ]
        packages = config.plugins.plugin_packages

        def render_parser(parser) -> str:
            # TODO this should be added, once the metadata typography gets
            # fixed. At the moment the MD is completely broken in most cases.
            # more_description = None
            # if parser.metadata and 'parserSpecific' in parser.metadata:
            #     more_description = strip(parser.metadata['parserSpecific'])
            repo_url = packages[parser.plugin_package].homepage

            metadata = strip(
                f"""
                ### {parser.code_name}

                {parser.description or ""}

                - format homepage: [{parser.code_homepage}]({parser.code_homepage})
                - parser name: `{parser.id}`
                - plugin: `{parser.plugin_package}`
                - parser class: `{parser.parser_class_name}`
                - parser code: [{repo_url}]({repo_url})
            """
            )

            if (
                parser.metadata
                and parser.metadata.get("tableOfFiles", "").strip(" \t\n") != ""
            ):
                metadata += f"\n\n{strip(parser.metadata['tableOfFiles'])}"

            return metadata

        categories: dict[str, list[ParserEntryPoint]] = {}
        for parser in parsers:
            category_name = getattr(parser, "code_category", None)
            category = categories.setdefault(category_name, [])
            category.append(parser)

        def render_category(name: str, category: list[ParserEntryPoint]) -> str:
            return f"## {name}s\n\n" + "\n\n".join(
                [render_parser(parser) for parser in category]
            )

        return (
            ", ".join(
                [
                    f"[{parser.code_name}](#{slugify(parser.code_name, '-')})"
                    for parser in parsers
                ]
            )
            + "\n\n"
            + "\n\n".join(
                [
                    render_category(name, category)
                    for name, category in categories.items()
                ]
            )
        )

    @env.macro
    def plugin_entry_point_list():  # pylint: disable=unused-variable
        plugin_entry_points = [
            plugin for plugin in config.plugins.entry_points.options.values()
        ]
        plugin_packages = config.plugins.plugin_packages

        def render_plugin(plugin: EntryPointType) -> str:
            result = plugin.id
            docs_or_code_url = None
            package = plugin_packages.get(getattr(plugin, "plugin_package"))
            if package is not None:
                for field in [
                    "repository",
                    "homepage",
                    "documentation",
                ]:
                    value = getattr(package, field, None)
                    if value:
                        docs_or_code_url = value
                        break
            if docs_or_code_url:
                result = f"[{plugin.id}]({docs_or_code_url})"

            return result

        categories = {}
        for plugin_entry_point in plugin_entry_points:
            category = getattr(
                plugin_entry_point,
                "plugin_type",
                getattr(plugin_entry_point, "entry_point_type", None),
            )
            if category == "schema":
                category = "schema package"
            categories.setdefault(category, []).append(plugin_entry_point)

        return "\n\n".join(
            [
                f"**{category}**: {', '.join([render_plugin(plugin) for plugin in plugins])}"
                for category, plugins in categories.items()
            ]
        )

    @env.macro
    def metainfo_package(path, heading=None, hide=[]):  # pylint: disable=unused-variable
        """
        Produces markdown code for the given metainfo package.

        Arguments:
            path: The python qualified name of the package.
        """
        import importlib

        module_name, name = path.rsplit(".", 1)
        module = importlib.import_module(path)
        pkg = getattr(module, "m_package")

        return package_markdown_from_package(pkg)

    @env.macro
    def category_tag(name, **kwargs):  # pylint: disable=unused-variable
        """
        Creates a in-line category tag. The tag can be either text or an image.
        In the case of an image, the text is used as alt text.
        In the case of a text tag, the text is presented as a pill.

        Optional arguments can be:
            - tooltip: A tooltip that is shown when hovering over the tag.
            - href: A link that is opened when clicking on the tag.
            - image: URL to the image that is shown instead of the text.
            - style: additional CSS style that is added to the tag.

        Usage in markdown files:
            ```
            {{ category_tag('example', tooltip='Example tooltip', href='example.md') }}
            ```
            or
            ```
            {{ category_tag(name='example', tooltip='Example tooltip', \
                href='example.md', image='../assets/favicon.ico', \
                style='border-radius: 50%;')}}
            ```
        """
        # setup anchor tag
        href = kwargs.get("href", "")
        if href and href.endswith(".md"):
            href = href.replace(".md", ".html")
        tooltip = kwargs.get("tooltip", "")
        if tooltip:
            anchor_tag = [f'<a href="{href}" title="{tooltip}">', "</a>"]
        else:
            anchor_tag = [f'<a href="{href}">', "</a>"]

        style = kwargs.get("style", "")
        if style:
            style = f' style="{style}"'

        image = kwargs.get("image", "")
        if image:
            # Render an image-based category tag
            img_tag = f'<img src="{image}" alt="{name}" class="category-image"{style}>'
            return f"<span>{anchor_tag[0]}{img_tag}{anchor_tag[1]}</span>"
        else:
            # Render a text-based category tag
            return (
                f'<span class="category-pill"{style}>'
                f"{anchor_tag[0]}{name}{anchor_tag[1]}</span>"
            )
