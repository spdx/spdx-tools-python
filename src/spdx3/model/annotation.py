# SPDX-FileCopyrightText: 2023 spdx contributors
#
# SPDX-License-Identifier: Apache-2.0
from enum import Enum, auto
from typing import List, Optional

from common.typing.dataclass_with_properties import dataclass_with_properties
from common.typing.type_checks import check_types_and_set_values
from spdx3.model.creation_information import CreationInformation
from spdx3.model.element import Element
from spdx3.model.external_identifier import ExternalIdentifier
from spdx3.model.external_reference import ExternalReference
from spdx3.model.integrity_method import IntegrityMethod


class AnnotationType(Enum):
    REVIEW = auto()
    OTHER = auto()


@dataclass_with_properties
class Annotation(Element):
    annotation_type: AnnotationType = None
    subject: str = None
    content_type: Optional[str] = None  # placeholder for MediaType
    statement: Optional[str] = None

    def __init__(
        self,
        spdx_id: str,
        creation_info: CreationInformation,
        annotation_type: AnnotationType,
        subject: str,
        name: Optional[str] = None,
        summary: Optional[str] = None,
        description: Optional[str] = None,
        comment: Optional[str] = None,
        verified_using: Optional[List[IntegrityMethod]] = None,
        external_references: Optional[List[ExternalReference]] = None,
        external_identifier: Optional[List[ExternalIdentifier]] = None,
        extension: None = None,
        content_type: Optional[str] = None,
        statement: Optional[str] = None,
    ):
        verified_using = [] if verified_using is None else verified_using
        external_references = [] if external_references is None else external_references
        external_identifier = [] if external_identifier is None else external_identifier
        check_types_and_set_values(self, locals())
