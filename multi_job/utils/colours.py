"""
Utility functions for adding colour codes to strings
"""


def bold(string: str) -> str:
    """Add bold colour codes to string
    
    Args:
        string (str): Input string
    
    Returns:
        str: Bold string
    """
    return "\033[1m" + string + "\033[0m"


def underline(string: str) -> str:
    """Add underline colour codes to string
    
    Args:
        string (str): Input string
    
    Returns:
        str: Underlined string
    """
    return "\033[4m" + string + "\033[0m"


def fail(string: str) -> str:
    """Add fail colour codes to string
    
    Args:
        string (str): Input string
    
    Returns:
        str: Fail string
    """
    return "\033[91m" + string + "\033[0m"


def green(string: str) -> str:
    """Add green colour codes to string
    
    Args:
        string (str): Input string
    
    Returns:
        str: Green string
    """
    return "\033[92m" + string + "\033[0m"


def warn(string: str) -> str:
    """Add warn colour codes to string
    
    Args:
        string (str): Input string
    
    Returns:
        str: Warn string
    """
    return "\033[93m" + string + "\033[0m"


def blue(string: str) -> str:
    """Add blue colour codes to string
    
    Args:
        string (str): Input string
    
    Returns:
        str: Blue string
    """
    return "\033[94m" + string + "\033[0m"


def header(string: str) -> str:
    """Add header colour codes to string
    
    Args:
        string (str): Input string
    
    Returns:
        str: Header string
    """
    return "\033[95m" + string + "\033[0m"
