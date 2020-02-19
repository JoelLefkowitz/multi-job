"""
Validation checks to be run sequentiatlly
"""

import ruamel.yaml  # type: ignore
from .validate_structure import structure_validators
from .validate_jobs import job_validators
from .validate_routines import routine_validators
from .validate_projects import project_validators


def validate(config_path: str) -> dict:
    """Apply all validation functions to the given configuration
    
    Args:
        config_path (str): Path to the configuration file
    
    Returns:
        Any: Validated configuration
    """
    config = read(config_path)

    # Validate structure first to allow simpler validator designs
    for validator in (
        structure_validators + job_validators + routine_validators + project_validators
    ):
        validator.validate(config)
    return config


def read(config_path: str) -> dict:
    """
    Read configuration from yaml file
    
    Args:
        config_path (str): Path to configuration file
    
    Returns:
        Any: Unvalidated configuration
    """
    with open(config_path, "r") as stream:
        return ruamel.yaml.load(stream, Loader=ruamel.yaml.Loader)
