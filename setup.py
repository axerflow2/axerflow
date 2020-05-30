import sys

from setuptools import setup

# Require pytest-runner only when running tests
pytest_runner = (['pytest-runner>=2.0,<3dev']
                 if any(arg in sys.argv for arg in ('pytest', 'test'))
                 else [])

setup_requires = pytest_runner

setup(
    name="axerflow",
    version="0.0.1",
    description="a minimal example package (pure python version)",
    author='The axerflow team',
    author_email='jornbowrl@gmail.com',
    license="MIT",
    url="https://github.com/axerflow/axerflow/",
    download_url="https://github.com/axerflow/axerflow/archive/0.0.1.zip",
    packages=['hello'],
    tests_require=['pytest'],
    setup_requires=setup_requires
)
