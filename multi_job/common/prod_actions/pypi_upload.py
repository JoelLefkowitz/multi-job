from multi_job.utils.functions import step, get_from_context, success_msg


def main(path: str, context: dict) -> str:
    release_type, twine_username = get_from_context(
        ["release_type", "twine_username"], context
    )
    step(["bumpversion", release_type], path)
    step(["python3", "setup.py", "sdist", "bdist_wheel"], path)
    step(["twine", "upload", "dist/*", "--username", twine_username], path)
    return success_msg
