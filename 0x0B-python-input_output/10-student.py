#!/usr/bin/python3
"""
    This module defines a class Student.
"""


class Student:
    """
    Defines a class Student.
    """
    def __init__(self, first_name, last_name, age):
        """ Initializes a Student object """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self, attrs=None):
        """ Retrieves a dictionary representation of a Student. """
        res = {}

    if attrs is None:
        return self.__dict__

    for attr in attrs:
        value = self.__dict__.get(attr)
        if value is not None:
            res[attr] = value

    return res
