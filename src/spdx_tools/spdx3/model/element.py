# SPDX-FileCopyrightText: 2023 spdx contributors
#
# SPDX-License-Identifier: Apache-2.0
from abc import ABC, abstractmethod
from dataclasses import field
from typing import List, Optional

from spdx_tools.common.typing.dataclass_with_properties import dataclass_with_properties
from spdx_tools.spdx3.model import CreationInformation, ExternalIdentifier, ExternalReference, IntegrityMethod


@dataclass_with_properties
class Element(ABC):
    spdx_id: str  # IRI
    creation_info: CreationInformation
    name: Optional[str] = None
    summary: Optional[str] = None
    description: Optional[str] = None
    comment: Optional[str] = None
    verified_using: Optional[List[IntegrityMethod]] = field(default_factory=list)
    external_references: Optional[List[ExternalReference]] = field(default_factory=list)
    external_identifier: Optional[List[ExternalIdentifier]] = field(default_factory=list)
    extension: None = None  # placeholder for extension

    @abstractmethod
    def __init__(self):
        pass
