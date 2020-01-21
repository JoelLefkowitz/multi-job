import os
import sys
import subprocess
from parser.utils import sub_to_exec
from typing import List, Mapping, Optional


class Base:
    
    def __init__(self, name: str, config_path: str) -> None:
        self.name = name
        self.config_path

    def __str__(self) -> str:
        return f"{type(self)}: {self.name}"


class Subprocess(Base):
    def __init__(self, call: List[str], cwd: str = None, check: bool = False, quiet: bool = False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.call = call
        self.cwd = cwd
        self.check = check
        self.quiet = quiet

    def run(self) -> Optional[str]:
        if not self.quiet:
            print(f"Running: {self.call}")

        if not self.check:
            return subprocess.run(self.call, cwd=self.cwd)


class Job(Base):

    def __init__(self, command: str = None, function: str = None, parameters: List[Mapping[str, str]] = None,
                 targets: List[str] = None, skips: List[str] = None, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.command = command
        self.function = function
        self.parameters = parameters
        self.target = targets
        self.skips = skips
    
    # TODO Fix run
    def run(self, cli_params: List[Mapping[str, str]], project_params: List[Mapping[str, str]], project_path: str) ->  Subprocess:
        params = self.parameters.update(cli_params).update(project_params)
        if self.command:
            call = sub_to_exec(this.command, params)
        elif self.function:
            module_path = join_paths(self.config_path, self.function['path'])
            kwargs = ['{k}={v}' for (k, v) in params.items()].join(', ')
            call = f"getattr(__import__(rsplit({module_path}, '/', 1)), {self.function['name']})({kwargs})"
        return Subprocess(call, cwd=join_paths(self.config_path, project_path), check=cli_params['check'], quiet=cli_params['quiet'])


class Project(Base):
    def __init__(
        self,
        path: str,
        params: Mapping[str, dict] = None,
        target_by: List[str] = None,
        skip_by: List[str] = None,
    ) -> None:
        super().__init__(*args, **kwargs)
        self.path = path
        self.params = params
        self.target_by = target_by
        self.skip_by = skip_by
