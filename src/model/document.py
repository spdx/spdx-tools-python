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
from typing import List, Optional

from src.model.actor import Actor
from src.model.annotation import Annotation
from src.model.dataclass_with_properties import dataclass_with_properties
from src.model.external_document_ref import ExternalDocumentRef
from src.model.extracted_licensing_info import ExtractedLicensingInfo
from src.model.file import File
from src.model.package import Package
from src.model.relationship import Relationship
from src.model.snippet import Snippet
from src.model.type_checks import check_types_and_set_values
from src.model.version import Version


@dataclass_with_properties
class CreationInfo:
    spdx_version: str
    spdx_id: str
    name: str
    document_namespace: str
    creators: List[Actor]
    created: datetime
    creator_comment: Optional[str] = None
    data_license: str = "CC0-1.0"
    external_document_refs: List[ExternalDocumentRef] = field(default_factory=list)
    license_list_version: Optional[Version] = None
    document_comment: Optional[str] = None

    def __init__(self, spdx_version: str, spdx_id: str, name: str, document_namespace: str, creators: List[Actor],
                 created: datetime, creator_comment: Optional[str] = None, data_license: str = "CC0-1.0",
                 external_document_refs: List[ExternalDocumentRef] = None,
                 license_list_version: Optional[Version] = None, document_comment: Optional[str] = None):
        external_document_refs = external_document_refs or []
        check_types_and_set_values(self, locals())


@dataclass_with_properties
class Document:
    creation_info: CreationInfo

    packages: List[Package] = field(default_factory=list)
    files: List[File] = field(default_factory=list)
    snippets: List[Snippet] = field(default_factory=list)
    annotations: List[Annotation] = field(default_factory=list)
    relationships: List[Relationship] = field(default_factory=list)
    extracted_licensing_info: List[ExtractedLicensingInfo] = field(default_factory=list)

    def __init__(self, creation_info: CreationInfo, packages: List[Package] = None, files: List[File] = None,
                 snippets: List[Snippet] = None, annotations: List[Annotation] = None,
                 relationships: List[Relationship] = None,
                 extracted_licensing_info: List[ExtractedLicensingInfo] = None):
        packages = packages or []
        files = files or []
        snippets = snippets or []
        annotations = annotations or []
        relationships = relationships or []
        extracted_licensing_info = extracted_licensing_info or []
        check_types_and_set_values(self, locals())
