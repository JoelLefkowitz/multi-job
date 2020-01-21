import os
import sys
from docopt import docopt # type: ignore
from typing import List
from parser.models import Job, Project

#TODO Write generate
def generate(jobs: List[Job]) -> str:
    return "Usage:"

#     interface = 
#     exec_path = " ".join(sys.argv[:2])
#     for name, params in [(i.name, i.params) for i in scripts + jobs]:
#         interface += f"\n {exec_path} {name} {fmt(params) if params else ''} [--quiet --check]"
#     return interface


# def fmt(params):
#     return " ".join(
#         sorted([f"[<{i}>]" if params[i] else f"<{i}>" for i in params.keys()])
#     )


# def main(
#     config_path=sys.argv[1],
#     working_path=os.path.realpath(""),
#     exec_path=sys.argv[0],
# ):

#     abs_config_path = join_paths(working_path, config_path)
#     scripts, jobs, projects = parse(abs_config_path)
#     interface = generate(scripts, jobs)
#     arguments = docopt(interface)

#     # TODO Check this doesn't break when an argument matches a job name
#     check, quiet, = arguments["--check"], arguments["--quiet"]
#     task = [i for i in scripts + jobs if arguments[i.name]].pop()
#     if task.params:
#         task.params = override(task.params, arguments, lambda x: f"<{x}>")

#     if isinstance(task, Job):
#         for project in [p for p in projects if compatable(task, p)]:
#             params_copy = task.params.copy() if task.params else None
#             if project.params:
#                 task.params = override(task.params, project.params)

#             task.run(check, quiet, project.path)
#             task.params = params_copy

#     elif isinstance(task, Script):
#         task.run(check, quiet)

