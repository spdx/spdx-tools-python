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
from typing import TextIO

from src.datetime_conversions import datetime_to_iso_string
from src.model.annotation import Annotation
from src.writer.tagvalue.tagvalue_writer_helper_functions import write_value, write_text_value


def write_annotation(annotation: Annotation, text_output: TextIO):
    """
    Write the fields of a single annotation to text_output.
    """
    write_value("Annotator", annotation.annotator.to_serialized_string(), text_output)
    write_value("AnnotationDate", datetime_to_iso_string(annotation.annotation_date), text_output)
    write_text_value("AnnotationComment", annotation.annotation_comment, text_output, True)
    write_value("AnnotationType", annotation.annotation_type.name, text_output)
    write_value("SPDXREF", annotation.spdx_id, text_output, True)
