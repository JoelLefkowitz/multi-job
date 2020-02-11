from subprocess import run
from typing import Any, List, Tuple

from multi_job.models.exceptions import ArgumentMissing, StepError


def get_from_context(keys: List[str], context: dict) -> Tuple[Any, ...]:
    context_values = []
    for key in keys:
        try:
            context_values.append(context[key])
        except KeyError as e:
            msg = f"Missing argument caught during runtime\nMissing context: {key}\n Key error: {e}"
            raise ArgumentMissing(msg)
    return context_values


def step(process: List[str], path: str) -> None:
    output = run(process, cwd=path)
    if output.returncode != 0:
        msg = f"Step: {process} returned a non zero exit code\nOutput: {output}"
        raise StepError(msg)
