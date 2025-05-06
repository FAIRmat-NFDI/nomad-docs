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


import pytest

from nomad.metainfo import Datetime, MSection, Package, Quantity, Reference
from nomad_docs.metainfo import (
    get_property_description,
    get_property_type_info,
    get_quantity_default,
)

m_package = Package()


class Test(MSection):
    pass


m_package.__init_metainfo__()


@pytest.mark.parametrize(
    "type_, name",
    [
        pytest.param(str, "`str`", id="str"),
        pytest.param(int, "`int`", id="int"),
        pytest.param(float, "`float`", id="float"),
        pytest.param(Datetime, "`nomad.metainfo.data_type.Datetime`", id="Datetime"),
        pytest.param(Reference(Test), "[`Test`](#test)", id="internal-ref"),
        pytest.param(
            Reference(Quantity), "`nomad.metainfo.metainfo.Quantity`", id="external-ref"
        ),
    ],
)
def test_property_type_info(type_, name):
    class Test(MSection):
        a = Quantity(type=type_)

    name_found = get_property_type_info(Test.m_def.all_properties["a"], pkg=m_package)
    assert name_found == name


@pytest.mark.parametrize(
    "description",
    [
        pytest.param(None, id="no-description"),
        pytest.param("This is a test description.", id="string-description"),
    ],
)
def test_property_description(description):
    class Test(MSection):
        a: str = Quantity(description=description)

    description_found = get_property_description(Test.m_def.all_properties["a"])
    assert description_found == description


@pytest.mark.parametrize(
    "default, default_str",
    [
        pytest.param(None, "", id="no-default"),
        pytest.param("test", "`test`", id="str-default"),
        pytest.param(1, "`1`", id="int-default"),
        pytest.param(
            {"test": "test"},
            "Complex object, default value not displayed.",
            id="complex-default",
        ),
    ],
)
def test_property_default(default, default_str):
    class Test(MSection):
        a = Quantity(default=default)

    default_found = get_quantity_default(Test.m_def.all_properties["a"])
    assert default_found == default_str
