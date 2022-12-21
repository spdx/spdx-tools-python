from typing import List

from src.model.document import Document
from src.model.relationship import RelationshipType
from src.validation.annotation_validator import AnnotationValidator
from src.validation.creation_info_validator import CreationInfoValidator
from src.validation.extracted_licensing_info_validator import ExtractedLicensingInfoValidator
from src.validation.file_validator import FileValidator
from src.validation.package_validator import PackageValidator
from src.validation.relationship_validator import RelationshipValidator
from src.validation.snippet_validator import SnippetValidator
from src.validation.validation_message import ValidationMessage, ValidationContext, SpdxElementType


class DocumentValidator:
    spdx_version: str
    creation_info_validator: CreationInfoValidator
    snippet_validator: SnippetValidator
    annotation_validator: AnnotationValidator
    relationship_validator: RelationshipValidator
    extracted_licensing_info_validator: ExtractedLicensingInfoValidator

    def __init__(self, spdx_version: str):
        self.spdx_version = spdx_version
        self.creation_info_validator = CreationInfoValidator(spdx_version)
        self.extracted_licensing_info_validator = ExtractedLicensingInfoValidator(spdx_version)

    def validate_full_spdx_document(self, document: Document) -> List[ValidationMessage]:
        package_validator = PackageValidator(self.spdx_version, document)
        file_validator = FileValidator(self.spdx_version, document)
        snippet_validator = SnippetValidator(self.spdx_version, document)
        annotation_validator = AnnotationValidator(self.spdx_version, document)
        relationship_validator = RelationshipValidator(self.spdx_version, document)

        validation_messages: List[ValidationMessage] = []

        validation_messages.extend(self.creation_info_validator.validate_creation_info(document.creation_info))
        validation_messages.extend(package_validator.validate_packages(document.packages))
        validation_messages.extend(file_validator.validate_files(document.files))
        validation_messages.extend(snippet_validator.validate_snippets(document.snippets))
        validation_messages.extend(annotation_validator.validate_annotations(document.annotations))
        validation_messages.extend(relationship_validator.validate_relationships(document.relationships))
        validation_messages.extend(self.extracted_licensing_info_validator.validate_extracted_licensing_infos(
            document.extracted_licensing_info))

        document_id = document.creation_info.spdx_id
        document_describes_relationships = [relationship for relationship in document.relationships if
                                            relationship.relationship_type == RelationshipType.DESCRIBES and relationship.spdx_element_id == document_id]
        described_by_document_relationships = [relationship for relationship in document.relationships if
                                               relationship.relationship_type == RelationshipType.DESCRIBED_BY and relationship.related_spdx_element_id == document_id]

        if not document_describes_relationships + described_by_document_relationships:
            validation_messages.append(
                ValidationMessage(
                    f'there must be at least one relationship "{document_id} DESCRIBES ..." or "... DESCRIBED_BY {document_id}"',
                    ValidationContext(spdx_id=document_id,
                                      element_type=SpdxElementType.DOCUMENT)))

        return validation_messages
