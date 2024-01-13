#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='tap-mavenlink',
      version='0.0.3',
      description='Singer.io tap for extracting data from the Mavenlink API',
      author='Fishtown Analytics',
      url='http://fishtownanalytics.com',
      classifiers=['Programming Language :: Python :: 3 :: Only'],
      py_modules=['tap_mavenlink'],
      install_requires=[
          'singer-python>=5.1.0,<5.14',
          'backoff>=1.3.2,<=1.8.0',
          'requests>=2.18.4,<=2.31',
          'requests-oauthlib>=0.8.0,<1.4',
          'funcy>=1.10.1,<1.19',
          'urllib3>=2'
      ],
      entry_points='''
          [console_scripts]
          tap-mavenlink=tap_mavenlink:main
      ''',
      packages=find_packages(),
      package_data={
          'tap_mavenlink': [
              'schemas/*.json'
          ]
      })
