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

    def to_json(self):
        """ Retrieves a dictionary representation of a Student. """
        self.__dict__
