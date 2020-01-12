#!/usr/bin/env python3
import sys
import cli
import parser
from docopt import docopt
from utils import override
from models import Script, Job, compatable


def main(path):
    scripts, jobs, projects = parser.main(path)
    interface = cli.main(scripts, jobs)
    arguments = docopt(interface)

    check, quiet, = arguments["--check"], arguments["--quiet"]
    task = [i for i in scripts + jobs if arguments[i.name]].pop()
    task.params = override(task.params, arguments, lambda x: f"<{x}>")

    if isinstance(task, Job):
        for project in [p for p in projects if compatable(task, p)]:
            params_copy = task.params.copy()
            if project.params:
                task.params = override(task.params, project.params)

            task.run(check, quiet, project)
            task.params = params_copy

    elif isinstance(task, Script):
        task.run(check, quiet)


if __name__ == "__main__":
    main(sys.argv[1])
