from multi_job.utils.functions import get_from_context, step, success_msg


def main(path: str, context: dict) -> str:
    version, image_name = get_from_context(["version", "image_name"])
    step(["docker", "build", ".", "-t", f"{image_name}:{version}"], path)
    return success_msg
