#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

Setup script for dynamicalab
You can install dynamicalab with
`python setup.py install`
/

"""

from glob import glob
import os
import sys
if os.path.exists('MANIFEST'):
    os.remove('MANIFEST')

from setuptools import setup

if sys.argv[-1] == 'setup.py':
    print("To install, run 'python setup.py install'")
    print()

if sys.version_info[:2] < (2, 7):
    print("Resilience requires Python 2.7 or later (%d.%d detected)." %
          sys.version_info[:2])
    sys.exit(-1)

# Write the version information.
sys.path.insert(0, 'dynamicalab')

sys.path.pop(0)

packages = ["dynamicalab",
            "dynamicalab.algorithms",
            "dynamicalab.classes",
            "dynamicalab.generators",
            "dynamicalab.drawing",
            "dynamicalab.tests",
            "dynamicalab.utils"]


extras_require = {'all': ['numpy', 'scipy',  'matplotlib', 'networkx']}

if __name__ == "__main__":

    setup(
        name="dynamicalab",
        version="0.0",
        author="Dynamica Research Group",
        author_email="edward.laurence.1@ulaval.ca",
        description="Python module to study complex networks",
        packages=packages,
        extras_require=extras_require
    )











