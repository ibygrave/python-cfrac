#!/usr/bin/env python

import setuptools

setuptools.setup(name='cfrac',
      version='1.0',
      description='Continue Fractions',
      author='Ian Bygrave',
      author_email='ian@bygrave.me.uk',
      packages=['cfrac'],
      package_dir={'cfrac':'src'},
      install_requires=[
          ],
      entry_points = {
          'console_scripts': [
          ]
          },
      )
