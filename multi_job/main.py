#!/usr/bin/env python3

"""
Entrypoint for multi-job
"""

from os import getcwd, path
from sys import argv

from multi_job.interface.interceptors import intercept
from multi_job.interface.interface import interface_factory
from multi_job.models.exceptions import ConfigNotGiven
from multi_job.models.jobs import Job
from multi_job.models.projects import Project
from multi_job.models.routines import Routine
from multi_job.runtime.resolver import resolve
from multi_job.runtime.runtime import run
from multi_job.utils.strings import join_paths
from multi_job.validation.validation import validate


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
    jobs = Job.from_config(config["jobs"]) if "jobs" in config else []
    projects = Project.from_config(config["projects"]) if "projects" in config else []
    routines = Routine.from_config(config["routines"]) if "routines" in config else []
    interface = interface_factory(jobs, projects, routines)
    cli_params = intercept(interface)
    processes, options = resolve(jobs, projects, routines, cli_params, config_path)
    run(processes, options)


if __name__ == "__main__":
    entrypoint()
