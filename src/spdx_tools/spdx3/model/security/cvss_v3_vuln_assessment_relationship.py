# SPDX-FileCopyrightText: 2023 spdx contributors
#
# SPDX-License-Identifier: Apache-2.0
from datetime import datetime

from beartype.typing import List, Optional

from spdx_tools.common.typing.dataclass_with_properties import dataclass_with_properties
from spdx_tools.common.typing.type_checks import check_types_and_set_values
from spdx_tools.spdx3.model.core import (
    CreationInfo,
    ExternalIdentifier,
    ExternalReference,
    IntegrityMethod,
    RelationshipCompleteness,
)
from spdx_tools.spdx3.model.security.vuln_assessment_relationship import VulnAssessmentRelationship
from spdx_tools.spdx.model import RelationshipType


@dataclass_with_properties
class CvssV3VulnAssessmentRelationship(VulnAssessmentRelationship):
    score: str = None
    severity: Optional[str] = None
    vector: Optional[str] = None

    def __init__(
        self,
        spdx_id: str,
        from_element: str,
        to: List[str],
        relationship_type: RelationshipType,
        score: str,
        creation_info: Optional[CreationInfo] = None,
        name: Optional[str] = None,
        summary: Optional[str] = None,
        description: Optional[str] = None,
        comment: Optional[str] = None,
        verified_using: List[IntegrityMethod] = [],
        external_reference: List[ExternalReference] = [],
        external_identifier: List[ExternalIdentifier] = [],
        extension: Optional[str] = None,
        completeness: Optional[RelationshipCompleteness] = None,
        start_time: Optional[datetime] = None,
        end_time: Optional[datetime] = None,
        assessed_element: Optional[str] = None,
        published_time: Optional[datetime] = None,
        supplied_by: Optional[str] = None,
        modified_time: Optional[datetime] = None,
        withdrawn_time: Optional[datetime] = None,
        severity: Optional[str] = None,
        vector: Optional[str] = None,
    ):
        verified_using = [] if not verified_using else verified_using
        external_reference = [] if not external_reference else external_reference
        external_identifier = [] if not external_identifier else external_identifier
        check_types_and_set_values(self, locals())
