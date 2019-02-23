from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from setuptools import setup

setup(
    name='rle',
    version='0.0.1',
    description='run length encoding functions for numpy/tensorflow',
    url='http://github.com/jackd/run_length_encoding',
    author='Dominic Jack',
    author_email='thedomjack@gmail.com',
    license='MIT',
    packages=['rle'],
    install_requires=['numpy'],
    zip_safe=True
)
