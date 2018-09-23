#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open("README.rst") as readme_file:
    readme = readme_file.read()

setup(
    name="poautofill",
    version="0.1.2",
    description="Autofill po files with automated translations.",
    long_description=readme,
    author="Julien Palard",
    author_email="julien@palard.fr",
    url="https://github.com/JulienPalard/poautofill",
    packages=["poautofill"],
    package_dir={"poautofill": "poautofill"},
    entry_points={"console_scripts": ["poautofill=poautofill.poautofill:fill_pos"]},
    include_package_data=True,
    install_requires=["polib", "requests", "click"],
    extras_require={"dev": ["black", "detox"]},
    license="MIT license",
    zip_safe=False,
    keywords="poautofill",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
)
