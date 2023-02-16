#!/usr/bin/env python

from distutils.core import setup

setup(name='thesis',
      version='1.0',
      description='Thesis Project',
      author='Aybueke Ulusarslan',
      author_email='aybueke.ulusarslan@tum.de',
      url='TBD',
      packages=['thesis'],
      install_requires=[
          'numpy',
          'pandas',
          'jupyter',
          'matplotlib',
          'torch',
          'torchvision'
      ],
     )