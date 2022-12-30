from setuptools import find_packages, setup
setup(
    name='steplib',
    packages=find_packages(include=['stepuplib']),
    version='3.0',
    description='find sum of 3 numbers',
    author='stepup',
    license='MIT',
    install_requires=[],
    setup_requires=['wheel']
)