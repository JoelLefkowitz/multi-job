from multi_job.utils.functions import step, get_from_context, success_msg


def main(path: str, context: dict) -> str:
    version, image_name = get_from_context(["version", "image_name"], context)
    build = ["docker", "build", ".", "--build-arg", "VERSION=" + version]
    step(
        build + ["-t", f"{image_name}/build:{version}", "-f", "build.Dockerfile"], path
    )
    step(build + ["-t", f"{image_name}:{version}"], path)
    return success_msg
