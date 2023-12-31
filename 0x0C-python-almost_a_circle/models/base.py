#!/usr/bin/python3
""" This module defines a Class Base. """
import json
import csv


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

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances. """
        file_name = f"{cls.__name__}.json"

        try:
            with open(file_name, "r") as f:
                json_string = f.read()
                if not json_string:
                    return []
                else:
                    list_dicts = cls.from_json_string(json_string)
                    return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes the CSV serialization of a list of objects to a file."""
        filename = f"{cls.__name__}.csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs:
                fieldnames = (
                        ["id", "width", "height", "x", "y"]
                        if cls.__name__ == "Rectangle"
                        else ["id", "size", "x", "y"]
                        )
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Returns a list of class instances instantiated from a CSV file."""
        filename = f"{cls.__name__}.csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                fieldnames = (
                        ["id", "width", "height", "x", "y"]
                        if cls.__name__ == "Rectangle"
                        else ["id", "size", "x", "y"]
                        )
                dc = csv.DictReader(csvfile, fieldnames=fieldnames)
                dc = [dict([k, int(v)] for k, v in d.items()) for d in dc]
                return [cls.create(**d) for d in dc]
        except IOError:
            return []
