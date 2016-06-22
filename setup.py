#!/usr/bin/env python
# Copyright (c) 2016 Marco Giusti
# See LICENSE for details.


from setuptools import setup


def get_version(filename="nvd3.py", varname="__version__"):
    glb = {}
    with open(filename) as fp:
        for line in fp:
            if varname in line:
                exec(line, glb)
                break
    return glb[varname]


def readfile(filename):
    with open(filename) as fp:
        return fp.read()


setup(name="nvd3_py",
      version=get_version(),
      description="Build NVD3 charts from python",
      long_description=readfile("README.rst"),
      keywords="chart, charts, graph, nvd3, d3, html, javascript",
      author="Marco Giusti",
      author_email="marco.giusti@posteo.de",
      url="http://github.com/marcogiusti/nvd3_py",
      license="MIT",
      test_suite="test_nvd3",
      py_modules=["nvd3"],
      classifiers=[
          "Development Status :: 1 - Planning",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2",
          "Programming Language :: Python :: 2.7",
      ],
)
