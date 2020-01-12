from ruamel import yaml
from models import Script, Job, Project


def main(path):
    with open(path, "r") as stream:
        config = yaml.load(stream, Loader=yaml.Loader)

    # Top level is only script, job or project
    pass

    # Scripts, jobs and projects must not be empty
    pass

    scripts = config_factory(Script, "scripts", config)
    jobs = config_factory(Job, "jobs", config)
    projects = config_factory(Project, "projects", config)

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


def config_factory(cls, tag, config):
    return (
        [
            cls(**{**obj, "name": name})
            for name, obj in config[tag].items()
        ]
        if tag in config.keys()
        else []
    )
