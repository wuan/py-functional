#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='py-functional',
    packages=find_packages(),
    install_requires=[],
    tests_require=['pytest-cov', 'mock', 'assertpy'],
    version="0.0.1",
    description="Simple python framework wrapping generators into a Stream class for chained processing",
    author='Andreas Wuerl',
    author_email='andi@tryb.de',
    url='https://github.com/wuan/py-functional',
    license="Apache 2.0",
    platforms='OS Independent',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
)
