from setuptools import setup, find_packages

setup(
    name='onet-data-collector',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'keyword_search=onet_data_collector.keyword_search_script:main',
            'fetch_job_details=onet_data_collector.fetch_job_details_script:main',
            'full_details=onet_data_collector.full_details_script:main',
        ],
    },
)
