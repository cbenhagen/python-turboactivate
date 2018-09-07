#!/usr/bin/env python

from distutils.core import setup

setup(name="turboactivate",
      version="4.1.0",
      description="Python bindings for TurboActivate",
      url="https://github.com/wyattoday/python-turboactivate",
      author="Develer S.r.L",
      author_email="info@develer.com",
      maintainer="wyDay, LLC",
      maintainer_email="support@wyday.com",
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Topic :: Software Development :: Libraries :: Python Modules',
		  'Programming Language :: Python',
		  'Programming Language :: Python :: 2',
		  'Programming Language :: Python :: 3',
      ],
      packages=["turboactivate"],
      long_description=open("README.rst").read()
)
