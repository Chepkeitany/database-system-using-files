from setuptools import setup
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = ["tests/"]

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import sys, pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(
    name='Simple Database System using Files',
    version='0.0.1',
    description="Simple Database System using Files",
    author='Anne Chepkeitany',
    packages=['simple_database'],
    maintainer='Anne Chepkeitany',
    tests_require=[
        'pytest==2.9.1'
    ],
    zip_safe=False,
    cmdclass={'test': PyTest},
)
