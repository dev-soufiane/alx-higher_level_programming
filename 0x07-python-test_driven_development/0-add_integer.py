#!/usr/bin/python3
"""

This module a function that adds 2 integers.
"""


def add_integer(a, b=98):
    """ Returns the sum of two numbers as integers.

    Args:
        a: first argument
        b: second argument

    Returns:
        Sum of the two arguments

    Raises:
        TypeError: Both arguments must be either an integer or a float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
