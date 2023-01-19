# Copyright (c) 2023 spdx contributors
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#   http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from typing import TextIO

from spdx3.model.annotation import Annotation
from spdx3.model.bom import Bom
from spdx3.model.bundle import Bundle

from spdx3.model.software.file import File
from spdx3.model.software.package import Package
from spdx3.model.relationship import Relationship
from spdx3.model.software.sbom import Sbom
from spdx3.model.software.snippet import Snippet
from spdx3.model.spdx_document import SpdxDocument
from spdx3.spdx_id_map import SpdxIdMap

from spdx3.writer.console.annotation_writer import write_annotation
from spdx3.writer.console.bom_writer import write_bom
from spdx3.writer.console.bundle_writer import write_bundle
from spdx3.writer.console.relationship_writer import write_relationship
from spdx3.writer.console.software.file_writer import write_file
from spdx3.writer.console.software.package_writer import write_package
from spdx3.writer.console.software.sbom_writer import write_sbom
from spdx3.writer.console.software.snippet_writer import write_snippet
from spdx3.writer.console.spdx_document_writer import write_spdx_document

MAP_CLASS_TO_WRITE_METHOD = {
    Annotation: write_annotation,
    Relationship: write_relationship,
    Bundle: write_bundle,
    SpdxDocument: write_spdx_document,
    Bom: write_bom,
    File: write_file,
    Package: write_package,
    Snippet: write_snippet,
    Sbom: write_sbom
}
def write_spdx_id_map(spdx_id_map: SpdxIdMap, text_output: TextIO):
    for element in spdx_id_map.get_full_map().values():
        write_method = MAP_CLASS_TO_WRITE_METHOD[type(element)]
        write_method(element, text_output)
        text_output.write("\n")

