import os
import sys
from docopt import docopt  # type: ignore
from typing import List
from parser.models import Job, Project, Routine


def generate(jobs: List[Job], routines: List[Routine]) -> str:
    options = ["help", "quiet", "check", "verbose"]
    job_strings = "\n".join(
        [
            fmt_line(
                f"{job.name} {' '.join([f'<{p}>' for p in job.params.keys()])}", options
            )
            if job.params
            else fmt_line(job.name, options)
            for job in jobs
        ]
    )
    routine_strings = "\n".join(
        [fmt_line(routine.name, options) for routine in routines]
    )
    option_strings = "\n".join([f"  -{option[0]} --{option}" for option in options])
    return "\n".join(
        ["Usage:", job_strings, routine_strings, "\nOptions:", option_strings]
    )


def fmt_line(string: str, options: List[str]) -> str:
    return (
        f"  dev <config_path> {string} [-{''.join([option[0] for option in options])}]"
    )
