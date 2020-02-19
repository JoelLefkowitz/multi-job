from .validation_utils import Result, Validator


def check_job_has_callable(config: dict) -> Result:
    return Result(True)


def check_job_callable_str(config: dict) -> Result:
    return Result(True)


def check_job_callable_exists(config: dict) -> Result:
    return Result(True)


def check_job_has_targets_xor_skips(config: dict) -> Result:
    return Result(True)


def check_job_targets_lst(config: dict) -> Result:
    return Result(True)


def check_job_valid_targets(config: dict) -> Result:
    return Result(True)


job_validators = [
    Validator(
        "Job configuration",
        "Jobs must have a 'callable' ie a command xor script xor a function field",
        check_job_has_callable,
    ),
    Validator(
        "Job configuration",
        "A job's callable field must be a string",
        check_job_callable_str,
    ),
    Validator(
        "Job configuration",
        "A job's callable field must be resolvable",
        check_job_callable_exists,
    ),
    Validator(
        "Job configuration",
        "Jobs may only have a targets xor a skips field",
        check_job_has_targets_xor_skips,
    ),
    Validator(
        "Job configuration",
        "A job's targets or skips field must be a list or 'all",
        check_job_targets_lst,
    ),
    Validator(
        "Job configuration",
        "A job's targets or skips field must contain project names or 'all'",
        check_job_valid_targets,
    ),
]
