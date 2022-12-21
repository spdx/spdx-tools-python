#  Copyright (c) 2022 spdx contributors
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#      http://www.apache.org/licenses/LICENSE-2.0
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
from typing import Type, Any

from src.jsonschema.converter import TypedConverter
from src.jsonschema.json_property import JsonProperty
from src.jsonschema.relationship_properties import RelationshipProperty
from src.model.document import Document
from src.model.relationship import Relationship
from src.writer.casing_tools import snake_case_to_camel_case


class RelationshipConverter(TypedConverter[Relationship]):
    def json_property_name(self, relationship_property: RelationshipProperty) -> str:
        return snake_case_to_camel_case(relationship_property.name)

    def _get_property_value(self, relationship: Relationship, relationship_property: RelationshipProperty,
                            document: Document = None) -> Any:
        if relationship_property == RelationshipProperty.SPDX_ELEMENT_ID:
            return relationship.spdx_element_id
        elif relationship_property == RelationshipProperty.COMMENT:
            return relationship.comment
        elif relationship_property == RelationshipProperty.RELATED_SPDX_ELEMENT:
            return relationship.related_spdx_element_id
        elif relationship_property == RelationshipProperty.RELATIONSHIP_TYPE:
            return relationship.relationship_type.name

    def get_json_type(self) -> Type[JsonProperty]:
        return RelationshipProperty

    def get_data_model_type(self) -> Type[Relationship]:
        return Relationship
