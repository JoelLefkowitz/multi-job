from multi_job.utils.functions import (
    get_required_from_context,
    get_optional_from_context,
    step,
    success_msg,
)


def main(path: str, context: dict) -> str:
    version, image_name = get_required_from_context(["version", "image_name"], context)
    build_args = get_optional_from_context(["build_args"], context)
    name_lst = ["-t", f"{image_name}:{version}"]
    args_lst = []
    if build_args:
        for k, v in build_args.items():
            args_lst.append("--build-arg")
            args_lst.append(f"{k}={v}")
    step(["docker", "build", "."] + name_lst + args_lst, path)
    return success_msg
