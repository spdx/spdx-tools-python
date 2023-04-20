# SPDX-FileCopyrightText: 2023 spdx contributors
#
# SPDX-License-Identifier: Apache-2.0
from dataclasses import field
from datetime import datetime
from typing import List, Optional

from spdx_tools.common.typing.dataclass_with_properties import dataclass_with_properties
from spdx_tools.common.typing.type_checks import check_types_and_set_values
from spdx_tools.spdx3.model import CreationInfo, ExternalIdentifier, ExternalReference, IntegrityMethod
from spdx_tools.spdx3.model.licensing import LicenseField
from spdx_tools.spdx3.model.software import SoftwarePurpose
from spdx_tools.spdx3.model.software.software_artifact import SoftwareArtifact


@dataclass_with_properties
class File(SoftwareArtifact):
    content_type: Optional[str] = None  # placeholder for MediaType

    def __init__(
        self,
        spdx_id: str,
        creation_info: CreationInfo,
        name: str,
        summary: Optional[str] = None,
        description: Optional[str] = None,
        comment: Optional[str] = None,
        verified_using: List[IntegrityMethod] = None,
        external_references: List[ExternalReference] = None,
        external_identifier: List[ExternalIdentifier] = None,
        extension: Optional[str] = None,
        originated_by: List[str] = None,
        supplied_by: List[str] = None,
        built_time: Optional[datetime] = None,
        release_time: Optional[datetime] = None,
        valid_until_time: Optional[datetime] = None,
        standard: List[str] = None,
        content_identifier: Optional[str] = None,
        purpose: List[SoftwarePurpose] = None,
        concluded_license: Optional[LicenseField] = None,
        declared_license: Optional[LicenseField] = None,
        copyright_text: Optional[str] = None,
        attribution_text: Optional[str] = None,
        content_type: Optional[str] = None,
    ):
        verified_using = [] if verified_using is None else verified_using
        external_references = [] if external_references is None else external_references
        external_identifier = [] if external_identifier is None else external_identifier
        originated_by = [] if originated_by is None else originated_by
        supplied_by = [] if supplied_by is None else supplied_by
        standard = [] if standard is None else standard
        purpose = [] if purpose is None else purpose
        check_types_and_set_values(self, locals())
