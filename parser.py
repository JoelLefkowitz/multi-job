from ruamel import yaml
from models import Script, Job, Project


def main(path):
    with open(path, "r") as stream:
        config = yaml.load(stream, Loader=yaml.Loader)

    # Top level is only script, job or project
    pass

    # Scripts, jobs and projects must not be empty
    pass

    scripts = (
        [
            Script(**{**script, "name": name})
            for name, script in config["scripts"].items()
        ]
        if "scripts" in config.keys()
        else []
    )

    jobs = (
        [Job(**{**job, "name": name}) for name, job in config["jobs"].items()]
        if "jobs" in config.keys()
        else []
    )

    projects = (
        [
            Project(**{**project, "name": name})
            for name, project in config["projects"].items()
        ]
        if "projects" in config.keys()
        else []
    )

    # Scripts, jobs, projects and arguments must all be unique
    pass

    # Projects must have paths
    pass

    # Scripts and jobs must be have either a path or a command
    pass

    # Skips and targets must refer to valid project names
    pass

    # Skip by and target by must refer to valid job names
    pass

    # Parameters defined for a command must be present in the command string
    pass

    # Parameters defined for a project must be valid parameters
    pass

    return scripts, jobs, projects
