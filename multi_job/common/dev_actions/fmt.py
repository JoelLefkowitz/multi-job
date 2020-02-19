from multi_job.utils.functions import step, success_msg


def main(path: str, context: dict) -> str:
    step(["black", ".", "--exclude", "node_modules|venv"], path)
    step(["prettier", "--write", "**/*.{ts,js,html,scss,md,yml}"], path)
    return success_msg
