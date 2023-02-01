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
import pytest
from rdflib import Graph, URIRef, RDF, Literal, RDFS
from spdx.writer.rdf.writer_utils import SPDX_NAMESPACE, POINTER_NAMESPACE

from spdx.writer.rdf.snippet_writer import add_snippet_information_to_graph, add_range_to_graph
from tests.spdx.fixtures import snippet_fixture


def test_add_snippet_information_to_graph():
    graph = Graph()
    snippet = snippet_fixture()

    add_snippet_information_to_graph(snippet, graph, "docNamespace", {})

    assert (URIRef("docNamespace#SPDXRef-Snippet"), RDF.type, SPDX_NAMESPACE.Snippet) in graph
    assert (None, SPDX_NAMESPACE.snippetFromFile, URIRef(f"docNamespace#{snippet.file_spdx_id}")) in graph
    assert (None, SPDX_NAMESPACE.licenseConcluded, None) in graph
    assert (None, SPDX_NAMESPACE.licenseInfoInSnippet, None) in graph
    assert (None, SPDX_NAMESPACE.licenseComments, Literal("snippetLicenseComment")) in graph
    assert (None, SPDX_NAMESPACE.copyrightText, Literal("licenseCopyrightText")) in graph
    assert (None, SPDX_NAMESPACE.name, Literal("snippetName")) in graph
    assert (None, SPDX_NAMESPACE.attributionText, Literal("snippetAttributionText")) in graph
    assert (None, RDFS.comment, Literal("snippetComment")) in graph


@pytest.mark.parametrize("range,pointer,predicate",
                         [((5, 190), POINTER_NAMESPACE.ByteOffsetPointer, POINTER_NAMESPACE.offset),
                          ((1, 3), POINTER_NAMESPACE.LineCharPointer, POINTER_NAMESPACE.lineNumber)])
def test_add_ranges_to_graph(range, pointer, predicate):
    graph = Graph()
    add_range_to_graph(range, graph, URIRef("anyUR"), URIRef("docNamespace#SPDXRef-File"), pointer)

    assert (None, SPDX_NAMESPACE.range, None) in graph
    assert (None, POINTER_NAMESPACE.startPointer, None) in graph
    assert (None, POINTER_NAMESPACE.endPointer, None) in graph
    assert (None, POINTER_NAMESPACE.reference, URIRef("docNamespace#SPDXRef-File")) in graph
    assert (None, predicate, Literal(range[0])) in graph
    assert (None, predicate, Literal(range[1])) in graph
