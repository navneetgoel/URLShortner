import codecs
from os import path
from setuptools import setup, find_packages

with open('requirements.txt') as reqs:
    install_requires = [line for line in reqs.read().split('\n') if (line and not line.startswith('--'))]
    print(install_requires)