# coding=utf-8
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='banko',
    version='0.1.0',
    download_url='https://github.com/skipperkongen/banko/archive/refs/tags/v0.1.0.tar.gz',
    author="Pimin Konstantin Kefaloukos",
    author_email="skipperkongen@gmail.com",
    description="Library for generating banko plates",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/skipperkongen/banko",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
