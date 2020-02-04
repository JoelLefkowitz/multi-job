
from utils.colours import green
from abc import ABC, abstractmethod, abstractproperty
from subprocess import run, CompletedProcess
from typing import Callable

from dataclasses import dataclass

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


class CommandProcess(Process):
    call: str

    def trigger(self) -> str:
        output = run(self.call, cwd=self.path)
        return str(output)

    def raw(self) -> str:
        return f"{self.call} in {self.path}"


class FunctionProcess(Process):
    function: Callable
    context: dict

    def trigger(self) -> str:
        return callablle(context)

    def raw(self) -> str:
        return f"{self.function} from {self.path} with context arg: {context}"
