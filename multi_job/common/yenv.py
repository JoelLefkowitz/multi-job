from multi_job.utils.functions import (
    get_required_from_context,
    step,
    success_msg,
)


def main(path: str, context: dict) -> str:
    env_targets, yenv_file = get_required_from_context("env-targets", "yenv-file")

    for target in env_targets:
        with open(f"{target}.env", "w") as file:
            step(
                ["yenv", "print", yenv_file, target, "dotenv", "-f", "-s"],
                path=path,
                stdout=file,
            )
    return success_msg
