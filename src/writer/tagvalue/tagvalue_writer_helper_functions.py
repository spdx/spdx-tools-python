#  Copyright (c) 2022 spdx contributors
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#    http://www.apache.org/licenses/LICENSE-2.0
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
from typing import TextIO, Tuple, List, Dict, Any, Union, Callable

from src.model.actor import Actor
from src.model.file import File
from src.model.license_expression import LicenseExpression
from src.model.package import Package
from src.model.relationship import Relationship
from src.model.snippet import Snippet
from src.model.spdx_no_assertion import SpdxNoAssertion
from src.model.spdx_none import SpdxNone


def write_separator(out: TextIO):
    out.write("\n")


def write_value(tag: str, value: Union[bool, str, SpdxNone, SpdxNoAssertion], out: TextIO, optional: bool = False):
    if optional and not value:
        return
    out.write(f"{tag}: {value}\n")


def write_range(tag: str, value: Tuple[int, int], out: TextIO, optional: bool = False):
    if optional and not value:
        return
    out.write(f"{tag}: {value[0]}:{value[1]}\n")


def write_text_value(tag: str, value: str, out: TextIO, optional: bool = False):
    if optional and not value:
        return
    if "\n" in value:
        out.write(f"{tag}: <text>{value}</text>\n")
    else:
        write_value(tag, value, out, True)


def transform_enum_name_to_tv(enum_str: str) -> str:
    return enum_str.replace("_", "-")


def write_optional_heading(optional_field: Any, heading: str, text_output: TextIO):
    if not optional_field:
        return
    text_output.write(heading)


def write_list_of_elements(list_of_elements: List[Any], write_method: Callable[[Any, TextIO], None],
                           text_output: TextIO, with_separator: bool = False):
    for element in list_of_elements:
        write_method(element, text_output)
        if with_separator:
            write_separator(text_output)


def write_actor_or_no_assertion(tag: str, element_to_write: Any, text_output: TextIO, optional: bool):
    if optional and not element_to_write:
        return
    if isinstance(element_to_write, SpdxNoAssertion):
        write_value(tag, element_to_write, text_output)
        return
    if isinstance(element_to_write, Actor):
        write_value(tag, element_to_write.to_serialized_string(), text_output)
        return
    else:
        write_value(tag, element_to_write, text_output)


def write_field_or_none_or_no_assertion(tag: str, element_to_write: Union[
    List[LicenseExpression], LicenseExpression, SpdxNoAssertion, SpdxNone], text_output: TextIO,
                                        optional: bool = False):
    if optional and not element_to_write:
        return
    if isinstance(element_to_write, (SpdxNone, SpdxNoAssertion)):
        write_value(tag, element_to_write, text_output)
        return
    if isinstance(element_to_write, LicenseExpression):
        write_value(tag, element_to_write.expression_string, text_output)
        return
    if isinstance(element_to_write, str):
        write_value(tag, element_to_write, text_output)
        return
    if isinstance(element_to_write, list):
        for element in element_to_write:
            write_value(tag, element.expression_string, text_output)


def scan_relationships(relationships: List[Relationship], packages: List[Package], files: List[File]) \
    -> Tuple[List, Dict]:
    contained_files_by_package_id = dict()
    relationships_to_write = []
    files_by_spdx_id = {file.spdx_id: file for file in files}
    packages_spdx_ids = [package.spdx_id for package in packages]
    for relationship in relationships:
        if relationship.relationship_type == "CONTAINS" and \
            relationship.spdx_element_id in packages_spdx_ids and \
            relationship.related_spdx_element in files_by_spdx_id.keys():
            contained_files_by_package_id.setdefault(relationship.spdx_element_id, []).append(
                files_by_spdx_id[relationship.related_spdx_element])
            if relationship.has_comment:
                relationships_to_write.append(relationship)
        elif relationship.relationship_type == "CONTAINED_BY" and \
            relationship.related_spdx_element in packages_spdx_ids and \
            relationship.spdx_element_id in files_by_spdx_id:
            contained_files_by_package_id.setdefault(relationship.related_spdx_element, []).append(
                files_by_spdx_id[relationship.spdx_element_id])
            if relationship.has_comment:
                relationships_to_write.append(relationship)
        else:
            relationships_to_write.append(relationship)

    return relationships_to_write, contained_files_by_package_id


def determine_files_containing_snippets(snippets: List[Snippet], files: List[File]) -> Dict:
    contained_snippets_by_file_id = dict()
    for snippet in snippets:
        if snippet.file_spdx_id in [file.spdx_id for file in files]:
            contained_snippets_by_file_id.setdefault(snippet.file_spdx_id, []).append(snippet)

    return contained_snippets_by_file_id
