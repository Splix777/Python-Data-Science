# setup.py

from setuptools import setup, find_packages

setup(
    name='ft_package',
    version='0.0.1',
    author='fsalazar',
    url='https://github.com/eagle/ft_package',
    author_email='fsalazar@42.fr',
    license='MIT',
    description='A sample test package',
    packages=find_packages(exclude=['tests']),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
    ],
)
