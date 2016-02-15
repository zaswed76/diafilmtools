# -*- coding: utf-8 -*-

from os.path import join, dirname

import diatools
from setuptools import setup, find_packages

setup(
        name="program",
        version=diatools.__version__,
        packages=find_packages(
                exclude=["*.exemple", "*.exemple.*", "exemple.*",
                         "exemple"]),
        include_package_data=True,
        long_description=open(
                join(dirname(__file__), 'README.rst')).read(),
        install_requires=[],
        entry_points={
            'console_scripts':
                ['diatools-min = diatools.dia_min:main',
                 'diatools-show = diatools.display:main']
        }

)
