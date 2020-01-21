import re
import os
from typing import Callable, List


def sub_to_exec(string: str, params: List[str]) -> List[str]:
    cmd = re.sub(
        "<.+?>",
        lambda x: params[remove_chars(x.group(0), ["<", ">"])],
        string,
    )
    return cmd.split(" ")


def remove_chars(string: str, chars: List[str]) -> str:
    to_remove = {c: "" for c in chars}
    return string.translate(str.maketrans(to_remove))


def formatted_update(a: dict, b: dict, callback: Callable[[str], str]) -> dict:
    if callback:
        return {k: b[fmt(k)] if b[fmt(k)] else v for (k, v) in a.items()}


def join_paths(a: str, b: str) -> str:
    return os.path.abspath(os.path.join(a, b))
