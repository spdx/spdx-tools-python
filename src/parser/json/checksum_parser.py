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
from typing import Dict, List

from src.model.checksum import Checksum, ChecksumAlgorithm
from src.model.typing.constructor_type_errors import ConstructorTypeErrors
from src.parser.error import SPDXParsingError
from src.parser.json.dict_parsing_functions import transform_json_str_to_enum_name
from src.parser.logger import Logger


class ChecksumParser:
    auxiliary_logger: Logger

    def __init__(self):
        self.auxiliary_logger = Logger()


    def parse_checksum(self, checksum_dict: Dict) -> Checksum:
        algorithm = transform_json_str_to_enum_name(checksum_dict.get("algorithm"))
        try:
            checksum_algorithm = ChecksumAlgorithm[algorithm]
        except KeyError:
            raise SPDXParsingError([f"Algorithm {algorithm} not valid for checksum."])
        checksum_value = checksum_dict.get("checksumValue")
        try:
            checksum = Checksum(checksum_algorithm, checksum_value)
        except ConstructorTypeErrors as err:
            raise SPDXParsingError(err.get_messages())
        return checksum

    def parse_checksums(self, checksum_dicts_list: List[Dict]) -> List[Checksum]:
        checksum_list = []
        for checksum_dict in checksum_dicts_list:
            try:
                checksum_list.append(self.parse_checksum(checksum_dict))
            except SPDXParsingError as err:
                self.auxiliary_logger.append_all(err.get_messages())
                continue
        if self.auxiliary_logger.has_messages():
            raise SPDXParsingError(self.auxiliary_logger.get_messages())

        return checksum_list

