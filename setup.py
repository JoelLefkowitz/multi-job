from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

s = setup(
    name="multi-job",
    version="0.9.22",
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
    ],
    entry_points={"console_scripts": ["multi-job=multi_job.main:entrypoint"]},
    python_requires=">= 3.6",
    author="Joel Lefkowitz",
    author_email="joellefkowitz@hotmail.com",
)
