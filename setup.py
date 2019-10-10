#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

from setuptools import setup
import unittest


def test_suite():
    return unittest.TestLoader().discover('tests', pattern='test_*.py')

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='spdx-tools',
    version='0.6.1',
    description='SPDX parser and tools.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=[
        'spdx',
        'spdx.parsers',
        'spdx.parsers.lexers',
        'spdx.writers',
    ],
    include_package_data=True,
    zip_safe=False,
    test_suite='setup.test_suite',
    install_requires=[
        'ply',
        'rdflib',
        'six',
        'pyyaml',
        'xmltodict',
        'license-expression',
    ],
    entry_points={
        'console_scripts': [
            'spdx-tv2rdf = spdx.tv_to_rdf:main',
        ],
    },

    author='Ahmed H. Ismail',
    author_email='ahm3d.hisham@gmail.com',
    maintainer='Philippe Ombredanne, SPDX group at the Linux Foundation and others',
    maintainer_email='pombredanne@gmail.com',
    url='https://github.com/spdx/tools-python',
    license='Apache-2.0',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7'
    ]
)
