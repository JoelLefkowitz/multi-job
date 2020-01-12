import re
import subprocess


class Script:
    def __init__(self, name, path=None, command=None, params=None):
        self.name = name
        self.path = path
        self.params = params
        self.command = command

    def run(self, check, quiet):
        if self.command:
            cmd = re.sub(
                "<.+?>",
                lambda x: self.params[
                    x.group(0).translate(str.maketrans({"<": "", ">": ""}))
                ],
                self.command,
            )
            cmd = cmd.split(' ')
            if not quiet:
                print(f"Running command: {cmd}")
            if not check:
                subprocess.run(cmd, shell=False)
        elif self.path:
            if not quiet:
                print(f"Call {self.path} with {self.params}")
            if not check:
                module = __import__(self.path)
                getattr(module, 'main')(**self.params)


class Job(Script):
    def __init__(self, targets=None, skips=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.targets = targets
        self.skips = skips

    def run(self, check, quiet, project):
        if not quiet:
            print(f"Running in: {project.name}")
        super().run(check, quiet)


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
