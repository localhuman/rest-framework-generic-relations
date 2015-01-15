#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


version = '0.3.1'

install_requires = [
    'djangorestframework>=3.0.0',
]


setup(
    name='rest-framework-generic-relations-localhuman-fork',
    version=version,
    url='https://github.com/localhuman/rest-framework-generic-relations',
    license='BSD',
    description='Generic Relations for Django Rest Framework - localhuman-fork',
    author='localhuman',
    author_email='python@ian.feete.org',
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
)
