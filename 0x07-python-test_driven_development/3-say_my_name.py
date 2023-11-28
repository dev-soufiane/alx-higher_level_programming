#!/usr/bin/python3
""""

This module includes a function that displays a given name.

"""


def say_my_name(first_name, last_name=""):
    """ This function prints name (<first name> <last name>)

    Args:
        first_name (str): The fisrt name to be printed
        last_name (str): The last name to be printed

    Raises:
        TypeError: In case either the first_name or last_name
        are not of string data type

    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
