import subprocess
from setuptools import find_packages, setup
from distutils.core import Command

__version__ = "0.10.13"

with open("README.md", "r") as f:
    long_description = f.read()


class UpdateDocs(Command):
    description = "Update build configuration using sphinx-apidoc"
    user_options = []

    def initialize_options(self) -> None:
        self.version = __version__

    def finalize_options(self) -> None:
        pass

    def run(self) -> None:
        subprocess.run(["sphinx-apidoc", "-o", "docs/", "src/", "tests/"])


class GenerateDocs(Command):
    description = "Generate docs using sphinx-autodoc"
    user_options = []

    def initialize_options(self) -> None:
        self.version = __version__

    def finalize_options(self) -> None:
        pass

    def run(self) -> None:
        subprocess.run(["sphinx-build", "docs/", "build/"])


s = setup(
    name="multi-job",
    version=__version__,
    license="MIT",
    description="Job runner for multifaceted projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JoelLefkowitz/multi-job",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "art>=4.5",
        "dataclasses>=0.7",
        "docopt>=0.6.2",
        "emoji>=0.5.4",
        "ruamel.yaml>=0.16.10",
    ],
    entry_points={"console_scripts": ["multi-job=multi_job.main:entrypoint"]},
    cmdclass={"updateDocs": UpdateDocs, "generateDocs": GenerateDocs},
    python_requires=">= 3.6",
    author="Joel Lefkowitz",
    author_email="joellefkowitz@hotmail.com",
)
