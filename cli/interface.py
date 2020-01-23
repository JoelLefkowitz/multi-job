import os
import sys
from docopt import docopt  # type: ignore
from typing import List
from parser.models import Job, Project


def generate(jobs: List[Job]) -> str:
    job_strings = [
        f"  dev <config_path> {job.name} {' '.join([f'<{p}>' for p in job.params.keys()])}  [--quiet] [--check]"
        if job.params
        else f"  dev <config_path> {job.name}  [--quiet] [--check]"
        for job in jobs
    ]
    return "Usage:\n" + "\n".join(job_strings)
