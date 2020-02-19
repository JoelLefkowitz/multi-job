from typing import List
from art import text2art
from docopt import docopt
from multi_job.models.jobs import Job
from multi_job.models.projects import Project
from multi_job.models.routines import Routine

from .formatters import fmt_options, fmt_uses


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
