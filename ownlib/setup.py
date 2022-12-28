from setuptools import find_packages, setup
setup(
    name='mypack',
    packages=find_packages(include=['mypack']),
    version='1.0',
    description='My first Python library',
    author='StepUp',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner', 'wheel'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)