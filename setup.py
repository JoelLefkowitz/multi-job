from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

s = setup(
    name="dev",
    version="0.3.12",
    license="MIT",
    description="Job runner",
    long_description=long_description,
    url="https://github.com/JoelLefkowitz/dev",
    packages=find_packages(),
    # install_requires=['ruamel.yaml>=16.5.0', 'numpy>=1.18.0', 'docopts>=0.6.11'],
    entry_points={"console_scripts": ["dev=dev.main:main"]},
    python_requires=">= 3.6",
    author="Joel Lefkowitz",
    author_email="joellefkowitz@hotmail.com",
)
