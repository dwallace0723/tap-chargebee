#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='tap-chargebee',
      version='0.0.10',
      description='Singer.io tap for extracting data from the Chargebee API',
      author='dwallace@envoy.com',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['tap_chargebee'],
      install_requires=[
          'tap-framework==0.1.1'
      ],
      entry_points='''
          [console_scripts]
          tap-chargebee=tap_chargebee:main
      ''',
      packages=find_packages(),
      package_data={
          'tap_chargebee': [
              'schemas/*.json'
          ]
      })
