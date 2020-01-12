import cli
import parser
from models import Script, Job
from docopt import docopt


def main(path="config.yml"):
    scripts, jobs, projects = parser.main(path)
    interface = cli.main(scripts, jobs)
    arguments = docopt(interface)

    check, quiet, = arguments["--check"], arguments["--quiet"]
    task = [i for i in scripts + jobs if arguments[i.name]].pop()
    task.params = {
        k: arguments[f"<{k}>"] if arguments[f"<{k}>"] else v
        for (k, v) in task.params.items()
    }

    if isinstance(task, Job):
        for p in projects:
            if (
                (not task.targets or p.name in task.targets)
                and (not task.skips or p not in task.skips)
                and (not p.target_by or task.name in p.target_by)
                and (not p.skip_by or task.name not in p.skip_by)
            ):
                params_copy = task.params.copy()
                task.params = {
                    k: p.params[k] if p.params and p.params[k] else v
                    for (k, v) in task.params.items()
                }
                task.run(check, quiet, p)
                task.params = params_copy

    elif isinstance(task, Script):
        task.run(check, quiet)


if __name__ == "__main__":
    main(path="./example.yml")
