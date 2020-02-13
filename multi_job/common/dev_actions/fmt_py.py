from multi_job.utils.functions import step


def main(path: str, context: dict) -> str:
    step(["black", ".", "--exclude", "/venv/"], path)
    step(["isort", "-rc", "."], path)
    step(
        [
            "autoflake",
            "-r",
            "--in-place",
            "--remove-unused-variables",
            "--expand-star-imports",
            ".",
        ],
        path,
    )
