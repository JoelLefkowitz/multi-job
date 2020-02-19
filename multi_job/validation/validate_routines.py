from .validation_utils import Result, Validator


def check_routine_lst(config: dict) -> Result:
    return Result(True)


def check_routine_valid(config: dict) -> Result:
    return Result(True)


routine_validators = [
    Validator(
        "Routine configuration", "Routines must be a list or 'all'", check_routine_lst,
    ),
    Validator(
        "Routine configuration",
        "Routines may only contain job names or 'all'",
        check_routine_valid,
    ),
]
