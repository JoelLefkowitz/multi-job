"""
Project, Job, Routine and Subprocess classes
"""

import functools
from importlib import import_module
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from utils.tags import substitute_exec_form
from typing import List, Union, Callable
from models.projects import Project
from models.processes import CommandProcess, FunctionProcess

@dataclass
class Job(ABC):
    name: str
    context: dict = field(default_factory=dict)
    targets: Union[str, List[str]] = field(default_factory=list)
    skips: Union[str, List[str]] = field(default_factory=list)

    def resolve_targets(self, projects: List[Project]) -> List[Project]:
        matches = []
        if self.targets:
            matches = [
                p for p in projects if p.name in self.targets or self.targets == ["all"]
            ]
        elif self.skips:
            matches = [
                p
                for p in projects
                if not (p.name in self.skips or self.skips == ["all"])
            ]

        if not matches:
            local = Project(name="Local", path="..")
            matches.append(local)

        return matches

    def resolve_process(
        self, target: Project, context_overrides: dict, config_path: str
    ) -> Process:
        context = functools.reduce(
            lambda a, b: {**a, **b}, [self.context, context_overrides, target.context]
        )
        path = target.abs_path(config_path)
        alias = f"Job: {self.name}, project: {target.name}"
        return self.make_process(context, path, alias)

    @abstractmethod
    def make_process(self, context: dict, path: str, alias: str) -> Process:
        pass

    @staticmethod
    def from_config(dct: dict) -> List[T]:
        return [CommandJob(name=k, **v) if "command" in v else FunctionJob(name=k, **v) for k, v in dct.items()]
        

@dataclass
class CommandJob(Job):
    command: str

    def make_process(self, context: dict, path: str, alias: str) -> Process:
        call = substitute_exec_form(self.command, context, alias)
        return CommandProcess(call, path, alias)


@dataclass
class FunctionJob(Job):
    function: str

    def make_process(self, context: dict, path: str, alias: str) -> Process:
        module_path, funct_name = str.rsplit(self.function, ":", 1)
        funct = getattr(import_module(module_path), funct_name)
        return FunctionProcess(funct, context, path, alias)
