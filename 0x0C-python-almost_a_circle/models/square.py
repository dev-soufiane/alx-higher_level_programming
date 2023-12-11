#!/usr/bin/python3
""" This module defines a class Square that inherits from Rectangle. """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Defines a class Square. """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes a new Square object. """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """
        Returns a string representation of the sqaure object.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.size)
