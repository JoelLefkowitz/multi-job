from setuptools import setup, find_packages

with open("README", 'r') as f:
    long_description = f.read()

s = setup(
    name="dev",
    version="1.0.0",
    license="MIT",
    description="Job runner",
    long_description=long_description,
    url='https://github.com/JoelLefkowitz/dev",
    packages=find_packages(),
    install_requires=['ruamel', 'numpy', 'docopts'],
    scripts=['scripts/main'],
    python_requires=">= 3.7",
    author="Joel Lefkowitz",
    author_email="joellefkowitz@hotmail.com",
    )
