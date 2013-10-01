# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import sys, os

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src') )
from gmaps import __version__ as version

def strip_comments(l):
    return l.split('#', 1)[0].strip()

def reqs(*f):
    return list(filter(None, [strip_comments(l) for l in open(
        os.path.join(os.getcwd(), *f)).readlines()]))

install_requires = reqs('requirements.txt')

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