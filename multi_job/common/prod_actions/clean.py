from multi_job.utils.functions import get_from_context, step, success_msg


def main(path: str, context: dict) -> str:
    clean_dirs = get_from_context(["clean_dirs"], context)
    for target in clean_dirs:
        step(["find", "-path", target, "-exec", "rm", "-r", "{}", "+"], path)
    return success_msg
