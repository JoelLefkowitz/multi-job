"""
Project, Job, Routine and Subprocess classes
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Callable, List, Union

from multi_job.models.processes import CommandProcess, FunctionProcess, Process
from multi_job.models.projects import Project
from multi_job.utils.dicts import override
from multi_job.utils.imports import from_path
from multi_job.utils.strings import join_paths
from multi_job.utils.tags import substitute_exec_form


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
        context = override([self.context, context_overrides, target.context])
        path = target.abs_path(config_path)
        alias = f"Job: {self.name}, project: {target.name}"
        return self.make_process(context, path, alias, config_path)

    @abstractmethod
    def make_process(
        self, context: dict, path: str, alias: str, config_path: str
    ) -> Process:
        pass

    @staticmethod
    def from_config(dct: dict) -> List[Any]:
        return [
            CommandJob(name=k, **v)
            if "command" in v
            else FunctionJob(name=k, **v)
            if "function" in v
            else ScriptJob(name=k, **v)
            for k, v in dct.items()
        ]


@dataclass
class CommandJob(Job):
    command: str = ""

    def make_process(
        self, context: dict, path: str, alias: str, config_path: str
    ) -> Process:
        call = substitute_exec_form(self.command, context, alias)
        return CommandProcess(call=call, path=path, alias=alias)


@dataclass
class ScriptJob(Job):
    script: str = ""

    def make_process(
        self, context: dict, path: str, alias: str, config_path: str
    ) -> Process:
        call = join_paths(config_path, self.script)
        return CommandProcess(call=call, path=path, alias=alias)


@dataclass
class FunctionJob(Job):
    function: str = ""

    def get_function(self, config_path: str) -> Callable:
        module_path, funct_name = str.rsplit(self.function, ":", 1)
        abs_module_path = join_paths(config_path, module_path)
        module = from_path(abs_module_path)
        return getattr(module, funct_name)

    def make_process(
        self, context: dict, path: str, alias: str, config_path: str
    ) -> Process:
        funct = self.get_function(config_path)
        return FunctionProcess(function=funct, context=context, path=path, alias=alias)
