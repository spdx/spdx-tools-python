from typing import List

from src.model.external_document_ref import ExternalDocumentRef
from src.validation.checksum_validator import validate_checksum
from src.validation.spdx_id_validators import is_valid_external_doc_ref_id
from src.validation.uri_validators import validate_uri
from src.validation.validation_message import ValidationMessage, ValidationContext, SpdxElementType


def validate_external_document_refs(external_document_refs: List[ExternalDocumentRef], parent_id: str) -> List[
    ValidationMessage]:
    validation_messages = []
    for external_document_ref in external_document_refs:
        validation_messages.extend(validate_external_document_ref(external_document_ref, parent_id))

    return validation_messages


def validate_external_document_ref(external_document_ref: ExternalDocumentRef, parent_id: str) -> List[ValidationMessage]:
    validation_messages = []
    context = ValidationContext(parent_id=parent_id, element_type=SpdxElementType.EXTERNAL_DOCUMENT_REF,
                                full_element=external_document_ref)

    if not is_valid_external_doc_ref_id(external_document_ref.document_ref_id):
        validation_messages.append(
            ValidationMessage(
                f'document_ref_id must only contain letters, numbers, ".", "-" and "+" and must begin with "DocumentRef-", but is: {external_document_ref.document_ref_id}',
                context
            )
        )

    for message in validate_uri(external_document_ref.document_uri):
        validation_messages.append(
            ValidationMessage(
                "document_uri " + message, context
            )
        )

    validation_messages.extend(validate_checksum(external_document_ref.checksum, parent_id))

    return validation_messages
