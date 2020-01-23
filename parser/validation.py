import ruamel.yaml
from .exceptions import ParserValidationError
from typing import Any


def validate(config_path: str) -> Any:
    tree = read(config_path)
    check_top_level(tree)
    check_field_requirements(tree)
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

        if top_level_name not in ["jobs", "projects"]:
            case = f"'{top_level_name}' is not 'jobs' or 'projects'"
            reject(general, specific, case)

        if type(tree[top_level_name]) != dict:
            case = f"'{top_level_name}' is not a dictionary"
            reject(general, specific, case)


# TODO Write check_field_requirements
def check_field_requirements(tree: Any) -> None:
    general = "Not all field are filled correctly"
    if False:
        specific = "Projects must have paths"
        reject(general, specific)
    if False:
        specific = "Jobs must have commands or function paths"
        reject(general, specific)
    if False:
        specific = "Functions needs a name and path"
        reject(general, specific)
    if False:
        specific = "Jobs may have either targets or skips"
        reject(general, specific)
    if False:
        specific = "Jobs targets and skips must be a list of project names or None"
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
    general = "Argument references must be valid"
    if False:
        specific = "Project parameters must specify valid jobs"
        reject(general, specific)
    if False:
        specific = "Project parameters must exist in the declared job"
        reject(general, specific)
    if False:
        specific = "Command parameters must be specified in the command"
        reject(general, specific)
    if False:
        specific = "Project parameters must be a dictionary"
        reject(general, specific)
    if False:
        specific = "Command parameters must be a dictionary"
        reject(general, specific)
