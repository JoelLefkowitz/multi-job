from dataclasses import dataclass
from os.path import basename, dirname, normpath
from sys import path
from types import ModuleType


def from_path(module_path: str) -> ModuleType:
    module_name = basename(normpath(module_path))
    module_dir = dirname(normpath(module_path))
    with PathControl(module_dir):
        module = __import__(module_name)
    return module


@dataclass
class PathControl:
    module_dir: str

    def __enter__(self) -> None:
        path.append(self.module_dir)

    def __exit__(self, type, value, tb) -> None:
        path.remove(self.module_dir)
