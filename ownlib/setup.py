from setuptools import find_packages, setup
setup(
    name='mystepuppack',
    packages=find_packages(include=['mystepuppack']),
    version='3.0',
    description='My first Python library',
    author='StepUp',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner', 'wheel'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)