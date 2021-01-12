from sys import argv
from typing import List
from typing import Mapping
from typing import Tuple

from art import text2art
from docopt import docopt

from multi_job.models.jobs import Job
from multi_job.models.processes import Process
from multi_job.models.projects import Project
from multi_job.models.routines import Routine
from multi_job.utils.strings import has_prefix
from multi_job.utils.tags import is_tagged
from multi_job.utils.tags import strip_tags


def interface_factory(
    jobs: List[Job], projects: List[Project], routines: List[Routine]
) -> str:

    job_names = [job.name for job in jobs]
    routine_names = [routine.name for routine in routines]

    uses = [
        f"{job.name} [{' '.join([f'<{p}>' for p in job.context])}]"
        if job.context
        else job.name
        for job in jobs
    ] + [routine.name for routine in routines]

    options = ["quiet", "silent", "check", "verbose"]

    prefix = text2art("Multi job") + "\n\n".join(
        [
            list_display("Jobs", job_names),
            list_display("Routines", routine_names),
            list_display("Options", options, "--"),
        ]
    )
    docopt_interface = fmt_uses(uses) + "\n" + fmt_options(options)

    print(prefix, end="\n\n")
    return docopt(docopt_interface)


def list_display(title: str, items: List[str], prefix: str = "") -> str:
    items = items or ["None"]
    return f"{title}:\n" + "\n".join([f"  {prefix}{i}" for i in items])


def fmt_uses(uses):
    lines = [f"    {argv[0]} <config_path> [options] " + l for l in uses]
    return "Usage:\n" + "\n".join(lines)


def fmt_options(options):
    lines = [f"    --{opt}" for opt in options]
    return "\n" + "\n".join(lines)




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
