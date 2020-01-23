from typing import List, Tuple
from .models import Job, Project, Routine


def build(tree, config_path) -> Tuple[List[Job], List[Project], List[Routine]]:
    jobs, projects, routines = [], [], []
    for k, v in tree["jobs"].items():
        jobs.append(Job(name=k, config_path=config_path, **v))
    for k, v in tree["projects"].items():
        projects.append(Project(name=k, config_path=config_path, **v))
    for k, v in tree["routines"].items():
        routines.append(Routine(name=k, config_path=config_path, **v))
    routines.append(
        Routine(name="all", config_path=None, jobs=[job.name for job in jobs])
    )
    return jobs, projects, routines
