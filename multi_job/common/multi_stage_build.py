from multi_job.utils.functions import (
    get_required_from_context,
    get_optional_from_context,
    step,
    success_msg,
)


def main(path: str, context: dict) -> str:
    version, image_name = get_required_from_context(["version", "image_name"], context)
    build_args, build_stage_prefix = get_optional_from_context(
        ["build_args", "build_stage_prefix"], context
    )

    if not build_stage_prefix:
        build_stage_prefix = "build"

    name_lst = ["-t", f"{image_name}:{version}"]
    build_name_lst = ["-t", f"{image_name}/{build_stage_prefix}:{version}"]
    build_file_lst = ["-f", f"{build_stage_prefix}.Dockerfile"]

    args_lst = []
    if build_args:
        for k, v in build_args.items():
            args_lst.append("--build-arg")
            args_lst.append(f"{k}={v}")

    step(["docker", "build", "."] + build_name_lst + build_file_lst + args_lst, path)
    step(["docker", "build", "."] + name_lst + args_lst, path)
    return success_msg
