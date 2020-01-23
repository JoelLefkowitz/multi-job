from typing import Any
from .models import Job, Project


def build(tree, config_path):
    jobs, projects = [], []
    for k, v in tree["jobs"].items():
        jobs.append(Job(name=k, config_path=config_path, **v))
    for k, v in tree["projects"].items():
        projects.append(Project(name=k, config_path=config_path, **v))
    return jobs, projects
