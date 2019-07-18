from setuptools import (setup, find_packages)
import os


def get_version():
    g = {}
    exec(open(os.path.join("statisfactory", "version.py")).read(), g)
    return g["__version__"]


setup(
    name='statisfactory',
    version=get_version(),
    packages=find_packages(exclude=["tests"]),
    description='',
    long_description='',
    url='https://giordonstark.com.com',
    author='Giordon Stark',
    author_email='gstark@cern.ch',
    license="BSD 3-clause",
    setup_requires=["pytest-runner", "flake8"],
    tests_require=["pytest"],
    classifiers=['Development Status :: 1 - Planning'],
)
