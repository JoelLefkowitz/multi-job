import ruamel.yaml
from parser.exceptions import ParserValidationError
from typing import Any


def validate(config_path: str) -> Any:
    tree = read(config_path)
    check_top_level(tree)
    check_required_fields(tree)
    check_paths(tree)
    check_arguments(tree)
    return tree


def reject(general: str = None, specific: str = None, case: str = None) -> None:
    msg = f"\n\nValidation error:\n{'. '.join([general, specific, case])}" 
    raise ParserValidationError(msg)


def read(config_path: str) -> Any:
    with open(config_path, "r") as stream:
        return ruamel.yaml.load(stream, Loader=ruamel.yaml.Loader)


def check_top_level(tree: Any) -> None:
    general = "The configuration file's top level elements are invalid"
    if type(tree) != dict:
        specific = "The configuration given is not a dictionary"
        reject(general, specific)
    
    for top_level_name in tree.keys():
        specific = "Top level entries must consist only of dictionaties named 'jobs' or 'projects'"

        if top_level_name not in ['jobs', 'projects']:
            case = f"'{top_level_name}' is not 'jobs' or 'projects'"
            reject(general, specific, case)

        if type(tree[top_level_name]) != dict:
            case = f"'{top_level_name}' is not a dictionary"
            reject(general, specific, case)
        

# TODO Write check_required_fields 
def check_required_fields(tree: Any) -> None:
    general = "Not all required fields are filled"
    if False:
        specific = "Projects must have paths"
        reject(general, specific)
    if False:
        specific = "Jobs must have commands or function paths"
        reject(general, specific)
    if False:
        specific = "Functions needs a name and path"
        reject(general, specific)


# TODO Write check_paths
def check_paths(tree: Any) -> None:
    general = "Paths must be valid"
    if False:
        specific = "Project paths must be resolvable"
        reject(general, specific)
    if False:
        specific = "Function paths must be resolvable"
        reject(general, specific)


# TODO Write check_arguments
def check_arguments(tree: Any) -> None:
    general = "References must be valid"
    if False:
        specific = "Project parameters must specify valid jobs"
        reject(general, specific)
    if False:
        specific = "Project parameters must exist in the declared job"
        reject(general, specific)
    if False:
        specific = "Project targets must reference valid projects"
        reject(general, specific)
    if False:
        specific = "Project skips must reference valid projects"
        reject(general, specific)
    if False:
        specific = "Job targets must reference valid projects"
        reject(general, specific)
    if False:
        specific = "Job skips must reference valid projects"
        reject(general, specific)
