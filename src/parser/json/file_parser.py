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

from src.model.checksum import Checksum
from src.model.file import File, FileType
from src.model.license_expression import LicenseExpression
from src.model.spdx_no_assertion import SpdxNoAssertion
from src.model.spdx_none import SpdxNone
from src.parser.json.checksum_parser import ChecksumParser
from src.parser.json.dict_parsing_functions import append_parsed_field_or_log_error, \
    raise_parsing_error_if_logger_has_messages, construct_or_raise_parsing_error, parse_field_or_log_error, \
    parse_field_or_no_assertion_or_none
from src.parser.json.license_expression_parser import LicenseExpressionParser
from src.parser.logger import Logger


class FileParser:
    logger: Logger
    checksum_parser: ChecksumParser
    license_expression_parser: LicenseExpressionParser

    def __init__(self):
        self.logger = Logger()
        self.checksum_parser = ChecksumParser()
        self.license_expression_parser = LicenseExpressionParser()

    def parse_files(self, file_dicts: List[Dict]) -> List[File]:
        files = []
        for file_dict in file_dicts:
            files = append_parsed_field_or_log_error(self.logger, files, file_dict, self.parse_file)
        raise_parsing_error_if_logger_has_messages(self.logger)
        return files

    def parse_file(self, file_dict: Dict) -> Optional[File]:
        logger = Logger()
        name: Optional[str] = file_dict.get("fileName")
        spdx_id: Optional[str] = file_dict.get("SPDXID")
        checksums_list: List[Dict] = file_dict.get("checksums")
        checksums: List[Checksum] = parse_field_or_log_error(logger, checksums_list,
                                                             self.checksum_parser.parse_checksums)

        attribution_texts: List[str] = file_dict.get("attributionTexts", [])
        comment: Optional[str] = file_dict.get("comment")
        copyright_text: Optional[str] = file_dict.get("copyrightText")
        file_contributors: List[str] = file_dict.get("fileContributors", [])
        file_types: List[FileType] = parse_field_or_log_error(logger, file_dict.get("fileTypes"), self.parse_file_types)

        license_comments: Optional[str] = file_dict.get("licenseComments")

        license_concluded: Optional[Union[LicenseExpression, SpdxNoAssertion, SpdxNone]] = parse_field_or_log_error(
            logger, file_dict.get("licenseConcluded"), lambda x: parse_field_or_no_assertion_or_none(x, self.license_expression_parser.parse_license_expression))

        license_info_in_files: Optional[Union[List[LicenseExpression], SpdxNoAssertion, SpdxNone]] = parse_field_or_log_error(
            logger, file_dict.get("licenseInfoInFiles"), lambda x: parse_field_or_no_assertion_or_none(x, self.license_expression_parser.parse_license_expressions))
        notice_text: Optional[str] = file_dict.get("noticeText")
        raise_parsing_error_if_logger_has_messages(logger, "File")

        file = construct_or_raise_parsing_error(File, dict(name=name, spdx_id=spdx_id, checksums=checksums,
                                                           attribution_texts=attribution_texts, comment=comment,
                                                           copyright_text=copyright_text, file_type=file_types,
                                                           contributors=file_contributors,
                                                           license_comment=license_comments,
                                                           concluded_license=license_concluded,
                                                           license_info_in_file=license_info_in_files,
                                                           notice=notice_text)
                                                )
        return file

    @staticmethod
    def parse_file_types(file_types_list: List[str]) -> List[FileType]:
        logger = Logger()
        file_types = []
        for file_type in file_types_list:
            try:
                file_type = FileType[file_type]
            except KeyError:
                logger.append(f"Invalid FileType: {file_type}")
                continue
            file_types.append(file_type)
        raise_parsing_error_if_logger_has_messages(logger, "FileType")
        return file_types
