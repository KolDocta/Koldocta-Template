#!/usr/bin/env python
# -*- coding: utf-8; -*-
#
# This file is part of Superdesk.
#
# Copyright 2013, 2014, 2015 Sourcefabric z.u. and contributors.
#
# For the full copyright and license information, please see the
# AUTHORS and LICENSE files distributed with this source code, or
# at https://www.sourcefabric.org/superdesk/license


from setuptools import setup, find_packages
from pip.req import parse_requirements
from pip.download import PipSession
import os

SOURCE_FOLDER = 'project'
LONG_DESCRIPTION = open(os.path.join(SOURCE_FOLDER, 'README.rst')).read()
REQUIREMENTS = [str(ir.req) for ir in parse_requirements('server/requirements.txt', session=PipSession())
                if not (getattr(ir, 'link', False) or getattr(ir, 'url', False))]

setup(
    name='KolDocta Project Template',
    version='0.0.1',
    description='KolDocta Project Template',
    long_description=LONG_DESCRIPTION,
    author='Salton Massally',
    author_email='salton.massally@gmail.com',
    url='https://github.com/koldocta/koldocta-template',
    license='GPLv3',
    platforms=['any'],
    package_dir={'': SOURCE_FOLDER},
    packages=find_packages(SOURCE_FOLDER),
    install_requires=REQUIREMENTS,
    test_suite='nose.collector',
    tests_require=['nose'],
    scripts=['settings.py', 'run.py', 'wsgi.py', 'manage.py'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ]
)
