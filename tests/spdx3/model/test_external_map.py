# SPDX-FileCopyrightText: 2023 spdx contributors
#
# SPDX-License-Identifier: Apache-2.0
from unittest import mock

import pytest

from spdx_tools.spdx3.model import ExternalMap


@mock.patch("spdx_tools.spdx3.model.IntegrityMethod", autospec=True)
def test_correct_initialization(integrity_method):
    external_map = ExternalMap("https://external.id", [integrity_method], "https://location.hint")

    assert external_map.external_id == "https://external.id"
    assert external_map.verified_using == [integrity_method]
    assert external_map.location_hint == "https://location.hint"


def test_invalid_initialization():
    with pytest.raises(TypeError) as err:
        ExternalMap(234, None, ["location  hints"])

    assert err.value.args[0] == [
        'SetterError ExternalMap: type of argument "external_id" must be str; got int ' "instead: 234",
        'SetterError ExternalMap: type of argument "location_hint" must be one of '
        "(str, NoneType); got list instead: ['location  hints']",
    ]
