"""
Utility methods for '<element>' style tags
"""

import re
from typing import List, Mapping

from multi_job.models.exceptions import ArgumentMissing


def is_tagged(string: str) -> bool:
    """
    Check whether a string is enclosed in '<' and '>' characters
    
    Args:
        string (str): String to test
    
    Returns:
        bool: True if string is enclosed in '<' and '>'
    """
    return len(string) > 2 and string[0] == "<" and string[-1] == ">"


def strip_tags(string: str) -> str:
    """
    Strip '<' and '>' characters if a string is enclosed in them

    Args:
        string (str): String to strip
    
    Returns:
        str: Stripped string
    """
    return string[1:-1] if is_tagged(string) else string


def get_tagged_elements(string: str) -> List[str]:
    """
    Extract all substrings that are enclosed by '<' and '>'
    Args:
        string (str): String to extract from
    
    Returns:
        List[str]: List of all substrings that are enclosed by '<' and '>'
    """
    words = string.split(" ")
    return [strip_tags(word) for word in words if is_tagged(word)]


def substitute_exec_form(
    string: str, context: Mapping[str, str], description: str
) -> str:
    """ 
    Replace all substrings that are enclosed by '<' and '>' by the value
    stored at that substring's key in a dictionary

    Args:
        string (str): String on which to perform the substitution
        params (List[str]): Dictionary of substitutions
    
    Returns:
        List[str]: String with all substrings that are enclosed by
        <' and '>' substituted
    """
    raw = re.sub(
        "<.+?>",
        lambda x: get_context(strip_tags(x.group(0)), context, description),
        string,
    )
    return raw.split(" ")


def get_context(param: str, context: Mapping[str, str], description: str):
    if param in context:
        return context[param]
    else:
        msg = f"Argument not found: {param}\n{description}\nContext: {context}"
        raise ArgumentMissing(msg)
