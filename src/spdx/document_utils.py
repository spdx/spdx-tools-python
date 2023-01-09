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


def get_contained_spdx_element_ids(document: Document) -> List[str]:
    element_ids = [file.spdx_id for file in document.files]
    element_ids.extend([package.spdx_id for package in document.packages])
    element_ids.extend([snippet.spdx_id for snippet in document.snippets])
    return element_ids
