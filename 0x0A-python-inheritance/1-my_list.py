#!/usr/bin/python3
"""
    This module deines class MyList that inherits from list.
"""


class MyList(list):
    """ Defines a MyList class """
    def print_sorted(self):
        """Prints the list in ascending order."""
        print(sorted(self))
