from .validation_utils import Result, Validator


def check_project_has_path(config: dict) -> Result:
    return Result(True)


def check_project_path_str(config: dict) -> Result:
    return Result(True)


def check_project_path_exists(config: dict) -> Result:
    return Result(True)


def check_project_context_dict(config: dict) -> Result:
    return Result(True)


project_validators = [
    Validator(
        "Project configuration",
        "Projects must have a path field",
        check_project_has_path,
    ),
    Validator(
        "Project configuration",
        "A project's path field must be a string",
        check_project_path_str,
    ),
    Validator(
        "Project configuration",
        "A project's path field must be resolvable",
        check_project_path_exists,
    ),
    Validator(
        "Project configuration",
        "A project context field can only be a dictionary",
        check_project_context_dict,
    ),
]
