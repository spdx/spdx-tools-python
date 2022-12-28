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
from typing import Dict, List, Optional, Union

from src.model.extracted_licensing_info import ExtractedLicensingInfo
from src.model.spdx_no_assertion import SpdxNoAssertion
from src.model.typing.constructor_type_errors import ConstructorTypeErrors
from src.parser.error import SPDXParsingError
from src.parser.json.dict_parsing_functions import parse_optional_field
from src.parser.logger import Logger


class ExtractedLicensingInfoParser:
    logger: Logger

    def __init__(self):
        self.logger = Logger()

    def parse_extracted_licensing_infos(self, extracted_licensing_info_dicts: List[Dict]) -> List[
        ExtractedLicensingInfo]:
        extracted_licensing_info_list = []
        for extracted_licensing_info_dict in extracted_licensing_info_dicts:
            try:
                extracted_licensing_info_list.append(self.parse_extracted_licensing_info(extracted_licensing_info_dict))
            except SPDXParsingError as err:
                self.logger.append_all(err.get_messages())
        if self.logger.has_messages():
            raise SPDXParsingError(self.logger.get_messages())
        return extracted_licensing_info_list

    def parse_extracted_licensing_info(self, extracted_licensing_info_dict: Dict) -> ExtractedLicensingInfo:
        license_id: Optional[str] = extracted_licensing_info_dict.get("licenseId")
        extracted_text: Optional[str] = extracted_licensing_info_dict.get("extractedText")
        license_name: Optional[Union[str, SpdxNoAssertion]] = parse_optional_field(
            extracted_licensing_info_dict.get("name"), self.parse_extracted_licensing_info_name)
        cross_references: List[str] = extracted_licensing_info_dict.get("seeAlsos")
        comment: str = extracted_licensing_info_dict.get("comment")

        try:
            extracted_licensing_info_dict = ExtractedLicensingInfo(license_id=license_id, extracted_text=extracted_text,
                                                                   comment=comment, license_name=license_name,
                                                                   cross_references=cross_references)
        except ConstructorTypeErrors as err:
            raise SPDXParsingError([f"Error while constructing ExtractedLicensingInfo : {err.get_messages()}"])
        return extracted_licensing_info_dict

    @staticmethod
    def parse_extracted_licensing_info_name(extracted_licensing_info_name_or_no_assertion) -> Union[str, SpdxNoAssertion]:
        if extracted_licensing_info_name_or_no_assertion == SpdxNoAssertion().__str__():
            return SpdxNoAssertion()
        else:
            return extracted_licensing_info_name_or_no_assertion
