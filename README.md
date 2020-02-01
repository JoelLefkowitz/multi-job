# Multi-job

Job runner for multifaceted projects

## Status

| Source  | Shields  |
|-----|--------------|
| Project  | ![license][license] ![release][release]  |
| Publishers  | [![pypi][pypi]][pypi_link]    |
| Downloads  | ![pypi_downloads][pypi_downloads] |
| Raised  | [![issues][issues]][issues_link] [![pulls][pulls]][pulls_link]  |

[license]: https://img.shields.io/github/license/joellefkowitz/dev

[release]: https://img.shields.io/github/v/release/joellefkowitz/dev

[pypi]: https://img.shields.io/pypi/v/dev (PyPi)
[pypi_link]: https://pypi.org/project/dev

[python_version]: https://img.shields.io/pypi/pyversions/dev

[pypi_downloads]: https://img.shields.io/pypi/dw/dev

[issues]: https://img.shields.io/github/issues/joellefkowitz/dev (Issues)
[issues_link]: https://github.com/JoelLefkowitz/dev/issues

[pulls]: https://img.shields.io/github/issues-pr/joellefkowitz/dev (Pull requests)
[pulls_link]: https://github.com/JoelLefkowitz/dev/pulls  

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
    command: "prettier . --ignore-path <regex>"
    params:
      regex: "*.ts"
  format:
    function:
      path: "./server/management"
      name: "main"
    skips:
      - "app"

projects:
  app:
    path: "./app"
    params: 
      lint:
        regex: "*.js"

  server:
    path: "./server"

routines:
  dev:
    - lint
    - format

```


Finally automatic cli generation tools shouldn't need separate configuration

```bash
$ multi-job ./config.yml

Usage:
  multi-job ./config.yml lint [regex] [-vcq]
  multi-job ./config.yml format [-vcq]
  multi-job ./config.yml all [-vcq]
Options:
  -h --help     Display this screen
  -v --verbose  Verbose output
  -c --check    Dry run
  -q --quiet    Silence output

$ multi-job ./config.yml lint --check --verbose

Checking job lint...
```


## Installing

Install from pypi:

```bash
pip install multi-job
```

## Running tests

Use pytest to invoke tests:

```bash
python -m pytest
```

### What is being tested

Multi-job is behaviour driven. Every desired behaviour and every validation rule has a test.

### Further docs

For full documentation visit our [wiki](https://github.com/JoelLefkowitz/multi-job/wiki).

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the tags on this repository.

## Author

* **Joel Lefkowitz** - *Initial work* - [JoelLefkowitz](https://github.com/JoelLefkowitz)

See also the list of contributors who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file. for details

## Acknowledgments

None yet!
