from typing import List

import sys; sys.path.append('..')
from models.jobs import Job
from models.projects import Project
from models.routines import Routine
from .formatters import fmt_options, fmt_uses


def interface_factory(
    jobs: List[Job], projects: List[Project], routines: List[Routine]
) -> str:

    uses = [
        f"{job.name} [{' '.join([f'<{p}>' for p in job.context])}]"
        if job.context
        else job.name
        for job in jobs
    ] + [routine.name for routine in routines]
    options = [("quiet", "f"), ("silent", "f"), ("check", "f"), ("verbose", "f")]
    return fmt_uses(uses) + "\n" + fmt_options(options)
