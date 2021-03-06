#!/usr/bin/env python

from setuptools import setup, find_packages

with open('fs/_version.py') as f:
    exec(f.read())

CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Topic :: System :: Filesystems',
]

with open('README.txt', 'r') as f:
    DESCRIPTION = f.read()

REQUIREMENTS = [
    "appdirs",
    "enum34",
    "pytz",
    "scandir",
    "setuptools",
    "six>=1.10.0",
]

setup(
    author="Will McGugan",
    author_email="will@willmcgugan.com",
    classifiers=CLASSIFIERS,
    description="Filesystem abstraction layer",
    install_requires=REQUIREMENTS,
    license="BSD",
    long_description=DESCRIPTION,
    name='fs',
    packages=find_packages(),
    platforms=['any'],
    test_suite="nose.collector",
    tests_require=['appdirs', 'mock', 'pytz', 'pyftpdlib'],
    url="http://pypi.python.org/pypi/fs/",
    version=__version__,
)
