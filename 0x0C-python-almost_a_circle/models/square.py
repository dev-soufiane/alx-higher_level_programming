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

    def update(self, *args, **kwargs):
        """ Assigns an argument to each attribute. """
        attributes = ['id', 'size', 'x', 'y']

        if args:
            for i, value in enumerate(args):
                setattr(self, attributes[i], value)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ Returns the dictionary representation of a Rectangle. """
        return {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y
                }
