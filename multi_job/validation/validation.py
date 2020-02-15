"""
Validation checks to be run sequentiatlly
"""

from dataclasses import dataclass
from typing import Any, Callable, NoReturn, Optional

import ruamel.yaml  # type: ignore

from multi_job.models.exceptions import ParserValidationError


@dataclass
class Result:
    success: bool
    details: Optional[str] = None


@dataclass
class Validator:
    category: str
    subcategory: str
    check: Callable[..., Result]

    def validate(self, config: Any):
        """
        Apply the validator's check method and call its reject method if the
        result is a failure
        
        Args:
            config (Any): Validation target
        """
        result = self.check(config)
        if not result.success:
            self.reject(result.details)

    def reject(self, details: Optional[str]) -> NoReturn:
        """
        Raise a ParserValidationError with a formatted error message
        
        Args:
            details (Optional[str]): The specific case of failure reported in the check's result
        
        Raises:
            ParserValidationError:
 
        Returns:
            NoReturn:
        """
        msg = f"The config file failed validation.\nIssue catagory: {self.category}\nIssue subcatagory: {self.subcategory}\nDetails: {details}"
        raise ParserValidationError(msg)


def validate(config_path: str) -> Any:
    """Apply all validation functions to the given configuration
    
    Args:
        config_path (str): Path to the configuration file
    
    Returns:
        Any: Validated configuration
    """
    config = read(config_path)
    spec = {
        "Top level structure": {
            "The configuration must not be blank": check_not_blank,
            "The configuration must be a dictionary": check_top_level_dict,
            "The configuration's top level must contain only 'jobs', 'projects' or 'routines'": check_top_level_names,
        },
        "Jobs, projects and routines' structure": {
            "Jobs, projects and routines must be dictionaries": check_second_level_dict,
            "Each job and project must be a dictionary": check_third_level_dict,
            "Each routine must be a list": check_routines_list,
            "Jobs, projects and routines must have unique names": check_unique_names,
        },
        "Project fields": {
            "Projects must have a path field": check_projects_have_paths,
            "A project's path field must be a string": check_project_paths_strings,
            "A project's path field must be resolvable": check_project_paths_exist,
            "A project context field can only be a dictionary": check_project_params_dict,
        },
        "Job fields": {
            "Jobs must have a command xor a function field": check_jobs_calls,
            "A job's command field must be a string": check_jobs_commands_strings,
            "A job's function field must be a string": check_jobs_functions_strings,
            "A job's function field must be resolvable": check_jobs_function_exists,
            "Jobs may only have a targets xor a skips field": check_jobs_targets_field,
            "A job's targets or skips field must be a list or 'all": check_jobs_targets_list,
            "A job's targets or skips field must contain project names or 'all'": check_jobs_targets_names,
        },
        "Routine fields": {
            "Routines may only contain job names or 'all'": check_routines_names,
        },
    }

    validators = [
        Validator(category, subcategory, check)
        for category, subcategory_entry in spec.items()
        for subcategory, check in subcategory_entry.items()
    ]

    for validator in validators:
        validator.validate(config)
    return config


def read(config_path: str) -> Any:
    """
    Read configuration from yaml file
    
    Args:
        config_path (str): Path to configuration file
    
    Returns:
        Any: Unvalidated configuration
    """
    with open(config_path, "r") as stream:
        return ruamel.yaml.load(stream, Loader=ruamel.yaml.Loader)


def check_not_blank(config: Any) -> Result:
    return Result(True) if config else Result(False)


def check_top_level_dict(config: Any) -> Result:
    return Result(True) if type(config) is dict else Result(False)


def check_top_level_names(config: Any) -> Result:
    if list(config.keys()) == ["jobs", "projects", "routines"]:
        return Result(True)
    else:
        issues = list(set(config.keys()) - set(["jobs", "projects", "routines"]))
        return Result(False, f"{issues} don't match 'jobs', 'projects' or 'routines'")


def check_second_level_dict(config: Any) -> Result:
    if not type(config["jobs"]) is dict:
        return Result(False, f"'Jobs' must be a dictionary")
    elif not type(config["projects"]) is dict:
        return Result(False, f"'Projects' must be a dictionary")
    elif not type(config["routines"]) is dict:
        return Result(False, f"'Routines' must be a dictionary")
    else:
        return Result(True)


def check_third_level_dict(config: Any) -> Result:
    return Result(True)


def check_routines_list(config: Any) -> Result:
    return Result(True)


def check_unique_names(config: Any) -> Result:
    return Result(True)


def check_projects_have_paths(config: Any) -> Result:
    return Result(True)


def check_project_paths_strings(config: Any) -> Result:
    return Result(True)


def check_project_paths_exist(config: Any) -> Result:
    return Result(True)


def check_project_params_dict(config: Any) -> Result:
    return Result(True)


def check_project_params_keys(config: Any) -> Result:
    return Result(True)


def check_project_params_values(config: Any) -> Result:
    return Result(True)


def check_jobs_calls(config: Any) -> Result:
    return Result(True)


def check_jobs_commands_strings(config: Any) -> Result:
    return Result(True)


def check_jobs_functions_strings(config: Any) -> Result:
    return Result(True)


def check_jobs_function_exists(config: Any) -> Result:
    return Result(True)


def check_jobs_targets_field(config: Any) -> Result:
    return Result(True)


def check_jobs_targets_list(config: Any) -> Result:
    return Result(True)


def check_jobs_targets_names(config: Any) -> Result:
    return Result(True)


def check_routines_names(config: Any) -> Result:
    return Result(True)
