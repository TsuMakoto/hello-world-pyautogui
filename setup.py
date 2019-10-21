# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='hello-world-pyautogui',
    version='0.1.0',
    description='Hello World with java which auto generated source code.',
    long_description=readme,
    author='TsuMakoto',
    url='https://github.com/TsuMakoto/hello-world-pyautogui',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

