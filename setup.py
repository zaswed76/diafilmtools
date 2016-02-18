# -*- coding: utf-8 -*-

from os.path import join, dirname

from setuptools import setup, find_packages

import diatools

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
                ['dia-min = diatools.dia_min:main',
                 'dia-show = diatools.dia_show:main',
                 'dia-replace = diatools.dia_replace:main'
                 ]
        }

)
