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
from rdflib import Graph, BNode, RDF, Literal, RDFS, URIRef

from spdx.datetime_conversions import datetime_to_iso_string
from spdx.model.document import CreationInfo
from spdx.writer.rdf.external_document_ref_writer import add_external_document_ref_to_graph
from spdx.writer.rdf.writer_utils import spdx_namespace, add_literal_value


def add_creation_info_to_graph(creation_info: CreationInfo, graph: Graph):
    doc_node = URIRef(f"{creation_info.document_namespace}#{creation_info.spdx_id}")
    graph.add((doc_node, RDF.type, spdx_namespace.SpdxDocument))
    graph.add((doc_node, spdx_namespace.specVersion, Literal(creation_info.spdx_version)))
    graph.add((doc_node, spdx_namespace.dataLicense, Literal(creation_info.data_license)))
    graph.add((doc_node, spdx_namespace.name, Literal(creation_info.name)))
    add_literal_value(graph, doc_node, RDFS.comment, creation_info.document_comment)

    creation_info_node = BNode()
    graph.add((creation_info_node, RDF.type, spdx_namespace.CreationInfo))

    graph.add((creation_info_node, spdx_namespace.created, Literal(datetime_to_iso_string(creation_info.created))))

    for creator in creation_info.creators:
        graph.add((creation_info_node, spdx_namespace.creator, Literal(creator.to_serialized_string())))

    add_literal_value(graph, creation_info_node, spdx_namespace.licenseListVersion, creation_info.license_list_version)
    add_literal_value(graph, creation_info_node, RDFS.comment, creation_info.creator_comment)

    graph.add((doc_node, spdx_namespace.creationInfo, creation_info_node))

    for external_document_ref in creation_info.external_document_refs:
        add_external_document_ref_to_graph(external_document_ref, graph, doc_node, creation_info.document_namespace)

    return doc_node
