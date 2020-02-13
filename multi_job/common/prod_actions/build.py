from multi_job.utils.functions import get_from_context, step


def main(path: str, context: dict) -> str:
    VERSION, NAME = get_from_context(["build_version", "build_name"])
    step(["docker", "build", ".", "-t", f"{NAME}:{VERSION}"], path)
