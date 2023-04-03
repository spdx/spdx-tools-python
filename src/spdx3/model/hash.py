# SPDX-FileCopyrightText: 2023 spdx contributors

# SPDX-License-Identifier: Apache-2.0
from enum import Enum, auto
from typing import Optional

from common.typing.dataclass_with_properties import dataclass_with_properties
from common.typing.type_checks import check_types_and_set_values
from spdx3.model.integrity_method import IntegrityMethod


class HashAlgorithm(Enum):
    BLAKE2B256 = auto()
    BLAKE2B384 = auto()
    BLAKE2B512 = auto()
    BLAKE3 = auto()
    MD2 = auto()
    MD4 = auto()
    MD5 = auto()
    MD6 = auto()
    OTHER = auto()
    SHA1 = auto()
    SHA224 = auto()
    SHA256 = auto()
    SHA3_224 = auto()
    SHA3_256 = auto()
    SHA3_384 = auto()
    SHA3_512 = auto()
    SHA384 = auto()
    SHA512 = auto()
    SPDXPVCSHA1 = auto()
    SPDXPVCSHA256 = auto()


@dataclass_with_properties
class Hash(IntegrityMethod):
    algorithm: HashAlgorithm = None
    hash_value: str = None

    def __init__(self, algorithm: HashAlgorithm, hash_value: str, comment: Optional[str] = None):
        check_types_and_set_values(self, locals())
