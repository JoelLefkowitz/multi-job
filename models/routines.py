from dataclasses import dataclass
from typing import List, Type, TypeVar

from .jobs import Job

T = TypeVar("T")


@dataclass
class Routine:
    name: str
    jobs: List[str]

    def resolve_jobs(self, jobs: List[Job]) -> List[Job]:
        return [j for j in jobs if j.name in self.jobs]

    @classmethod
    def from_config(cls: Type[T], dct: dict) -> List[T]:
        return [cls(name=k, jobs=v) for k, v in dct.items()]
