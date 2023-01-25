# Copyright (c) 2022 spdx contributors
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from dataclasses import field
from datetime import datetime
from enum import Enum, auto
from typing import Optional, Union, List, Dict

from spdx.model.actor import Actor
from spdx.model.checksum import Checksum
from common.typing.dataclass_with_properties import dataclass_with_properties
from spdx.model.license_expression import LicenseExpression
from spdx.model.spdx_no_assertion import SpdxNoAssertion
from spdx.model.spdx_none import SpdxNone
from common.typing.type_checks import check_types_and_set_values


class PackagePurpose(Enum):
    APPLICATION = auto()
    FRAMEWORK = auto()
    LIBRARY = auto()
    CONTAINER = auto()
    OPERATING_SYSTEM = auto()
    DEVICE = auto()
    FIRMWARE = auto()
    SOURCE = auto()
    ARCHIVE = auto()
    FILE = auto()
    INSTALL = auto()
    OTHER = auto()


@dataclass_with_properties
class PackageVerificationCode:
    value: str
    excluded_files: List[str] = field(default_factory=list)

    def __init__(self, value: str, excluded_files: List[str] = None):
        excluded_files = [] if excluded_files is None else excluded_files
        check_types_and_set_values(self, locals())


class ExternalPackageRefCategory(Enum):
    SECURITY = auto()
    PACKAGE_MANAGER = auto()
    PERSISTENT_ID = auto()
    OTHER = auto()


CATEGORY_TO_EXTERNAL_PACKAGE_REF_TYPES: Dict[ExternalPackageRefCategory, List[str]] = {
    ExternalPackageRefCategory.SECURITY : ["cpe22Type", "cpe23Type", "advisory", "fix", "url", "swid"],
    ExternalPackageRefCategory.PACKAGE_MANAGER : ["maven-central", "npm", "nuget", "bower", "purl"],
    ExternalPackageRefCategory.PERSISTENT_ID : ["swh", "gitoid"]
}


@dataclass_with_properties
class ExternalPackageRef:
    category: ExternalPackageRefCategory
    # In theory, once could refine the typing,
    # see https://spdx.github.io/spdx-spec/v2.3/external-repository-identifiers/. But it's probably not worth the
    # effort.
    reference_type: str
    locator: str
    comment: Optional[str] = None

    def __init__(self, category: ExternalPackageRefCategory, reference_type: str, locator: str,
                 comment: Optional[str] = None):
        check_types_and_set_values(self, locals())


@dataclass_with_properties
class Package:
    spdx_id: str
    name: str
    download_location: Union[str, SpdxNoAssertion, SpdxNone]
    version: Optional[str] = None
    file_name: Optional[str] = None
    supplier: Optional[Union[Actor, SpdxNoAssertion]] = None
    originator: Optional[Union[Actor, SpdxNoAssertion]] = None
    files_analyzed: bool = True
    verification_code: Optional[PackageVerificationCode] = None
    checksums: List[Checksum] = field(default_factory=list)
    homepage: Optional[Union[str, SpdxNoAssertion, SpdxNone]] = None
    source_info: Optional[str] = None
    license_concluded: Optional[Union[LicenseExpression, SpdxNoAssertion, SpdxNone]] = None
    license_info_from_files: Optional[Union[List[LicenseExpression], SpdxNoAssertion, SpdxNone]] = field(
        default_factory=list)
    license_declared: Optional[Union[LicenseExpression, SpdxNoAssertion, SpdxNone]] = None
    license_comment: Optional[str] = None
    copyright_text: Optional[Union[str, SpdxNoAssertion, SpdxNone]] = None
    summary: Optional[str] = None
    description: Optional[str] = None
    comment: Optional[str] = None
    external_references: List[ExternalPackageRef] = field(default_factory=list)
    attribution_texts: List[str] = field(default_factory=list)
    primary_package_purpose: Optional[PackagePurpose] = None
    release_date: Optional[datetime] = None
    built_date: Optional[datetime] = None
    valid_until_date: Optional[datetime] = None

    def __init__(self, spdx_id: str, name: str, download_location: Union[str, SpdxNoAssertion, SpdxNone],
                 version: Optional[str] = None, file_name: Optional[str] = None,
                 supplier: Optional[Union[Actor, SpdxNoAssertion]] = None,
                 originator: Optional[Union[Actor, SpdxNoAssertion]] = None,
                 files_analyzed: bool = True, verification_code: Optional[PackageVerificationCode] = None,
                 checksums: List[Checksum] = None, homepage: Optional[Union[str, SpdxNoAssertion, SpdxNone]] = None,
                 source_info: Optional[str] = None,
                 license_concluded: Optional[Union[LicenseExpression, SpdxNoAssertion, SpdxNone]] = None,
                 license_info_from_files: Optional[Union[List[LicenseExpression], SpdxNoAssertion, SpdxNone]] = None,
                 license_declared: Optional[Union[LicenseExpression, SpdxNoAssertion, SpdxNone]] = None,
                 license_comment: Optional[str] = None,
                 copyright_text: Optional[Union[str, SpdxNoAssertion, SpdxNone]] = None,
                 summary: Optional[str] = None, description: Optional[str] = None, comment: Optional[str] = None,
                 external_references: List[ExternalPackageRef] = None, attribution_texts: List[str] = None,
                 primary_package_purpose: Optional[PackagePurpose] = None, release_date: Optional[datetime] = None,
                 built_date: Optional[datetime] = None, valid_until_date: Optional[datetime] = None):
        checksums = [] if checksums is None else checksums
        license_info_from_files = [] if license_info_from_files is None else license_info_from_files
        external_references = [] if external_references is None else external_references
        attribution_texts = [] if attribution_texts is None else attribution_texts
        check_types_and_set_values(self, locals())
