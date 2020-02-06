#!/usr/bin/env python3

"""
Entrypoint for multi-job
"""

from os import getcwd, path
from sys import argv

from .interface.interceptors import intercept
from .interface.interface import interface_factory
from .models.exceptions import ConfigNotGiven
from .models.jobs import Job
from .models.projects import Project
from .models.routines import Routine
from .runtime.resolver import resolve
from .runtime.runtime import run
from .utils.strings import join_paths
from .validation.validation import validate


def entrypoint() -> None:
    """Assert that a resolvable configuration path is provided"""
    if len(argv) < 2:
        raise (
            ConfigNotGiven(
                "You must supply a configuration path e.g. dev <config_path>"
            )
        )
    config_path = join_paths(getcwd(), argv[1])
    if not path.exists(config_path):
        raise (ConfigNotGiven("You must supply a resolvable configuration path"))
    main(config_path)


def main(config_path: str) -> None:
    """
    Call the main parser and cli functions sequentially

    Args:
        config_path (str): path of the configuration file
    """
    config = validate(config_path)
    jobs = Job.from_config(config["jobs"])
    projects = Project.from_config(config["projects"])
    routines = Routine.from_config(config["routines"])
    interface = interface_factory(jobs, projects, routines)
    cli_params = intercept(interface)
    processes, options = resolve(jobs, projects, routines, cli_params, config_path)
    run(processes, options)


if __name__ == "__main__":
    entrypoint()
