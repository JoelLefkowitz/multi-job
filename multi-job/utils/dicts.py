from typing import List


def override(dicts: List[dict]) -> dict:

    # Remove key = None so that they aren't used for overrites
    dicts = [{k: v for k, v in d.items() if v} for d in dicts]

    reduced = {}
    for d in dicts:
        reduced.update(d)
    return reduced
