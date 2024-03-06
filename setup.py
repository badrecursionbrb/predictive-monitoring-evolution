from setuptools import setup, find_packages

setup(
    name='predictive monitoring evolution',
    version='0.1.0',
    description='replication of the predictive monitoring evolution paper',
    author='Group 3 - Advanced Process Mining',
    url='https://github.com/badrecursionbrb/predictive-monitoring-evolution.git',
    packages=find_packages(),
    install_requires=[
        'scikit-learn',
        'numpy',
        'pandas',
        'scipy',
        'matplotlib',
        'seaborn'
    ]
)