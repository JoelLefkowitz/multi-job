from distutils.core import Command, setup
from unittest import TestLoader, TextTestRunner

from setuptools import find_packages, setup
from sphinx.setup_command import BuildDoc

__version__ = "0.10.4"


class DocsCommand(BuildDoc):
    description = "Generate build configuration and make docs"

    def initialize_options(self) -> None:
        """  
        Docs command override. Call the parent initializer then add version and config directory
        """
        super().initialize_options()
        self.version = __version__
        self.config_dir = "./multi_job/docs"


class TestsCommand(Command):
    description = "Discover and run tests"
    user_options = []

    def initialize_options(self) -> None:
        pass

    def finalize_options(self) -> None:
        pass

    def run(self) -> None:
        """
        Discover and run tests        
        """
        suite = TestLoader().discover("./multi_job/tests")
        TextTestRunner().run(suite)


with open("README.md", "r") as f:
    long_description = f.read()


s = setup(
    name="multi-job",
    version=__version__,
    license="MIT",
    description="Job runner for multifaceted projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JoelLefkowitz/multi-job",
    packages=find_packages(),
    install_requires=[
        "ruamel.yaml>=0.16.5",
        "dataclasses>=0.7",
        "emoji>=0.5.4",
        "docopts>=0.6.1",
        "paramiko>=2.7.1",
        "scp>=0.13.2",
        "Sphinx>=2.4.1"
    ],
    entry_points={"console_scripts": ["multi-job=multi_job.main:entrypoint"]},
    cmdclass={"docs": DocsCommand, "test": TestsCommand},
    python_requires=">= 3.6",
    author="Joel Lefkowitz",
    author_email="joellefkowitz@hotmail.com",
)
