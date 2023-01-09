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

from spdx.model.checksum import Checksum
from spdx.model.typing.dataclass_with_properties import dataclass_with_properties
from spdx.model.typing.type_checks import check_types_and_set_values


@dataclass_with_properties
class ExternalDocumentRef:
    document_ref_id: str  # of the form "DocumentRef-[idstring]"
    document_uri: str
    checksum: Checksum

    def __init__(self, document_ref_id: str, document_uri: str, checksum: Checksum):
        check_types_and_set_values(self, locals())
