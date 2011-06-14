#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from distutils.core import setup



if sys.argv[-1] == 'publish':
    os.system("python setup.py sdist upload")
    sys.exit()

with open('reqs.txt', 'r') as f:
    required = r.readlines()

if sys.version_info[:2] < (2,6):
    required.append('simplejson')

setup(
    name='readability',
    version='0.1.0',
    description='Python wrapper for the Readability API.',
    long_description=open('README.rst').read(),
    author='The Readability Team',
    author_email='feedback@readability.com',
    url='https://www.readability.com/publishers/api',
    packages= ['readability'],
    install_requires=required,
    license='MIT',
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        # 'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
    ),
)