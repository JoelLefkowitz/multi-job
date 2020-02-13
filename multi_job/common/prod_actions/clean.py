from multi_job.utils.functions import get_from_context, step


def main(path: str, context: dict) -> str:
    DIRS = get_from_context(["clean_dirs"], context)
    for dir in DIRS:
        step(["find", "-path", "'./dist'", "-exec", "rm", "-r", "{}", "+"], path)
