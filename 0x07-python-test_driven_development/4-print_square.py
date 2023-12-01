#!/usr/bin/python3
"""
This module contains a function to print a square.
"""


def print_square(size):
    """Prints a square with the character '#'.

    Args:
        size (int): Represents the length of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than zero.

    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for n in range(size):
        for m in range(size):
            print("#", end="")
        print("")
