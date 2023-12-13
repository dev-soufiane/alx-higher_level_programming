#!/usr/bin/python3
""" This module defines a Class Base. """
import json


class Base:
    """ Defines a Class Base."""
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializes a new Base object. """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of list_dictionaries. """
        if list_dictionaries == [] or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
