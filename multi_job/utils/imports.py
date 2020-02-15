import sys
from dataclasses import dataclass
from os import path
from types import ModuleType


def from_path(module_path: str) -> ModuleType:
    module_name = path.basename(path.normpath(module_path))
    module_dir = path.dirname(path.normpath(module_path))
    with PathControl(module_dir):
        module = __import__(module_name)
    return module


# Put common jobs package into scope
common_dir = path.realpath(path.join(__file__, "../../common"))


@dataclass
class PathControl:
    module_dir: str

    def __enter__(self) -> None:
        sys.path.append(self.module_dir)
        sys.path.append(common_dir)

    def __exit__(self, type, value, tb) -> None:
        sys.path.remove(self.module_dir)
        sys.path.remove(common_dir)
