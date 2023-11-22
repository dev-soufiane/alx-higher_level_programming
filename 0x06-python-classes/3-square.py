#!/usr/bin/python3
""" Area of a square task """


class Square:
    """ A class that defines a square """

    def __init__(self, size=0):
        """ Initialzing a square object. """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Public method that returns the current square area. """
        return self.__size ** 2
