"""
String utility methods
"""

import os
from typing import List


def join_paths(a: str, b: str) -> str:
    """Join two paths and return the absolute path of the result
    
    Args:
        a (str): First path
        b (str): Second path
    
    Returns:
        str: Absolute joined path
    """
    return os.path.abspath(os.path.join(a, b))


def remove_chars(string: str, chars: List[str]) -> str:
    """
    Removes all instances of characters in the given list from the string

    Args:
        string (str): Initial string from which to remove characters
        chars (List[str]): List of characters to remove
    
    Returns:
        str: String with all instances removed 
    """
    replacements = str.maketrans({c: "" for c in chars})
    return string.translate(replacements)


def has_prefix(string: str, prefix: str) -> bool:
    """
    TODO
    
    Args:
        string (str): [description]
        prefix (str): [description]
    
    Returns:
        bool: [description]
    """
    return len(string) > len(prefix) and string[: len(prefix)] == prefix
