#!/usr/bin/python3
""" This module defines a Class Base. """


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
