"""
Formatting functions for docopts
"""

from sys import argv


def fmt_uses(uses):
    """
    TODO write docstring
    
    Args:
        uses ([type]): [description]
    
    Returns:
        [type]: [description]
    """
    lines = [f"    {argv[0]} <config_path> [options] " + l for l in uses]
    return "Usage:\n" + "\n".join(lines)


def fmt_options(options):
    """
    TODO write docstring
    
    Args:
        options ([type]): [description]
    
    Returns:
        [type]: [description]
    """
    lines = [f"    --{opt}" for opt in options]
    return "\n" + "\n".join(lines)
