from setuptools import setup, find_packages
  
setup(
    name='merck_env',
    version='0.1.2',
    packages=find_packages(include=['merck_dna_project','merck_dna_project.*']),
    install_requires=[
        'pandas',
        'numpy',
        'scipy',
        'python-dateutil',
        'statistics',
        'tqdm',
        'awswrangler==2.4.0',
        'pandasql',
        'matplotlib',
	'fsspec',
	'smart-open',
	's3fs',
    ]
)
