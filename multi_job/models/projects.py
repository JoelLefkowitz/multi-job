from dataclasses import dataclass, field
from typing import List, Type, TypeVar

from multi_job.utils.strings import join_paths

T = TypeVar("T")


@dataclass
class Project:
    name: str
    path: str
    context: dict = field(default_factory=dict)

    def abs_path(self, config_path):
        return join_paths(config_path, self.path)

    @classmethod
    def from_config(cls: Type[T], dct: dict) -> List[T]:
        return [cls(name=k, **v) for k, v in dct.items()]
