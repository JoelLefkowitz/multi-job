# Multi-job

Job runner for multifaceted projects

## Status

| Source     | Shields                                                        |
| ---------- | -------------------------------------------------------------- |
| Project    | ![license][license] ![release][release]                        |
| Publishers | [![pypi][pypi]][pypi_link]                                     |
| Downloads  | ![pypi_downloads][pypi_downloads]                              |
| Raised     | [![issues][issues]][issues_link] [![pulls][pulls]][pulls_link] |

[license]: https://img.shields.io/github/license/joellefkowitz/multi-job
[release]: https://img.shields.io/github/v/tag/joellefkowitz/multi-job
[pypi]: https://img.shields.io/pypi/v/multi-job "PyPi"
[pypi_link]: https://pypi.org/project/multi-job
[python_version]: https://img.shields.io/pypi/pyversions/multi-job
[pypi_downloads]: https://img.shields.io/pypi/dw/multi-job
[issues]: https://img.shields.io/github/issues/joellefkowitz/multi-job "Issues"
[issues_link]: https://github.com/JoelLefkowitz/multi-job/issues
[pulls]: https://img.shields.io/github/issues-pr/joellefkowitz/multi-job "Pull requests"
[pulls_link]: https://github.com/JoelLefkowitz/multi-job/pulls

## Motivation

Configuring jobs to run accross multiple directories should be as easy as writting a yaml file:

```yml
jobs:
  fmt:
    function: dev_actions/fmt:main
    targets:
      - app
      - server

  lint:
    command: "pylint ."
    targets: all

  bump:
    command: "bumpversion <bump-type>"
    skips: app
    context:
      bump-type: patch

  boot:
    script: ../boot.bash

  clean:
    function: prod_actions/clean:main
    context:
      clean_dirs:
        - build
        - dist
        - multi_job.egg-info

  pypi-upload:
    function: prod_actions/pypi_upload:main
    context:
      release_type: patch
      twine_username: joellefkowitz

projects:
  app:
    path: ../app

  server:
    path: ../server
    context:
      bump-type: minor

  models:
    path: ../models

routines:
  dev:
    - fmt
    - lint
```

Additionally, automatic cli generation tools shouldn't need separate configuration:

```bash
multi-job config.yml

Usage:
    <Workspace> <config_path> [options] fmt
    <Workspace> <config_path> [options] lint
    <Workspace> <config_path> [options] bump [<bump-type>]
    <Workspace> <config_path> [options] boot
    <Workspace> <config_path> [options] clean [<clean_dirs>]
    <Workspace> <config_path> [options] pypi-upload [<release_type> <twine_username>]
    <Workspace> <config_path> [options] dev
```

## Usage

```bash
multi-job config.yml lint --check

⚡ Multi Job ⚡
Plan:
Job: lint, project: Local
```

## Installing

Install from pypi:

```bash
pip install multi-job
```

## Running tests

Tests are not included in the package build. Clone the repo to include all the source files.

To invoke tests:

```bash
python -m unittest
```

### What is being tested

Multi-job is behaviour driven. Desired model behaviours and validation rules are prescribed unittests.

## Docs

Docs are not included in the package build. Clone the repo to include all the source files.

Full documentation can be generated locally:

```bash
python setup.py docs
```

To view the generated docs visit ./build/sphinx/html/multi_job/docs/modules.html:

```bash
open -a "Google Chrome" ./build/sphinx/html/multi_job/docs/modules.html
```

## Development roadmap

- Finish writting validation functions &rarr; v0.11.0
- Write unittests &rarr; v0.12.0
- Fill in missing docstrings &rarr; v1.0.0

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the tags on this repository.

Bumpversion is used to version and tag changes.
For example:

```bash
bumpversion patch
```

Releases are made on every major change.

## Author

- **Joel Lefkowitz** - _Initial work_ - [JoelLefkowitz](https://github.com/JoelLefkowitz)

See also the list of contributors who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file. for details

## Acknowledgments

None yet!
