from abc import ABC, abstractmethod, abstractproperty
from dataclasses import dataclass
from subprocess import run
from typing import Callable


@dataclass
class Process(ABC):
    path: str
    alias: str

    @abstractmethod
    def trigger(self) -> str:
        pass

    @abstractproperty
    def raw(self) -> str:
        pass

    def show(self, verbose: bool) -> str:
        return self.raw if verbose else self.alias


@dataclass
class CommandProcess(Process):
    call: str

    def trigger(self) -> str:
        output = run(self.call, cwd=self.path)
        return str(output)

    @property
    def raw(self) -> str:
        return f"{self.call} in {self.path}"


@dataclass
class FunctionProcess(Process):
    function: Callable
    context: dict

    def trigger(self) -> str:
        return self.function(self.path, self.context)

    @property
    def raw(self) -> str:
        return f"{self.function} with path arg: {self.path} and context arg: {self.context}"
