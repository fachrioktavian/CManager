#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import (setup, find_packages)
from cmanager import (__version__, __author__, __author_email__)

setup(
    name="cmanager",
    packages=find_packages(),
    version=__version__,
    platforms=["Linux"],
    url='https://github.com/fachrioktavian/CManager/',
    download_url='https://github.com/fachrioktavian/CManager/tarball/v{}'.format(
        __version__),
    description="CLI (Command Line Interface) for DracOS Linux's users to manage their connection ex: wifi connection.",
    long_description=open("README.rst").read(),
    license="GPLv3",
    author=__author__,
    author_email=__author_email__,
    zip_safe=False,
    include_package_data=True,
    keywords=["cmanager", "dracos connection manager", "connection manager"],
    entry_points={
        "console_scripts": ["cmanager=cmanager.cmanager:main", ],
    },
    install_requires=[
        "colorama>=0.3.7", "terminaltables>=3.1.0",
        "pbkdf2>=1.3", "netifaces>=0.10.5",
        "python-wifi>=0.6.1"
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: POSIX :: Linux",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.5",
        "Topic :: System :: Networking",
        "Topic :: Internet",
        "Topic :: Utilities"
    ]
)
