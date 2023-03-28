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
from typing import List

from spdx.model.document import Document
from spdx.model.relationship import RelationshipType
from spdx.model.relationship_filters import filter_by_type_and_origin, filter_by_type_and_target
from spdx.validation.annotation_validator import validate_annotations
from spdx.validation.creation_info_validator import validate_creation_info
from spdx.validation.extracted_licensing_info_validator import validate_extracted_licensing_infos
from spdx.validation.file_validator import validate_files
from spdx.validation.package_validator import validate_packages
from spdx.validation.relationship_validator import validate_relationships
from spdx.validation.snippet_validator import validate_snippets
from spdx.validation.spdx_id_validators import get_list_of_all_spdx_ids
from spdx.validation.validation_message import SpdxElementType, ValidationContext, ValidationMessage


def validate_full_spdx_document(document: Document, spdx_version: str = None) -> List[ValidationMessage]:
    validation_messages: List[ValidationMessage] = []

    # SPDX version validation has to happen here because subsequent validators rely on it
    document_version: str = document.creation_info.spdx_version
    context = ValidationContext(spdx_id=document.creation_info.spdx_id, element_type=SpdxElementType.DOCUMENT)
    if not spdx_version:
        spdx_version = document_version

    if document_version not in ["SPDX-2.2", "SPDX-2.3"]:
        validation_messages.append(
            ValidationMessage(
                f'only SPDX versions "SPDX-2.2" and "SPDX-2.3" are supported, but the document\'s spdx_version is: {document_version}',
                context
            )
        )
    elif spdx_version != document_version:
        validation_messages.append(
            ValidationMessage(f"provided SPDX version {spdx_version} does not match "
                              f"the document's SPDX version {document_version}", context)
        )

    if validation_messages:
        validation_messages.append(ValidationMessage("There are issues concerning the SPDX version of the document. "
                                                     "As subsequent validation relies on the correct version, "
                                                     "the validation process has been cancelled.", context))
        return validation_messages

    validation_messages.extend(validate_creation_info(document.creation_info, spdx_version))
    validation_messages.extend(validate_packages(document.packages, spdx_version, document))
    validation_messages.extend(validate_files(document.files, spdx_version, document))
    validation_messages.extend(validate_snippets(document.snippets, spdx_version, document))
    validation_messages.extend(validate_annotations(document.annotations, document))
    validation_messages.extend(validate_relationships(document.relationships, spdx_version, document))
    validation_messages.extend(validate_extracted_licensing_infos(document.extracted_licensing_info))

    document_id = document.creation_info.spdx_id
    document_describes_relationships = filter_by_type_and_origin(document.relationships, RelationshipType.DESCRIBES,
                                                                 document_id)
    described_by_document_relationships = filter_by_type_and_target(document.relationships,
                                                                    RelationshipType.DESCRIBED_BY, document_id)

    if not document_describes_relationships + described_by_document_relationships:
        validation_messages.append(
            ValidationMessage(
                f'there must be at least one relationship "{document_id} DESCRIBES ..." or "... DESCRIBED_BY '
                f'{document_id}"',
                ValidationContext(spdx_id=document_id,
                                  element_type=SpdxElementType.DOCUMENT)))

    all_spdx_ids: List[str] = get_list_of_all_spdx_ids(document)
    auxiliary_set = set()
    duplicated_spdx_ids = set(
        spdx_id for spdx_id in all_spdx_ids if spdx_id in auxiliary_set or auxiliary_set.add(spdx_id))

    if duplicated_spdx_ids:
        validation_messages.append(
            ValidationMessage(
                f"every spdx_id must be unique within the document, but found the following duplicates: {sorted(duplicated_spdx_ids)}",
                context)
        )

    return validation_messages
