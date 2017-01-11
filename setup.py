#!/usr/bin/env python

#from distutils.core import setup
from setuptools import setup

setup(name='pandoc-shortcaption',
      version='1.1',
      description='Pandoc Filter that uses the alt-text of an image' +
      'as short caption when converting to LaTeX',
      author='Martin Isaksson',
      author_email='martin@martisak.com',
      url='https://www.python.org/sigs/distutils-sig/',
      license='GPL',
      keywords='pandoc image caption latex filter',
      install_requires=[
          'pandocfilters'
      ],
      classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python'
      ],
      packages = ['pandoc_shortcaption'],
      entry_points={
          'console_scripts': [
              'pandoc-shortcaption = pandoc_shortcaption.__main__:main'
          ]
      },
)