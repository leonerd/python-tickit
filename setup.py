
from setuptools import setup

setup(
    name='python-tickit',
    version='0.1',
    description='Python bindings for libtickit',
    author='Kiyoshi Aman',
    author_email='kiyoshi.aman@gmail.com',
    test_suite='tickit.tests',
    packages=('tickit',),
)

