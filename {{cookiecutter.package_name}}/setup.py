#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script"""

from setuptools import setup, find_packages

setup(author="{{ cookiecutter.author_name }}",
      author_email='{{ cookiecutter.author_email }}',
      classifiers=[
          'Development Status :: 3 - Alpha',
           # 'Intended Audience :: Science/Research',
          'Natural Language :: English',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
      ],
      description='{{ cookiecutter.package_description }}',
      extras_require={
        "docs": ["nbsphinx", "sphinx-rtd-theme", "IPython"],
        "test": ["pytest"],
      },
      keywords=[],
      name='{{ cookiecutter.package_name }}',
      packages=find_packages(include=['{{ cookiecutter.package_name }}'], exclude=["demos", "tests", "docs"]),
      install_requires=[],
      url='{{ cookiecutter.package_url }}',
      version='{{ cookiecutter.package_version }}',

      )
