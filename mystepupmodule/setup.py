
from setuptools import find_packages, setup
setup(
    name='mystepupmodule',
    packages=find_packages(include=['mystepupmodule']),
    version='1.0',
    description='My third Python library',
    author='Stepup',
    license='MIT',
    setup_requires=[ 'wheel']
)