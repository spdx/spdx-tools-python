from typing import List
import pytest

from src.model.checksum import Checksum, ChecksumAlgorithm
from src.model.file import File, FileType
from src.model.spdx_no_assertion import SpdxNoAssertion
from src.model.spdx_none import SpdxNone
from src.validation.file_validator import FileValidator
from src.validation.validation_message import ValidationMessage, ValidationContext, SpdxElementType
from tests.valid_defaults import get_checksum, get_file, get_document


def test_correct_file():
    file_validator = FileValidator("2.3", get_document())

    file = File("./file/name.py", "SPDXRef-File", [get_checksum()], [FileType.OTHER, FileType.SPDX], SpdxNone(), SpdxNoAssertion(),
                "comment on license", "copyright", "comment", "notice", ["contributor"], ["attribution"])
    validation_messages: List[ValidationMessage] = file_validator.validate_file(file)

    assert validation_messages == []


@pytest.mark.parametrize("file_input, spdx_id, expected_message",
                         [(get_file(spdx_id="SPDXRef-some_file"), "SPDXRef-some_file",
                           'spdx_id must only contain letters, numbers, "." and "-" and must begin with "SPDXRef-", but is: SPDXRef-some_file'),
                          (get_file(name="wrong file name"), get_file().spdx_id,
                           'file name must be a relative path to the file, starting with "./", but is: wrong file name'),
                          (get_file(checksums=[Checksum(ChecksumAlgorithm.MD2, "d4c41ce30a517d6ce9d79c8c17bb4b66")]), get_file().spdx_id,
                           f'checksums must contain a SHA1 algorithm checksum, but is: {[Checksum(ChecksumAlgorithm.MD2, "d4c41ce30a517d6ce9d79c8c17bb4b66")]}')
                          ])
def test_wrong_file(file_input, spdx_id, expected_message):
    file_validator = FileValidator("2.3", get_document())
    validation_messages: List[ValidationMessage] = file_validator.validate_file(file_input)

    expected = ValidationMessage(expected_message,
                                 ValidationContext(spdx_id=spdx_id,
                                                   element_type=SpdxElementType.FILE,
                                                   full_element=file_input))

    assert validation_messages == [expected]
