# !/usr/bin/env python

from setuptools import setup

setup(
    name='my-package',
    packages=['my_package',],
    version='0.0.0',
    description='My sample package',
    author='MA',
    setup_requires=["pytest-runner"],
    test_suite="tests",
    # license='',
    # author_email='',
    # url='',
    # keywords=[],
    # python_requires='>=3.8',
)
