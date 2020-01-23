def bold(str):
    return "\033[1m" + str + "\033[0m"


def underline(str):
    return "\033[4m" + str + "\033[0m"


def fail(str):
    return "\033[91m" + str + "\033[0m"


def green(str):
    return "\033[92m" + str + "\033[0m"


def warn(str):
    return "\033[93m" + str + "\033[0m"


def blue(str):
    return "\033[94m" + str + "\033[0m"


def header(str):
    return "\033[95m" + str + "\033[0m"
