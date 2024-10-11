# SPDX-FileCopyrightText: 2023 spdx contributors
#
# SPDX-License-Identifier: Apache-2.0
from beartype.typing import List, Optional

from spdx_tools.common.typing.dataclass_with_properties import dataclass_with_properties
from spdx_tools.common.typing.type_checks import check_types_and_set_values

from .creation_info import CreationInfo
from .element_collection import ElementCollection
from .external_identifier import ExternalIdentifier
from .external_map import ExternalMap
from .external_ref import ExternalRef
from .integrity_method import IntegrityMethod
from .namespace_map import NamespaceMap
from .profile_identifier import ProfileIdentifierType


@dataclass_with_properties
class Bundle(ElementCollection):
    context: Optional[str] = None

    def __init__(
        self,
        spdx_id: str,
        element: List[str],
        root_element: List[str],
        creation_info: Optional[CreationInfo] = None,
        name: Optional[str] = None,
        summary: Optional[str] = None,
        description: Optional[str] = None,
        comment: Optional[str] = None,
        verified_using: List[IntegrityMethod] = [],
        external_ref: List[ExternalRef] = [],
        external_identifier: List[ExternalIdentifier] = [],
        extension: Optional[str] = None,
        namespace: List[NamespaceMap] = [],
        import_: List[ExternalMap] = [],
        context: Optional[str] = None,
        profile_conformance: List[ProfileIdentifierType] = [],
    ):
        verified_using = [] if not verified_using else verified_using
        external_ref = [] if not external_ref else external_ref
        external_identifier = [] if not external_identifier else external_identifier
        namespace = [] if not namespace else namespace
        import_ = [] if not import_  else import_
        check_types_and_set_values(self, locals())
