#!/usr/bin/python3
"""
    This module checks if an object is an instance of, or if the object is
    an instance of a class that inherited from, the specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Determines if the object is an instance of, or if the object is an instance
    of a class that inherited from, the specified class.
    """
    return isinstance(obj, a_class)
