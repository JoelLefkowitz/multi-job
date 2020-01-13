import subprocess
from dev.utils import sub_to_exec


class Script:
    def __init__(self, name, path=None, command=None, params=None):
        self.name = name
        self.path = path
        self.params = params
        self.command = command

    def __str__(self):
        return f"Script: {self.name}"

    def run(self, check, quiet):
        if self.command:
            cmd = sub_to_exec(self.command, self.params)
            if not quiet:
                print(f"Running command: {cmd}")
            if not check:
                subprocess.run(cmd, shell=False)
        elif self.path:
            if not quiet:
                print(f"Calling {self.path} with {self.params or 'no parameters'}")
            if not check:
                module = __import__(self.path)
                getattr(module, "main")(**self.params)


class Job(Script):
    def __init__(self, targets=None, skips=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.targets = targets
        self.skips = skips

    def __str__(self):
        return f"Job: {self.name}"

    def run(self, check, quiet, path):
        if self.command:
            
            cmd = sub_to_exec(self.command, self.params)
            if not quiet:
                print(f"Running command: {cmd} in {path}")
            if not check:
                subprocess.run(cmd, shell=False, cwd=path)
        
        elif self.path:
            if not quiet:
                print(f"Calling {self.path} with path {path} and {self.params or 'no parameters'}")
            if not check:
                module = __import__(self.path)
                getattr(module, "main")(path, excludes, **self.params)


class Project:
    def __init__(
        self, name, path, params=None, excludes=None, target_by=None, skip_by=None
    ):
        self.name = name
        self.path = path
        self.params = params
        self.excludes = excludes
        self.target_by = target_by
        self.skip_by = skip_by

    def __str__(self):
        return f"Project: {self.name}"


def compatable(task, project):
    return (
        (not task.targets or project.name in task.targets)
        and (not task.skips or project not in task.skips)
        and (not project.target_by or task.name in project.target_by)
        and (not project.skip_by or task.name not in project.skip_by)
    )
