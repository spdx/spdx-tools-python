from unittest import mock

import pytest

from src.model.checksum import Checksum, ChecksumAlgorithm
from src.model.file import File, FileType
from src.model.spdx_no_assertion import SpdxNoAssertion
from src.model.spdx_none import SpdxNone


@mock.patch('src.model.checksum.Checksum', autospec=True)
def test_correct_initialization(checksum):
    file = File("name", "id", [checksum, checksum], [FileType.OTHER, FileType.SPDX], SpdxNone(), SpdxNoAssertion(),
                "comment on license", "copyright", "comment", "notice", ["contributor"], ["attribution"])
    assert file.name == "name"
    assert file.spdx_id == "id"
    assert file.checksums == [checksum, checksum]
    assert file.file_type == [FileType.OTHER, FileType.SPDX]
    assert file.concluded_license == SpdxNone()
    assert file.license_info_in_file == SpdxNoAssertion()
    assert file.license_comment == "comment on license"
    assert file.copyright_text == "copyright"
    assert file.comment == "comment"
    assert file.notice == "notice"
    assert file.contributors == ["contributor"]
    assert file.attribution_texts == ["attribution"]


@mock.patch('src.model.checksum.Checksum', autospec=True)
def test_correct_initialization_with_default_values(checksum):
    file = File("name", "id", [checksum, checksum])
    assert file.name == "name"
    assert file.spdx_id == "id"
    assert file.checksums == [checksum, checksum]
    assert file.file_type == []
    assert file.concluded_license is None
    assert file.license_info_in_file == []
    assert file.license_comment is None
    assert file.copyright_text is None
    assert file.comment is None
    assert file.notice is None
    assert file.contributors == []
    assert file.attribution_texts == []


@mock.patch('src.model.checksum.Checksum', autospec=True)
def test_wrong_type_in_name(checksum):
    with pytest.raises(TypeError):
        File(42, "id", [checksum])


@mock.patch('src.model.checksum.Checksum', autospec=True)
def test_wrong_type_in_spdx_id(checksum):
    with pytest.raises(TypeError):
        File("name", 42, [checksum])


def test_wrong_type_in_checksum():
    checksum = Checksum(ChecksumAlgorithm.BLAKE2B_256, "value")
    with pytest.raises(TypeError):
        File("name", "id", checksum)


@mock.patch('src.model.checksum.Checksum', autospec=True)
def test_wrong_type_in_file_type(checksum):
    with pytest.raises(TypeError):
        File("name", "id", [checksum], file_type=FileType.OTHER)


@mock.patch('src.model.checksum.Checksum', autospec=True)
def test_wrong_type_in_concluded_license(checksum):
    with pytest.raises(TypeError):
        File("name", "id", [checksum], concluded_license="NONE")


@mock.patch('src.model.checksum.Checksum', autospec=True)
def test_wrong_type_in_license_info_in_file(checksum):
    with pytest.raises(TypeError):
        File("name", "id", [checksum], license_info_in_file=[SpdxNone])


@mock.patch('src.model.checksum.Checksum', autospec=True)
def test_wrong_type_in_license_comment(checksum):
    with pytest.raises(TypeError):
        File("name", "id", [checksum], license_comment=42)


@mock.patch('src.model.checksum.Checksum', autospec=True)
def test_wrong_type_in_copyright_text(checksum):
    with pytest.raises(TypeError):
        File("name", "id", [checksum], copyright_text=[SpdxNone()])


@mock.patch('src.model.checksum.Checksum', autospec=True)
def test_wrong_type_in_comment(checksum):
    with pytest.raises(TypeError):
        File("name", "id", [checksum], comment=42)


@mock.patch('src.model.checksum.Checksum', autospec=True)
def test_wrong_type_in_notice(checksum):
    with pytest.raises(TypeError):
        File("name", "id", [checksum], notice=["notice"])


@mock.patch('src.model.checksum.Checksum', autospec=True)
def test_wrong_type_in_contributors(checksum):
    with pytest.raises(TypeError):
        File("name", "id", [checksum], contributors="contributor")


@mock.patch('src.model.checksum.Checksum', autospec=True)
def test_wrong_type_in_attribution_texts(checksum):
    with pytest.raises(TypeError):
        File("name", "id", [checksum], attribution_texts=["attribution", 42])
