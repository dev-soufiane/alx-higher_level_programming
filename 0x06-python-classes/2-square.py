#!/usr/bin/python3
""" Size validation task """


class Square:
    """ A class that represents a square. """

    def __init__(self, size=0):
        """ Initiliazing square object. """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
