from subprocess import run
from typing import Any
from typing import List
from typing import Tuple

from multi_job.models.exceptions import ArgumentMissing
from multi_job.models.exceptions import StepError

from .colours import blue
from .colours import fail
from .emojis import CROWN
from .emojis import MUSHROOM
from .emojis import RICE_BALL
from .emojis import TOPHAT


def get_required_from_context(keys: List[str], context: dict) -> Tuple[Any, ...]:
    missing_context = set(keys) - set(context.keys())
    if missing_context:
        msg = (
            f"Missing non-optional arguments caught during runtime"
            + f"\nMissing context: {list(missing_context)}"
        )
        raise ArgumentMissing(msg)
    context_values = [context[key] for key in keys]
    return context_values.pop() if len(context_values) == 1 else context_values


def get_optional_from_context(keys: List[str], context: dict) -> Tuple[Any, ...]:
    context_values = [context[key] if key in context else None for key in keys]
    return context_values.pop() if len(context_values) == 1 else context_values


def step(process: List[str], path: str, stdout=None) -> None:
    output = run(process, cwd=path, stdout=stdout)
    if output.returncode != 0:
        msg = f"Step: {process} returned a non zero exit code\nOutput: {output}"
        raise StepError(msg)


success_msg = TOPHAT + blue("Function exited successfully") + CROWN
failure_msg = RICE_BALL + fail("Function failed") + MUSHROOM
