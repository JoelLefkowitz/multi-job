from docopt import docopt  # type: ignore


def intercept(interface: str) -> dict:
    return docopt(interface)
