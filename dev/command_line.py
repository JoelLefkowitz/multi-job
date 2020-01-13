import sys
from dev.parse import parse
from dev.cli import generate
from docopt import docopt
from dev.utils import override
from dev.models import Script, Job, compatable


def main(path=sys.argv[1]):
    print(sys.argv)
    scripts, jobs, projects = parse(path)
    interface = generate(scripts, jobs)
    arguments = docopt(interface)

    # TODO Check this doesn't break when an argument matches a job name
    check, quiet, = arguments["--check"], arguments["--quiet"]
    task = [i for i in scripts + jobs if arguments[i.name]].pop()
    if task.params:
        task.params = override(task.params, arguments, lambda x: f"<{x}>")

    if isinstance(task, Job):
        for project in [p for p in projects if compatable(task, p)]:
            params_copy = task.params.copy() if task.params else None
            if project.params:
                task.params = override(task.params, project.params)

            task.run(check, quiet, project.path)
            task.params = params_copy

    elif isinstance(task, Script):
        task.run(check, quiet)
