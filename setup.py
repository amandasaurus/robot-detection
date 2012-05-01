#! /usr/bin/env python

from setuptools import setup, find_packages

setup(name="robot-detection",
      version="0.3",
      author="Rory McCann",
      author_email="rory@technomancy.org",
      py_modules=['robot_detection'],
      summary="Library for detecting if a HTTP User Agent header is likely to be a bot",
      description="Library for detecting if a HTTP User Agent header is likely to be a bot",
      url="http://www.celtic-knot-creator.com/robot-detection/",
      license="GPLv3+",
      classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Web Environment',
            'Intended Audience :: Developers',
            'Intended Audience :: System Administrators',
            'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Internet :: WWW/HTTP',
            'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries',
            'Topic :: Internet :: WWW/HTTP :: Site Management',
            'Topic :: Software Development :: Libraries :: Python Modules',
            ],
)
