# Multi-job

Job runner for multifaceted projects

## Status

| Source  | Shields  |
|-----|--------------|
| Project  | ![license][license] ![release][release]  |
| Publishers  | [![pypi][pypi]][pypi_link]    |
| Downloads  | ![pypi_downloads][pypi_downloads] |
| Raised  | [![issues][issues]][issues_link] [![pulls][pulls]][pulls_link]  |

[license]: https://img.shields.io/github/license/joellefkowitz/multi-job

[release]: https://img.shields.io/github/v/tag/joellefkowitz/multi-job

[pypi]: https://img.shields.io/pypi/v/multi-job (PyPi)
[pypi_link]: https://pypi.org/project/multi-job

[python_version]: https://img.shields.io/pypi/pyversions/multi-job

[pypi_downloads]: https://img.shields.io/pypi/dw/multi-job

[issues]: https://img.shields.io/github/issues/joellefkowitz/multi-job (Issues)
[issues_link]: https://github.com/JoelLefkowitz/multi-job/issues

[pulls]: https://img.shields.io/github/issues-pr/joellefkowitz/multi-job (Pull requests)
[pulls_link]: https://github.com/JoelLefkowitz/multi-job/pulls  

## Motivation

Configuring scripts to run accross multiple directories should be as easy as writting a yaml file:


```yml
jobs:
  lint:
    command: "prettier ."
    targets: "all"

projects:
  app:
    path: "./app"

  server:
    path: "./server"

```

Moreover it should be easy to configure default arguments per job and project, allow jobs to specify to skip projects let python functions be used for jobs and allow routines of jobs to be defined:

```yml
jobs:
  lint:
    command: "prettier . --ignore-path <linter-regex>"
    context:
      linter-regex: "*.ts"
  format:
    function: "./server/management:main"
    skips:
      - "app"

projects:
  app:
    path: "app/src"
    context:
      linter-regex: "*.js"

  server:
    path: "server/src"

routines:
  dev:
    - lint
    - format

```

Finally automatic cli generation tools shouldn't need separate configuration

```bash
$ multi-job src/config.yml

Usage:
    multi-job <config_path> [options] lint [<linter-regex>]
    multi-job <config_path> [options] format
    multi-job <config_path> [options] dev
```

```bash
$ multi-job src/config.yml lint --check

⚡ Multi Job ⚡
Plan:
Job: lint, project: Local
```

```bash
$ multi-job src/config.yml lint --check --verbose

⚡ Multi Job ⚡
Plan:
['prettier', '.', '--ignore-path', '']
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
python setup.py test
```

### What is being tested

Multi-job is behaviour driven. Every desired behaviour and every validation rule has a test.

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

* **Joel Lefkowitz** - *Initial work* - [JoelLefkowitz](https://github.com/JoelLefkowitz)

See also the list of contributors who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file. for details

## Acknowledgments

None yet!

