from multi_job.utils.functions import step


def main(path: str, context: dict) -> str:
    step(["prettier", "**/*.ts"], path)
