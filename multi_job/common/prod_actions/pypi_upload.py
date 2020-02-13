

def main(path: str, context: dict) -> str:
    RELEASE_TYPE, TWINE_USERNAME = get_from_context(
        ["release_type", "twine_username"], context
    )
    step(["bumpversion", RELEASE_TYPE], path)
    step(["python3", "setup.py", "sdist", "bdist_wheel"], path)
    step(["twine", "upload", "dist/*", "--username", TWINE_USERNAME], path)
