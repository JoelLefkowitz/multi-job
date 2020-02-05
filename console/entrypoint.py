from sys import argv

from utils.imports import from_path
from utils.strings import join_paths


def console_entrypoint() -> None:
    """
    TODO
    """
    main_module = from_path(join_paths(argv[0], "../../main"))
    entrypoint = getattr(main_module, "entrypoint")
    entrypoint()
