import os

from multi_job.utils.functions import get_required_from_context
from multi_job.utils.functions import step
from multi_job.utils.functions import success_msg


def main(path: str, context: dict) -> str:
    clean_dirs = get_required_from_context(["clean_dirs"], context)

    clean_dirs = [os.path.realpath(os.path.join(path, target)) for target in clean_dirs]

    for target in clean_dirs:
        if os.path.exists(target):
            step(["rm", "-r", target + "/"], path)
    return success_msg
