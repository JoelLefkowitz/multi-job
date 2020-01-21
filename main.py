from os import getcwd
from sys import argv
from parser.utils import join_paths
from parser.validation import validate
from parser.exceptions import ConfigNotGiven
from cli.interface import generate
from parser.factory import build
from docopt import docopt # type: ignore
from cli.runner import resolve


def main() -> None:
    input_args = docopt("Usage:\n  dev <config_path>")
    config_path = join_paths(getcwd(), input_args['<config_path>'])
    tree = validate(config_path)
    jobs, projects = build(tree)
    interface = generate(jobs)
    arguments = docopt(interface)
    resolve(jobs, projects, arguments)


if __name__ == "__main__":
    main()
