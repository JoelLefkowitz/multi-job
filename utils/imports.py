from sys import path
from typing import ModuleType
from os.path import basename, dirname, normpath


def from_path(module_path: str) -> ModuleType:
    module_name = basename(normpath(module_path))
    module_dir = dirname(normpath(module_path))
    path.append(module_dir)
    module = __import__(module_name)
    path.remove(module_dir)
    return module
