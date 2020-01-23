#!/usr/bin/env python3

from os import getcwd
from sys import argv
from parser.utils import join_paths
from parser.validation import validate
from parser.exceptions import ConfigNotGiven
from cli.interface import generate
from parser.factory import build
from docopt import docopt  # type: ignore
from cli.runner import resolve


def entrypoint():
    if len(argv) < 2:
        raise (ConfigNotGiven("You must supply a config path e.g. dev <config_path>"))
    config_path = join_paths(getcwd(), argv[1])
    main(config_path)


def main(config_path: str) -> None:
    tree = validate(config_path)
    jobs, projects, routines = build(tree, config_path)
    interface = generate(jobs, routines)
    cli_params = docopt(interface)
    resolve(jobs, projects, routines, cli_params, config_path)


if __name__ == "__main__":
    entrypoint()
