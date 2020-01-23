import os
import sys
import subprocess
from .utils import sub_to_exec
from typing import List, Mapping, Any
from .colours import green, blue


class Base:
    def __init__(self, name: str, config_path: str) -> None:
        self.name = name
        self.config_path = config_path

    def __str__(self) -> str:
        return f"{type(self)}: {self.name}"


class Subprocess:
    def __init__(
        self,
        call: List[str],
        cwd: str = None,
        description: str = None,
        *args,
        **kwargs,
    ) -> None:
        super().__init__(*args, **kwargs)
        self.call = call
        self.cwd = cwd
        self.description = description

    def fmt(self, verbose) -> str:
        if verbose:
            return green(f"{self.call} in {self.cwd}")
        else:
            return green(f"{self.description} in {self.cwd}")

    def run(self) -> Any:
        return subprocess.run(self.call, cwd=self.cwd)


class Job(Base):
    def __init__(
        self,
        command: str = None,
        function: str = None,
        params: List[Mapping[str, str]] = None,
        targets: List[str] = None,
        skips: List[str] = None,
        *args,
        **kwargs,
    ) -> None:
        super().__init__(*args, **kwargs)
        self.command = command
        self.function = function
        self.params = params
        self.targets = targets
        self.skips = skips


class Project(Base):
    def __init__(
        self, path: str, params: Mapping[str, dict] = None, *args, **kwargs,
    ) -> None:
        super().__init__(*args, **kwargs)
        self.path = path
        self.params = params


class Routine(Base):
    def __init__(self, jobs: Mapping[str, str] = None, *args, **kwargs,) -> None:
        super().__init__(*args, **kwargs)
        self.jobs = jobs
