from ruamel import yaml
from models import Script, Job, Project
from exceptions import ParserValidationError


def main(path):
    with open(path, "r") as stream:
        config = yaml.load(stream, Loader=yaml.Loader)

    # Top level is only script, job or project
    if False:
        raise ParserValidationError("")

    # Scripts, jobs and projects must not be empty
    if False:
        raise ParserValidationError("")

    scripts = config_factory(Script, "scripts", config)
    jobs = config_factory(Job, "jobs", config)
    projects = config_factory(Project, "projects", config)

    # Scripts, jobs, projects and arguments must all be unique
    if False:
        raise ParserValidationError("")

    # Projects must have paths
    if False:
        raise ParserValidationError("")

    # Scripts and jobs must be have either a path or a command
    if False:
        raise ParserValidationError("")

    # Skips and targets must refer to valid project names
    if False:
        raise ParserValidationError("")

    # Skip by and target by must refer to valid job names
    if False:
        raise ParserValidationError("")

    # Parameters defined for a command must be present in the command string
    if False:
        raise ParserValidationError("")

    # Parameters defined for a project must be valid parameters
    if False:
        raise ParserValidationError("")

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
