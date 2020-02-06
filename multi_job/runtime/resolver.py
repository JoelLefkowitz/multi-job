from typing import List, Mapping, Tuple

from multi_job.models.jobs import Job
from multi_job.models.processes import Process
from multi_job.models.projects import Project
from multi_job.models.routines import Routine
from multi_job.utils.strings import has_prefix
from multi_job.utils.tags import is_tagged, strip_tags


def resolve(
    jobs: List[Job],
    projects: List[Project],
    routines: List[Routine],
    cli_params: dict,
    config_path: str,
) -> Tuple[List[Process], Mapping[str, bool]]:
    choice, overrides, options = parse_cli_params(cli_params)
    chosen_jobs = resolve_job_matches(choice, jobs, routines)
    processes = [
        job.resolve_process(target, overrides, config_path)
        for job in chosen_jobs
        for target in job.resolve_targets(projects)
    ]
    return processes, options


def parse_cli_params(cli_params) -> Tuple[str, dict, dict]:
    choice = [
        k
        for k, v in cli_params.items()
        if not is_tagged(k) and not has_prefix(k, "--") and v
    ].pop()
    overrides = {strip_tags(k): v for k, v in cli_params.items() if is_tagged(k)}
    options = {k[2:]: v for k, v in cli_params.items() if has_prefix(k, "--")}
    return choice, overrides, options


def resolve_job_matches(
    choice: str, jobs: List[Job], routines: List[Routine]
) -> List[Job]:
    chosen_routine = next(
        (routine for routine in routines if routine.name == choice), None
    )
    chosen_jobs = [
        job
        for job in jobs
        if chosen_routine and job.name in chosen_routine.jobs or job.name == choice
    ]
    return chosen_jobs
