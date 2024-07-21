from setuptools import setup, find_packages

setup(
    name='onet-data-collector',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'pandas'
    ],
    entry_points={
        'console_scripts': [
            'keyword_search=onet_data_collector.keyword_search:main',
            'fetch_job_details=onet_data_collector.fetch_job_details:main',
            'full_details=onet_data_collector.full_details:main',
        ],
    },
)
