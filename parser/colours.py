def bold(str) -> str:
    return "\033[1m" + str + "\033[0m"


def underline(str) -> str:
    return "\033[4m" + str + "\033[0m"


def fail(str) -> str:
    return "\033[91m" + str + "\033[0m"


def green(str) -> str:
    return "\033[92m" + str + "\033[0m"


def warn(str) -> str:
    return "\033[93m" + str + "\033[0m"


def blue(str) -> str:
    return "\033[94m" + str + "\033[0m"


def header(str) -> str:
    return "\033[95m" + str + "\033[0m"
