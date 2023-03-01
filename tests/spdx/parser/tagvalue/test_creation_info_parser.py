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
from datetime import datetime
from unittest import TestCase

import pytest

from spdx.model.actor import Actor, ActorType
from spdx.model.checksum import Checksum, ChecksumAlgorithm
from spdx.model.external_document_ref import ExternalDocumentRef
from spdx.model.version import Version
from spdx.parser.tagvalue.parser.tagvalue import Parser

DOCUMENT_STR = '\n'.join([
    'SPDXVersion: SPDX-2.3',
    'DataLicense: CC0-1.0',
    'DocumentName: Sample_Document-V2.3',
    'SPDXID: SPDXRef-DOCUMENT',
    'DocumentComment: <text>Sample Comment</text>',
    'DocumentNamespace: https://spdx.org/spdxdocs/spdx-example-444504E0-4F89-41D3-9A0C-0305E82C3301',
    'ExternalDocumentRef: DocumentRef-spdx-tool-1.2 http://spdx.org/spdxdocs/spdx-tools-v1.2-3F2504E0-4F89-41D3-9A0C-0305E82C3301 SHA1: d6a770ba38583ed4bb4525bd96e50461655d2759',
    'Creator: Person: Bob (bob@example.com)',
    'Creator: Organization: Acme.',
    'Created: 2010-02-03T00:00:00Z',
    'CreatorComment: <text>Sample Comment</text>',
    'LicenseListVersion: 3.17'
])


@pytest.fixture
def parser():
    spdx_parser = Parser()
    spdx_parser.build()
    return spdx_parser


def test_creation_info(parser):
    document = parser.parse(DOCUMENT_STR)
    assert document is not None
    creation_info = document.creation_info
    assert creation_info is not None
    assert creation_info.spdx_version == "SPDX-2.3"
    assert creation_info.data_license == 'CC0-1.0'
    assert creation_info.name == 'Sample_Document-V2.3'
    assert creation_info.spdx_id == 'SPDXRef-DOCUMENT'
    assert creation_info.document_comment == 'Sample Comment'
    assert creation_info.document_namespace == 'https://spdx.org/spdxdocs/spdx-example-444504E0-4F89-41D3-9A0C-0305E82C3301'
    TestCase().assertCountEqual(creation_info.creators,
                                [Actor(ActorType.PERSON, "Bob", "bob@example.com"),
                                 Actor(ActorType.ORGANIZATION, "Acme.")])
    assert creation_info.creator_comment == 'Sample Comment'
    assert creation_info.created == datetime(2010, 2, 3, 0, 0)
    assert creation_info.license_list_version == Version(3, 17)
    TestCase().assertCountEqual(creation_info.external_document_refs,
                                [ExternalDocumentRef("DocumentRef-spdx-tool-1.2",
                                                     "http://spdx.org/spdxdocs/spdx-tools-v1.2-3F2504E0-4F89-41D3-9A0C-0305E82C3301",
                                                     Checksum(ChecksumAlgorithm.SHA1,
                                                              "d6a770ba38583ed4bb4525bd96e50461655d2759"))])
