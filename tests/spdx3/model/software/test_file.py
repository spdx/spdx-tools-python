# SPDX-FileCopyrightText: 2023 spdx contributors
#
# SPDX-License-Identifier: Apache-2.0
from unittest import mock

import pytest

from spdx_tools.spdx3.model.software import File, SoftwarePurpose


@mock.patch("spdx_tools.spdx3.model.CreationInformation", autospec=True)
def test_correct_initialization(creation_information):
    file = File(
        "SPDXRef-File",
        creation_information,
        "Test file",
        verified_using=None,
        content_identifier="https://any.uri",
        purpose=[SoftwarePurpose.ARCHIVE, SoftwarePurpose.FILE],
        content_type="MediaType",
    )

    assert file.spdx_id == "SPDXRef-File"
    assert file.creation_info == creation_information
    assert file.name == "Test file"
    assert file.content_identifier == "https://any.uri"
    assert file.purpose == [SoftwarePurpose.ARCHIVE, SoftwarePurpose.FILE]
    assert file.content_type == "MediaType"


@mock.patch("spdx_tools.spdx3.model.CreationInformation", autospec=True)
def test_invalid_initialization(creation_information):
    with pytest.raises(TypeError) as err:
        File(
            1,
            creation_information,
            "test file",
            content_identifier=3,
            purpose=SoftwarePurpose.FILE,
            content_type=SoftwarePurpose.ARCHIVE,
        )

    assert err.value.args[0] == [
        'SetterError File: type of argument "spdx_id" must be str; got int instead: 1',
        'SetterError File: type of argument "content_identifier" must be one of (str, '
        "NoneType); got int instead: 3",
        'SetterError File: type of argument "purpose" must be a list; got '
        "spdx_tools.spdx3.model.software.software_purpose.SoftwarePurpose instead: "
        "SoftwarePurpose.FILE",
        'SetterError File: type of argument "content_type" must be one of (str, '
        "NoneType); got spdx_tools.spdx3.model.software.software_purpose.SoftwarePurpose "
        "instead: SoftwarePurpose.ARCHIVE",
    ]
