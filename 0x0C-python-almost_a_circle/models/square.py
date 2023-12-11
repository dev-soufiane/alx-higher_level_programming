#!/usr/bin/python3
""" This module defines a class Square that inherits from Rectangle. """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Defines a class Square. """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes a new Square object. """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Gets the size attribute. """
        return self.width

    @size.setter
    def size(self, value):
        """ Sets the size attribute. """
        self.width = value
        self.height = value

    def __str__(self):
        """
        Returns a string representation of the sqaure object.
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.size)
