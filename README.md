Python SPDX Parser Library.
===========================

Official repository: http://git.spdx.org/?p=spdx-tools-python.git

GitHub mirror: https://github.com/ah450/sdpx-tools-python

This library provides an implementation of a tag/value and RDF SPDX parser in python.

Expected Features:
==================
* API for creating and manipulating SPDX documents.
* Parse Tag/Value format SPDX files
* Parse RDF format SPDX files
* Create Tag/Value files.
* Create RDF files.

Current Status:
===============
* RDF Parser implemented.
* Tag/value parser implemented
* Tag/value writer implemented.
* RDF/Writer implemented.


How to use:
===========
Sample Tag/Value parsing Usage:
```Python
    from spdx.parsers.tagvalue import Parser
    from spdx.parsers.tagvaluebuilders import Builder
    from spdx.parsers.loggers import StandardLogger
    p = Parser(Builder(), StandardLogger())
    p.build()
    # data is a string containing the SPDX file.
    document, error = p.parse(data)

```

See `parse_tv.py` in the `examples` directory.

Try running `python parse_tv.py 'data/SPDXSimpleTag.tag' `

The file `write_tv.py` provides an example of writing tag/value files.

Run `python write_tv.py sample.tag` to test it.

The file `pp_tv.py` demonstrates how to pretty-print a tag/value file.
To test it run `python pp_tv.py data/SPDXTagExample.tag pretty.tag`.

The file `parse_rdf.py` demonstrates how to parse an RDF file and print out
document information.
To test it run `python parse_rdf.py data/SPDXRdfExample.rdf`

The file `rdf_to_tv.py` demonstrates how to convert an RDF file to a tag/value one.
To test it run `python rdf_to_tv.py data/SPDXRdfExample.rdf converted.tag`

The file `pp_rdf.py` demonstrates how to pretty-print an RDF file,
to test it run `python pp_rdf.py data/SPDXRdfExample.rdf pretty.rdf`

Installation:
=============
Clone the repository and run `python setup.py install`
on windows the command should be `setup.py install`

How to run tests:
=================
From the project root directory.

run: `nosetests`

Dependencies:
=============
nose : https://pypi.python.org/pypi/nose/1.3.3

PLY : https://pypi.python.org/pypi/ply/3.4

rdflib : https://pypi.python.org/pypi/rdflib/4.1.2
