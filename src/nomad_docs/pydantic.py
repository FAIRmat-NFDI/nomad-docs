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

from enum import Enum
from inspect import isclass
from types import UnionType
from typing import Annotated, Any, Literal, Union, get_args, get_origin

from pydantic import BaseModel
from pydantic.fields import FieldInfo

from nomad import utils

exported_config_models = set()  # type: ignore


def get_field_type_info(field: FieldInfo) -> tuple[str, set[Any]]:
    """Used to recursively walk through a type definition, building up a cleaned
    up type name and returning all of the classes that were used.

    Args:
        type_: The type to inspect. Can be any valid type definition.

    Returns:
        Tuple containing the cleaned up type name and a set of classes
        found inside.
    """
    classes = set()
    annotation = field.annotation

    def get_class_name(ann: Any) -> str:
        if hasattr(ann, "__name__"):
            name = ann.__name__
            return "None" if name == "NoneType" else name
        return str(ann)

    def _recursive_extract(ann: Any, type_str: str = "") -> str:
        nonlocal classes

        origin = get_origin(ann)
        args = get_args(ann)

        if origin is None and issubclass(ann, Enum):
            classes.add(ann)
            # Determine base type for Enums
            if issubclass(ann, str):
                return get_class_name(str)
            elif issubclass(ann, int):
                return get_class_name(int)
            else:
                return get_class_name(ann)
        elif origin is None:
            classes.add(ann)
            return get_class_name(ann)
        if origin is list:
            classes.add(origin)
            if type_str:
                type_str += "[" + _recursive_extract(args[0]) + "]"
            else:
                type_str = "list[" + _recursive_extract(args[0]) + "]"
        elif origin is dict:
            classes.add(origin)
            if type_str:
                type_str += (
                    "["
                    + _recursive_extract(args[0])
                    + ", "
                    + _recursive_extract(args[1])
                    + "]"
                )
            else:
                type_str = (
                    "dict["
                    + _recursive_extract(args[0])
                    + ", "
                    + _recursive_extract(args[1])
                    + "]"
                )

        elif origin is UnionType or origin is Union:
            # Handle Union types (e.g., Optional[str] is equivalent to Union[str, None])
            union_types = []
            for arg in args:
                union_types.append(_recursive_extract(arg))
            type_str = " | ".join(union_types)
        elif origin is Literal:
            classes.add(origin)
            return get_class_name(
                type(args[0])
            )  # Add name of the literal value (e.g., str)
        elif origin is Annotated:
            # Extract the underlying type from Annotated
            return _recursive_extract(args[0])
        else:
            # Handle generic types
            classes.add(origin)
            return get_class_name(ann)

        return type_str

    type_name = _recursive_extract(annotation)
    return type_name, classes


def get_field_description(field: FieldInfo) -> str | None:
    """Retrieves the description for a pydantic field as a markdown string.

    Args:
        field: The pydantic field to inspect.

    Returns:
        Markdown string for the description.
    """
    value = field.description
    if value:
        value = utils.strip(value)
        value = value.replace("\n\n", "<br/>").replace("\n", " ")

    return value


def get_field_default(field: FieldInfo) -> str | None:
    """Retrieves the default value from a pydantic field as a markdown string.

    Args:
        field: The pydantic field to inspect.

    Returns:
        Markdown string for the default value.
    """
    default_value = field.default
    if default_value is not None:
        if isinstance(default_value, dict | BaseModel):
            default_value = "Complex object, default value not displayed."
        elif default_value == "":
            default_value = '""'
        else:
            default_value = f"`{default_value}`"
    return default_value


def get_field_options(field: FieldInfo) -> dict[str, str | None]:
    """Retrieves a dictionary of value-description pairs from a pydantic field.

    Args:
        field: The pydantic field to inspect.

    Returns:
        Dictionary containing the possible options and their description for
        this field. The description may be None indicating that it does not exist.
    """
    options: dict[str, str | None] = {}
    if isclass(field.annotation) and issubclass(field.annotation, Enum):
        for x in field.annotation:
            options[str(x.value)] = None
    return options


def get_field_deprecated(field: FieldInfo) -> bool:
    """Returns whether the given pydantic field is deprecated or not.

    Args:
        field: The pydantic field to inspect.

    Returns:
        Whether the field is deprecated.
    """
    if field.deprecated:
        return True
    return False
