# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='pyeth_keys',
    version='1.1.0',
    description='Creating and reading keyfiles',
    long_description=readme,
    author='Vitalik Buterin',
    author_email='',
    url='https://github.com/ethereum/research',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=[
    ],
)
