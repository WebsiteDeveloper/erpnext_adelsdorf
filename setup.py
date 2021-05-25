# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

setup(
	name='erpnext-adelsdorf',
	version="0.0.1",
	description='This creates erpnext-adelsdorf',
	author='K&K Software AG',
	author_email='teamx@kk-software.de',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
