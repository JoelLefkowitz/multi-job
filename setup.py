from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

s = setup(
    name="multi-job",
    version="0.7.5",
    license="MIT",
    description="Job runner for multifaceted projects",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JoelLefkowitz/multi-job",
    packages=find_packages(),
    install_requires=["ruamel.yaml>=0.16.5", "docopts>=0.6.1", "dataclasses>=0.7", "emoji>=0.5.4"],
    entry_points={"console_scripts": ["multi-job=main.main:entrypoint"]},
    python_requires=">= 3.6",
    author="Joel Lefkowitz",
    author_email="joellefkowitz@hotmail.com",
)
