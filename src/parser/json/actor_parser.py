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
from typing import Union, Pattern, Match

from src.model.actor import Actor, ActorType
from src.model.spdx_no_assertion import SpdxNoAssertion
from src.model.typing.constructor_type_errors import ConstructorTypeErrors
from src.parser.error import SPDXParsingError


class ActorParser:
    def parse_actor_or_no_assertion(self, actor_or_no_assertion: str) -> Union[SpdxNoAssertion, Actor]:
        if actor_or_no_assertion == SpdxNoAssertion.__str__:
            return SpdxNoAssertion()
        else:
            return self.parse_actor(actor_or_no_assertion)

    @staticmethod
    def parse_actor(actor: str) -> Actor:
        tool_re: Pattern = re.compile(r"Tool:\s*(.+)", re.UNICODE)
        person_re: Pattern = re.compile(r"Person:\s*(([^(])+)(\((.*)\))?", re.UNICODE)
        org_re: Pattern = re.compile(r"Organization:\s*(([^(])+)(\((.*)\))?", re.UNICODE)
        tool_match: Match = tool_re.match(actor)
        person_match: Match = person_re.match(actor)
        org_match: Match = org_re.match(actor)

        if tool_match:
            name: str = tool_match.group(1).strip()
            try:
                creator = Actor(ActorType.TOOL, name=name)
            except ConstructorTypeErrors as err:
                raise SPDXParsingError(err.get_messages())
        elif person_match:
            name: str = person_match.group(1).strip()
            email: str = person_match.group(4).strip() if person_match.group(4) else None
            try:
                creator = Actor(ActorType.PERSON, name=name, email=email)
            except ConstructorTypeErrors as err:
                raise SPDXParsingError(err.get_messages())
        elif org_match:
            name: str = org_match.group(1).strip()
            email: str = org_match.group(4).strip() if org_match.group(4) else None
            try:
                creator = Actor(ActorType.ORGANIZATION, name=name, email=email)
            except ConstructorTypeErrors as err:
                raise SPDXParsingError(err.get_messages())

        else:
            raise SPDXParsingError([f"Actor {actor} doesn't match any of person, organization or tool."])

        return creator
