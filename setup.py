# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os
import re


def strip_comments(l):
    return l.split('#', 1)[0].strip()


def reqs(*f):
    return list(filter(None, [strip_comments(l) for l in open(
        os.path.join(os.getcwd(), *f)).readlines()]))


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


install_requires = reqs('requirements.txt')
version = get_version('src/gmaps')
README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()
PACKAGES = find_packages('src')
PACKAGE_DIR = {'': 'src'}

setup(
    name='python-gmaps',
    version=version,
    author='Michał Jaworski',
    author_email='swistakm@gmail.com',
    description='Google Maps API client',
    long_description=README,

    packages=PACKAGES,
    package_dir=PACKAGE_DIR,

    include_package_data=True,
    install_requires=install_requires,
    zip_safe=False,

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],

)