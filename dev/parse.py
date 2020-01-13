import re
from ruamel import yaml
from numpy import concatenate
from dev.utils import remove_chars
from dev.models import Script, Job, Project
from dev.exceptions import ParserValidationError


def parse(path):
    with open(path, "r") as stream:
        config = yaml.load(stream, Loader=yaml.Loader)

    pre_parse_checks(config)
    scripts = config_factory(Script, "scripts", config)
    jobs = config_factory(Job, "jobs", config)
    projects = config_factory(Project, "projects", config)

    post_parse_checks(scripts, jobs, projects)
    return scripts, jobs, projects


def config_factory(cls, tag, config):
    return (
        [cls(**{**obj, "name": name}) for name, obj in config[tag].items()]
        if tag in config.keys()
        else []
    )


def pre_parse_checks(config):
    if not all(k in ["scripts", "jobs", "projects"] for k in [*config]):
        msg = f"Top level keys must only be scripts, jobs or projects"
        raise ParserValidationError(msg)

    if not all(concatenate([[v for v in k.values()] for k in config.values()])):
        raise ParserValidationError("Scripts, jobs and projects must not be empty")


def post_parse_checks(scripts, jobs, projects):
    names_list = [i.name for i in scripts + jobs + projects]

    # TODO Evaluate if this is needed
    if len(names_list) != len(set(names_list)):
        issues = filter(lambda rec: names_list.count(rec) > 1, names_list)
        msg = f"Scripts, jobs and projects names must all be unique\nIssues: {issues}"
        raise ParserValidationError(msg)

    pathless = [p.name for p in projects if not p.path]
    if pathless:
        msg = f"All projects must have paths\nIssues: {pathless}"
        raise ParserValidationError(msg)

    execless = [i.name for i in jobs + scripts if not (i.path or i.command)]
    if execless:
        msg = f"Scripts and jobs must be have either a path or a command\nIssues: {execless}"
        raise ParserValidationError(msg)

    for j in jobs:
        refs = (j.skips or []) + (j.targets or [])
        unmatched_refs = [i for i in refs if i not in [p.name for p in projects]]
        if unmatched_refs:
            msg = f"Skips and targets keys must refer to valid project names\nIssues: {unmatched_refs}"
            raise ParserValidationError(msg)

    for p in projects:
        refs = (p.skip_by or []) + (p.target_by or [])
        unmatched_refs = [i for i in refs if i not in [x.name for x in jobs + scripts]]
        if unmatched_refs:
            msg = f"Skip by and target by  keysmust refer to valid job names\nIssues: {unmatched_refs}"
            raise ParserValidationError(msg)

    for cmd, params in [(i.command, i.params) for i in scripts + jobs if i.command]:
        regex = re.compile(r"(<.*?>)")
        cmd_params = [remove_chars(i, ["<", ">"]) for i in regex.findall(cmd)]
        mismatches = list(set(cmd_params) ^ set(params)) if cmd_params else None
        if mismatches:
            msg = f"Parameters defined for a command must be present in the command string\nIssues: {mismatches}"
            raise ParserValidationError(msg)

    for p in [p for p in projects if p.params]:
        for ref in p.params:
            job = next((x for x in jobs if x.name == ref), None)
            if not job:
                msg = f"Parameters defined for a project must reference the job they correspond to\nIssue: {ref} in {p}"
                raise ParserValidationError(msg)

            elif not p.params[ref].keys():
                msg = f"Parameters defined for a project must not be empty\nIssue: {ref} in {p}"
                raise ParserValidationError(msg)

            elif not all(i in job.params.keys() for i in p.params[ref].keys()):
                msg = f"Parameters defined for a project must match the names of the corresponding job's parameters\nIssue: {ref} in {p}"
                raise ParserValidationError(msg)

