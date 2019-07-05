# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

__version__ = '0.0.3'

packages = [
    'pylibmodbus',
]

setup(
    name='pylibmodbus-mkat',
    version=__version__,
    description="Python wrapper for libmodbus (fork for MeerKAT support).",
    long_description=open('README.rst').read(),
    author="SARAO MeerKAT Software Team",
    author_email="software@ska.ac.za",
    url="http://libmodbus.org",
    keywords="python libmodbus",
    packages=packages,
    package_data={'': ['LICENSE']},
    include_package_data=True,
    install_requires=['cffi>=0.6'],
    license=open('LICENSE').read(),
    zip_safe=False,
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ),
)
