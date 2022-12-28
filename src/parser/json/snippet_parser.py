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
from enum import auto, Enum
from typing import Dict, Tuple, List, Optional, Union

from src.model.license_expression import LicenseExpression
from src.model.snippet import Snippet
from src.model.spdx_no_assertion import SpdxNoAssertion
from src.model.spdx_none import SpdxNone
from src.parser.error import SPDXParsingError
from src.parser.json.dict_parsing_functions import parse_optional_field, try_construction_raise_parsing_error

from src.parser.json.license_expression_parser import LicenseExpressionParser
from src.parser.logger import Logger


class RangeType(Enum):
    BYTE = auto()
    LINE = auto()


class SnippetParser:
    logger: Logger
    license_expression_parser = LicenseExpressionParser

    def __init__(self):
        self.logger = Logger()
        self.license_expression_parser = LicenseExpressionParser()

    def parse_snippets(self, snippet_dicts_list: List[Dict]) -> List[Snippet]:
        snippets_list = []
        for snippet_dict in snippet_dicts_list:
            try:
                snippets_list.append(self.parse_snippet(snippet_dict))
            except SPDXParsingError as err:
                self.logger.append_all(err.get_messages())
        if self.logger.has_messages():
            raise SPDXParsingError(self.logger.get_messages())

        return snippets_list

    def parse_snippet(self, snippet_dict: Dict) -> Snippet:
        logger = Logger()
        spdx_id: str = snippet_dict.get("SPDXID")
        file_spdx_id: str = snippet_dict.get("snippetFromFile")
        name: Optional[str] = snippet_dict.get("name")
        try:
            ranges: Dict = self.parse_ranges(snippet_dict.get("ranges"))
        except SPDXParsingError as err:
            logger.append_all(err.get_messages())
            ranges = {}
        byte_range: Tuple[int, int] = ranges.get(RangeType.BYTE)

        line_range: Optional[Tuple[int, int]] = ranges.get(RangeType.LINE)
        attribution_texts: List[str] = snippet_dict.get("attributionTexts")
        comment: Optional[str] = snippet_dict.get("comment")
        copyright_text: Optional[str] = snippet_dict.get("copyrightText")
        license_comment: Optional[str] = snippet_dict.get("licenseComments")
        try:
            concluded_license: Optional[Union[
                LicenseExpression, SpdxNoAssertion, SpdxNone]] = parse_optional_field(
                snippet_dict.get("licenseConcluded"), self.license_expression_parser.parse_license_expression)
        except SPDXParsingError as err:
            logger.append_all(err.get_messages())
            concluded_license = None
        try:
            license_info: Optional[Union[List[
                LicenseExpression], SpdxNoAssertion, SpdxNone]] = parse_optional_field(
                snippet_dict.get("licenseInfoInSnippets"), self.license_expression_parser.parse_license_expression)
        except SPDXParsingError as err:
            logger.append_all(err.get_messages())
            license_info = None
        if logger.has_messages():
            raise SPDXParsingError([f"Error while parsing snippet: {logger.get_messages()}"])

        snippet = try_construction_raise_parsing_error(Snippet,
                                                       dict(spdx_id=spdx_id, name=name, byte_range=byte_range,
                                                            file_spdx_id=file_spdx_id,
                                                            line_range=line_range,
                                                            attribution_texts=attribution_texts, comment=comment,
                                                            copyright_text=copyright_text,
                                                            license_comment=license_comment,
                                                            concluded_license=concluded_license,
                                                            license_info_in_snippet=license_info))

        return snippet

    def parse_ranges(self, ranges_from_snippet: List[Dict]) -> Dict:
        if not ranges_from_snippet:
            raise SPDXParsingError([f"No ranges dict provided."])
        logger = Logger()
        ranges = {}
        for range_dict in ranges_from_snippet:
            try:
                range_type: RangeType = self.validate_range_and_get_type(range_dict)
                start_end_tuple: Tuple[int, int] = SnippetParser.get_start_end_tuple(range_dict, range_type)
                ranges[range_type] = start_end_tuple
            except ValueError as error:
                logger.append(error.args[0])
        if logger.has_messages():
            raise SPDXParsingError([f"Error while parsing ranges_dict: {logger.get_messages()}"])
        return ranges

    @staticmethod
    def get_start_end_tuple(range_dict: Dict, range_type: RangeType) -> Tuple[int, int]:
        end_pointer: Dict = range_dict["endPointer"]
        start_pointer: Dict = range_dict["startPointer"]
        if range_type == RangeType.BYTE:
            start: int = start_pointer["offset"]
            end: int = end_pointer["offset"]
        else:
            start: int = start_pointer["lineNumber"]
            end: int = end_pointer["lineNumber"]
        return start, end

    def validate_range_and_get_type(self, range_dict: Dict) -> RangeType:
        if ("startPointer" not in range_dict) or ("endPointer" not in range_dict):
            raise ValueError("Start-/ Endpointer missing in ranges_dict.")
        start_pointer_type = self.validate_pointer_and_get_type(range_dict["startPointer"])
        end_pointer_type = self.validate_pointer_and_get_type(range_dict["endPointer"])
        if start_pointer_type != end_pointer_type:
            raise ValueError("Type of startpointer is not the same as type of endpointer.")
        return start_pointer_type

    @staticmethod
    def validate_pointer_and_get_type(pointer: Dict) -> RangeType:
        if ("offset" in pointer and "lineNumber" in pointer) or (
            "offset" not in pointer and "lineNumber" not in pointer):
            raise ValueError("Couldn't determine type of pointer.")
        return RangeType.BYTE if "offset" in pointer else RangeType.LINE
