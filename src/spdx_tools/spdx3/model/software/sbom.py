# SPDX-FileCopyrightText: 2023 spdx contributors
#
# SPDX-License-Identifier: Apache-2.0
from typing import List, Optional

from spdx_tools.common.typing.dataclass_with_properties import dataclass_with_properties
from spdx_tools.common.typing.type_checks import check_types_and_set_values
from spdx_tools.spdx3.model import (
    Bom,
    CreationInformation,
    ExternalIdentifier,
    ExternalMap,
    ExternalReference,
    IntegrityMethod,
    NamespaceMap,
)


@dataclass_with_properties
class Sbom(Bom):
    # We overwrite the super-__init__ as check_types_and_set_values()
    # takes care of all fields (including inherited ones).
    def __init__(
        self,
        spdx_id: str,
        creation_info: CreationInformation,
        elements: List[str],
        root_elements: List[str],
        name: Optional[str] = None,
        summary: Optional[str] = None,
        description: Optional[str] = None,
        comment: Optional[str] = None,
        verified_using: Optional[List[IntegrityMethod]] = None,
        external_references: Optional[List[ExternalReference]] = None,
        external_identifier: Optional[List[ExternalIdentifier]] = None,
        extension: None = None,
        namespaces: Optional[List[NamespaceMap]] = None,
        imports: Optional[List[ExternalMap]] = None,
        context: Optional[str] = None,
    ):
        verified_using = [] if verified_using is None else verified_using
        external_references = [] if external_references is None else external_references
        external_identifier = [] if external_identifier is None else external_identifier
        namespaces = [] if namespaces is None else namespaces
        imports = [] if imports is None else imports
        check_types_and_set_values(self, locals())
