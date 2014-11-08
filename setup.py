#!/usr/bin/env python
from setuptools import setup, find_packages
from sys import exit

long_description = open('README').read()

setup(
    name='tab',
    version='1.0',
    description='Opens a new OS X Terminal window in the current directory and '
        'runs an optional command in it.',
    long_description=long_description,
    author='Martin Mahner',
    author_email='martin@mahner.org',
    url='https://github.com/bartTC/tab/',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Mac OS X',
        'Programming Language :: Python',
    ],
    packages=find_packages(),
    scripts=['tab'],
    include_package_data=True,

)
