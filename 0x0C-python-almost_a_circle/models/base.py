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

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file. """
        file_name = f"{cls.__name__}.json"
        with open(file_name, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """ Returns the list of the JSON string representation. """
        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns an instance with all attributes already set. """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                instance = cls(1, 1)
            else:
                instance = cls(1)
            instance.update(**dictionary)
            return instance
        return None
