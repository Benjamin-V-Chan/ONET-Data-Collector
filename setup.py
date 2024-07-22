from setuptools import setup, find_packages

setup(
    name='onet-data-collector',
    version='0.1.1',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
)