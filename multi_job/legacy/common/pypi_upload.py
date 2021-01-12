from multi_job.utils.functions import get_required_from_context
from multi_job.utils.functions import step
from multi_job.utils.functions import success_msg


def main(path: str, context: dict) -> str:
    release_type, twine_username = get_required_from_context(
        ["release_type", "twine_username"], context
    )
    step(["bump2version", release_type], path)
    step(["python3", "setup.py", "sdist", "bdist_wheel"], path)
    step(["twine", "upload", "dist/*", "--username", twine_username], path)
    return success_msg
