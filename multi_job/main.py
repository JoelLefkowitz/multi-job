#!/usr/bin/env python3

"""
Entrypoint for multi-job
"""

import os, sys

package_directory = os.path.realpath(os.path.join(__file__, "../.."))
sys.path.append(package_directory)

from multi_job.interface.interface import interface_factory
from multi_job.models.exceptions import ConfigNotGiven
from multi_job.models.jobs import Job
from multi_job.models.projects import Project
from multi_job.models.routines import Routine
from multi_job.runtime.resolver import resolve
from multi_job.runtime.runtime import run
from multi_job.utils.strings import join_paths
from multi_job.validation.validate import validate


def entrypoint() -> None:
    """Assert that a resolvable configuration path is provided"""
    if len(sys.argv) < 2:
        raise (
            ConfigNotGiven(
                "You must supply a configuration path e.g. dev <config_path>"
            )
        )
    config_path = join_paths(os.getcwd(), sys.argv[1])
    if not os.path.exists(config_path):
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
    projects = (
        Project.from_config(config["projects"])
        if "projects" in config and config["projects"]
        else []
    )
    routines = (
        Routine.from_config(config["routines"])
        if "routines" in config and config["routines"]
        else []
    )
    cli_params = interface_factory(jobs, projects, routines)
    processes, options = resolve(jobs, projects, routines, cli_params, config_path)
    run(processes, options)


if __name__ == "__main__":
    entrypoint()
