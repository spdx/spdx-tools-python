from typing import List

import pytest

from src.model.document import Document
from src.model.relationship import Relationship, RelationshipType
from src.validation.relationship_validator import validate_relationship
from src.validation.validation_message import ValidationMessage, SpdxElementType, ValidationContext
from tests.valid_defaults import get_document, get_package, get_relationship, get_file


def test_valid_relationship():
    document: Document = get_document(packages=[get_package(spdx_id="SPDXRef-Package")])

    relationship = Relationship("SPDXRef-DOCUMENT", RelationshipType.AMENDS, "SPDXRef-Package", comment="comment")
    validation_messages: List[ValidationMessage] = validate_relationship(relationship, document, "2.3")

    assert validation_messages == []


@pytest.mark.parametrize("spdx_element_id, related_spdx_element_id, expected_message",
                         [("SPDXRef-unknownFile", "SPDXRef-File",
                           'did not find the referenced spdx_id SPDXRef-unknownFile in the SPDX document'),
                          ("SPDXRef-File", "SPDXRef-unknownFile",
                           'did not find the referenced spdx_id SPDXRef-unknownFile in the SPDX document'),
                          ])
def test_unknown_spdx_id(spdx_element_id, related_spdx_element_id, expected_message):
    relationship: Relationship = get_relationship(spdx_element_id=spdx_element_id,
                                                  related_spdx_element_id=related_spdx_element_id)
    document: Document = get_document(files=[get_file(spdx_id="SPDXRef-File")])
    validation_messages: List[ValidationMessage] = validate_relationship(relationship, document, "2.3")

    expected = ValidationMessage(expected_message,
                                 ValidationContext(element_type=SpdxElementType.RELATIONSHIP,
                                                   full_element=relationship))

    assert validation_messages == [expected]


@pytest.mark.parametrize("relationship, expected_message",
                         [(Relationship("SPDXRef-DOCUMENT", RelationshipType.SPECIFICATION_FOR, "SPDXRef-Package"),
                           "RelationshipType.SPECIFICATION_FOR is not supported for SPDX versions below 2.3"),
                          (Relationship("SPDXRef-DOCUMENT", RelationshipType.REQUIREMENT_DESCRIPTION_FOR,
                                        "SPDXRef-Package"),
                           "RelationshipType.REQUIREMENT_DESCRIPTION_FOR is not supported for SPDX versions below 2.3")])
def test_v2_3_only_types(relationship, expected_message):
    document: Document = get_document(packages=[get_package(spdx_id="SPDXRef-Package")])

    validation_message: List[ValidationMessage] = validate_relationship(relationship, document, "2.2")

    expected = [ValidationMessage(expected_message,
                                  ValidationContext(element_type=SpdxElementType.RELATIONSHIP,
                                                    full_element=relationship))]

    assert validation_message == expected
