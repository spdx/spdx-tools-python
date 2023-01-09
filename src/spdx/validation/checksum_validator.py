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

import re
from typing import List, Dict

from spdx.model.checksum import Checksum, ChecksumAlgorithm
from spdx.validation.validation_message import ValidationMessage, ValidationContext, SpdxElementType

# in hexadecimal digits
algorithm_length: Dict = {
    ChecksumAlgorithm.SHA1: "40",
    ChecksumAlgorithm.SHA224: "56",
    ChecksumAlgorithm.SHA256: "64",
    ChecksumAlgorithm.SHA384: "96",
    ChecksumAlgorithm.SHA512: "128",
    ChecksumAlgorithm.SHA3_256: "64",
    ChecksumAlgorithm.SHA3_384: "96",
    ChecksumAlgorithm.SHA3_512: "128",
    ChecksumAlgorithm.BLAKE2B_256: "64",
    ChecksumAlgorithm.BLAKE2B_384: "96",
    ChecksumAlgorithm.BLAKE2B_512: "128",
    ChecksumAlgorithm.BLAKE3: "256,",  # at least 256 bits
    ChecksumAlgorithm.MD2: "32",
    ChecksumAlgorithm.MD4: "32",
    ChecksumAlgorithm.MD5: "32",
    ChecksumAlgorithm.MD6: "0,512",  # between 0 and 512 bits
    ChecksumAlgorithm.ADLER32: "8",
}


def validate_checksums(checksums: List[Checksum], parent_id: str) -> List[ValidationMessage]:
    validation_messages = []
    for checksum in checksums:
        validation_messages.extend(validate_checksum(checksum, parent_id))

    return validation_messages


def validate_checksum(checksum: Checksum, parent_id: str) -> List[ValidationMessage]:
    validation_messages = []
    algorithm = checksum.algorithm
    context = ValidationContext(parent_id=parent_id, element_type=SpdxElementType.CHECKSUM,
                                full_element=checksum)

    if not re.match("^[0-9a-f]{" + algorithm_length[algorithm] + "}$", checksum.value):
        if algorithm == ChecksumAlgorithm.BLAKE3:
            length = "at least 256"
        elif algorithm == ChecksumAlgorithm.MD6:
            length = "between 0 and 512"
        else:
            length = algorithm_length[algorithm]
        validation_messages.append(
            ValidationMessage(
                f"value of {algorithm} must consist of {length} hexadecimal digits, but is: {checksum.value} (length: {len(checksum.value)} digits)",
                context)
        )

    return validation_messages
