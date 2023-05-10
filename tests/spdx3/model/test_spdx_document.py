# SPDX-FileCopyrightText: 2023 spdx contributors
#
# SPDX-License-Identifier: Apache-2.0
from unittest import mock

import pytest

from spdx_tools.spdx3.model import SpdxDocument


@mock.patch("spdx_tools.spdx3.model.CreationInformation", autospec=True)
def test_correct_initialization(creation_information):
    spdx_document = SpdxDocument(
        "SPDXRef-DOCUMENT", creation_information, "Test document", element=["spdx_id1"], root_element=["spdx_id2"]
    )

    assert spdx_document.spdx_id == "SPDXRef-DOCUMENT"
    assert spdx_document.creation_info == creation_information
    assert spdx_document.name == "Test document"
    assert spdx_document.element == ["spdx_id1"]
    assert spdx_document.root_element == ["spdx_id2"]


def test_invalid_initialization():
    with pytest.raises(TypeError) as err:
        SpdxDocument(1, {"info": 5}, "document name", element=[8], root_element=[])

    assert err.value.args[0] == [
        'SetterError SpdxDocument: type of argument "spdx_id" must be str; got int ' "instead: 1",
        'SetterError SpdxDocument: type of argument "creation_info" must be '
        "spdx_tools.spdx3.model.creation_information.CreationInformation; got dict "
        "instead: {'info': 5}",
        'SetterError SpdxDocument: type of argument "element"[0] must be str; got int ' "instead: [8]",
    ]


@mock.patch("spdx_tools.spdx3.model.CreationInformation", autospec=True)
def test_incomplete_initialization(creation_information):
    with pytest.raises(TypeError) as err:
        SpdxDocument("SPDXRef-Document", creation_information)

    assert (
        "__init__() missing 3 required positional arguments: 'name', 'element', and 'root_element'"
        in err.value.args[0]
    )
