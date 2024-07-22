from setuptools import setup, find_packages

setup(
    name='onet_data_collector',
    version='0.1.8',  # Update the version
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    package_data={
        '': ['*.py'],
    },
)
