"""
Multi-job exceptions
"""

import sys; sys.path.append('..')
from utils.colours import fail
from utils.emojis import FIRE


class PrettyException(Exception):
    def __init__(self, message):
        pretty_msg = f"\n{FIRE}{fail('Oh my!')}{FIRE}\n{message}"
        super().__init__(pretty_msg)


class ParserValidationError(PrettyException):
    pass


class ConfigNotGiven(PrettyException):
    pass


class ArgumentMissing(PrettyException):
    pass