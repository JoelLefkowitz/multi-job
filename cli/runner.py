from typing import List, Optional, Mapping
from parser.models import Job, Project, Subprocess
from parser.utils import join_paths, remove_tags, sub_to_exec


def resolve(jobs: List[Job], projects: List[Project], cli_params: dict) -> None:
    plan = []
    project_dict = {project.name: project for project in projects}

    for job in jobs:
        if job.targets:
            targets = [project_dict[name] for name in job.targets]
        elif job.skips:
            targets = [project_dict[name] for name in project_dict.keys() - job.skips]
        else:
            targets = []

        for project in targets:
            plan.append(make_process(job, cli_params, project))

    if not cli_params["--quiet"]:
        print("Plan:")
        for process in plan:
            print("Run:", process)

    if not cli_params["--check"]:
        for process in plan:
            if not cli_params["--quiet"]:
                print("Running:", process)
            print(process.run())


def make_process(
    job: Job, cli_params: List[Mapping[str, str]], project: Optional[Project]
) -> Subprocess:

    if job.params:
        cli_params.update(job.params)
    if type(project.params) is dict and job.name in project.params.keys():
        cli_params.update(project.params[job.name])

    # TODO Check all parmas filled or raise exception

    if job.command:
        call = sub_to_exec(job.command, cli_params)
    elif job.function:
        module_path = join_paths(job.config_path, job.function["path"])
        kwargs = ", ".join(
            [
                f"{remove_tags(k)}={v}"
                for (k, v) in cli_params.items()
                if type(job.params) is dict and remove_tags(k) in job.params.keys()
            ]
        )
        call = f"getattr(__import__(rsplit({module_path}, '/', 1)), {job.function['name']})({kwargs})"

    return Subprocess(
        call,
        cwd=join_paths(project.config_path, project.path) if project else None,
        check=cli_params["--check"],
        quiet=cli_params["--quiet"],
    )
