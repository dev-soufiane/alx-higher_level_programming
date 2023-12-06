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

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance.
        """
        myDict = self.__dict__

        for key, value in json.items():
            if (myDict.get(key) == self.first_name):
                self.first_name = value
            elif (myDict.get(key) == self.last_name):
                self.last_name = value
            elif (myDict.get(key) == self.age):
                self.age = value
