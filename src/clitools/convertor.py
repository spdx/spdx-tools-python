#!/usr/bin/env python3

# Copyright (c) 2020 Yash Varshney
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#    http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import sys
from typing import List

import click

from src.model.document import Document
from src.parser.parse_anything import parse_file
from src.validation.document_validator import validate_full_spdx_document
from src.validation.validation_message import ValidationMessage
from src.writer.tagvalue import tagvalue_writer
from src.writer.write_anything import write_file


@click.command()
@click.option("--infile", "-i", prompt="input file path", help="The file containing the document to be validated or converted.")
@click.option("--outfile", "-o", help="The file to write the converted document to (write a dash for output to stdout or omit for no conversion).")
@click.option("--version", help='The SPDX version to be used during parsing and validation (format "SPDX-2.3").', default="SPDX-2.3")
@click.option("--novalidation", is_flag=True, help="Don't validate the provided document.")
def main(infile: str, outfile: str, version: str, novalidation: bool):
    """
    CLI-tool for validating SPDX documents and converting between RDF, TAG-VALUE, JSON, YAML and XML formats.
    Formats are determined by the file endings.
    To use, run: 'pyspdxtools_convertor --infile <input file name> --outfile <output file name>'
    """
    try:
        document: Document = parse_file(infile)

        if outfile == "-":
            tagvalue_writer.write_document(document, sys.stdout)
            print("")

        if not novalidation:
            validation_messages: List[ValidationMessage] = validate_full_spdx_document(document, version)
            if validation_messages:
                print("The document is invalid. The following issues have been found:")
                for message in validation_messages:
                    print(message.validation_message)
                sys.exit(1)
            else:
                print("The document is valid.")

        if outfile and outfile != "-":
            write_file(document, outfile, validate=False)

    except NotImplementedError as err:
        print(err.args[0])
        print("Please note that this project is currently undergoing a major refactoring and therefore missing "
              "a few features which will be added in time (refer to https://github.com/spdx/tools-python/issues "
              "for insights into the current status).\n"
              "In the meantime, please use the PyPI release version 0.7.0.")
        sys.exit(1)


if __name__ == "__main__":
    main()
