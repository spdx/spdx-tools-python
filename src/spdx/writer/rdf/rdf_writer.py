# Copyright (c) 2023 spdx contributors
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from rdflib import Graph
from rdflib.compare import to_isomorphic

from spdx.model.document import Document
from spdx.writer.rdf.annotation_writer import add_annotation_info_to_graph
from spdx.writer.rdf.creation_info_writer import add_creation_info_to_graph
from spdx.writer.rdf.writer_utils import spdx_namespace


def write_document_to_file(document: Document, file_name: str):
    graph = Graph()

    add_creation_info_to_graph(document.creation_info, graph)
    for annotation in document.annotations:
        add_annotation_info_to_graph(annotation, graph, document.creation_info.document_namespace)

    graph = to_isomorphic(graph)
    graph.bind("spdx", spdx_namespace())
    graph.serialize(file_name, "pretty-xml", encoding="UTF-8")
