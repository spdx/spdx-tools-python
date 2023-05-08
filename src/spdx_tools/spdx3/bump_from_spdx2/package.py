# SPDX-FileCopyrightText: 2023 spdx contributors
#
# SPDX-License-Identifier: Apache-2.0
from typing import Optional, Union

from spdx_tools.spdx3.bump_from_spdx2.actor import bump_actor
from spdx_tools.spdx3.bump_from_spdx2.bump_utils import handle_no_assertion_or_none
from spdx_tools.spdx3.bump_from_spdx2.checksum import bump_checksum
from spdx_tools.spdx3.bump_from_spdx2.message import print_missing_conversion
from spdx_tools.spdx3.model import (
    CreationInformation,
    ExternalIdentifier,
    ExternalIdentifierType,
    ExternalReference,
    ExternalReferenceType,
)
from spdx_tools.spdx3.model.software import Package, SoftwarePurpose
from spdx_tools.spdx3.payload import Payload
from spdx_tools.spdx.model import Actor as Spdx2_Actor
from spdx_tools.spdx.model.package import ExternalPackageRef
from spdx_tools.spdx.model.package import Package as Spdx2_Package


def bump_package(
    spdx2_package: Spdx2_Package, payload: Payload, creation_information: CreationInformation, document_namespace: str
):
    spdx_id = "#".join([document_namespace, spdx2_package.spdx_id])
    download_location = handle_no_assertion_or_none(spdx2_package.download_location, "package.download_location")
    # package.file_name -> ?
    print_missing_conversion("package2.file_name", 0, "https://github.com/spdx/spdx-3-model/issues/83")
    # package.supplier -> Relationship, suppliedBy?
    print_missing_conversion("package2.supplier", 0, "https://github.com/spdx/spdx-3-model/issues/113")
    if isinstance(spdx2_package.originator, Spdx2_Actor):
        originated_by_spdx_id = bump_actor(spdx2_package.originator, payload, creation_information, document_namespace)
    else:
        originated_by_spdx_id = None
    # package.files_analyzed  -> ?
    print_missing_conversion("package2.files_analyzed", 0, "https://github.com/spdx/spdx-3-model/issues/84")
    # package.verification_code -> package.verified_using
    print_missing_conversion(
        "package2.verification_code", 1, "of IntegrityMethod, https://github.com/spdx/spdx-3-model/issues/85"
    )
    # package.checksums -> package.verified_using
    integrity_methods = [bump_checksum(checksum) for checksum in spdx2_package.checksums]
    print_missing_conversion(
        "package2.license_concluded, package2.license_info_from_files, package2.license_declared, "
        "package2.license_comment, package2.copyright_text",
        0,
        "and missing definition of license profile",
    )

    external_references = []
    external_identifiers = []
    purl_refs = [
        external_ref for external_ref in spdx2_package.external_references if external_ref.reference_type == "purl"
    ]
    exactly_one_purl_without_comment = len(purl_refs) == 1 and purl_refs[0].comment is None
    package_url = None
    if exactly_one_purl_without_comment:
        package_url = purl_refs[0].locator
    for spdx2_external_ref in spdx2_package.external_references:
        if exactly_one_purl_without_comment and spdx2_external_ref.reference_type == "purl":
            continue
        id_or_ref = bump_external_package_ref(spdx2_external_ref)
        if isinstance(id_or_ref, ExternalReference):
            external_references.append(id_or_ref)
        elif isinstance(id_or_ref, ExternalIdentifier):
            external_identifiers.append(id_or_ref)

    print_missing_conversion("package2.attribution_texts", 0, "missing definition of license profile")
    package_purpose = (
        [SoftwarePurpose[spdx2_package.primary_package_purpose.name]] if spdx2_package.primary_package_purpose else []
    )

    payload.add_element(
        Package(
            spdx_id,
            creation_information,
            spdx2_package.name,
            summary=spdx2_package.summary,
            description=spdx2_package.description,
            comment=spdx2_package.comment,
            verified_using=integrity_methods,
            external_references=external_references,
            external_identifier=external_identifiers,
            originated_by=originated_by_spdx_id,
            built_time=spdx2_package.built_date,
            release_time=spdx2_package.release_date,
            valid_until_time=spdx2_package.valid_until_date,
            package_purpose=package_purpose,
            package_version=spdx2_package.version,
            download_location=download_location,
            package_url=package_url,
            homepage=spdx2_package.homepage,
            source_info=spdx2_package.source_info,
        )
    )


external_ref_type_map = {
    "cpe22Type": ExternalIdentifierType.CPE22,
    "cpe23Type": ExternalIdentifierType.CPE23,
    "advisory": ExternalReferenceType.SECURITY_ADVISORY,
    "fix": ExternalReferenceType.SECURITY_FIX,
    "url": None,
    "swid": ExternalIdentifierType.SWID,
    "maven-central": None,
    "npm": None,
    "nuget": None,
    "bower": None,
    "purl": ExternalIdentifierType.PURL,
    "swh": ExternalIdentifierType.SWHID,
    "gitoid": ExternalIdentifierType.GITOID,
}


def bump_external_package_ref(
    spdx2_external_ref: ExternalPackageRef,
) -> Optional[Union[ExternalReference, ExternalIdentifier]]:
    reference_type = spdx2_external_ref.reference_type
    locator = spdx2_external_ref.locator
    comment = spdx2_external_ref.comment

    if reference_type not in external_ref_type_map:
        print_missing_conversion(
            reference_type,
            0,
            f"Conversion of ExternalPackageRef of type {reference_type} is currently not supported."
            f"https://github.com/spdx/spdx-3-model/issues/81",
        )
        return None

    id_or_ref_type = external_ref_type_map[reference_type]

    if isinstance(id_or_ref_type, ExternalReferenceType):
        return ExternalReference(id_or_ref_type, [locator], None, comment)
    elif isinstance(id_or_ref_type, ExternalIdentifierType):
        return ExternalIdentifier(id_or_ref_type, locator, comment)
