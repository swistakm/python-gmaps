# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os


def get_version(version_tuple):
    if not isinstance(version_tuple[-1], int):
        return '.'.join(map(str, version_tuple[:-1])) + version_tuple[-1]
    return '.'.join(map(str, version_tuple))


try:
    from pypandoc import convert

    def read_md(f):
        return convert(f, 'rst')

except ImportError:
    print(
        "warning: pypandoc module not found, could not convert Markdown to RST"
    )

    def read_md(f):
        return open(f, 'r').read()  # noqa

init = os.path.join(os.path.dirname(__file__), 'src', 'gmaps', '__init__.py')
version_line = list(filter(lambda l: l.startswith('VERSION'), open(init)))[0]
VERSION = get_version(eval(version_line.split('=')[-1]))

PACKAGES = find_packages('src')
PACKAGE_DIR = {'': 'src'}

setup(
    name='python-gmaps',
    version=VERSION,
    author='Michał Jaworski',
    author_email='swistakm@gmail.com',
    description='Google Maps API client',
    long_description=read_md('README.md'),

    packages=PACKAGES,
    package_dir=PACKAGE_DIR,

    url='https://github.com/swistakm/python-gmaps',
    include_package_data=True,
    install_requires=[
        'requests',
        'pytz',
    ],
    zip_safe=False,

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
