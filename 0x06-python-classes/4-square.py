#!/usr/bin/python3
""" Access and update private attribute Task """


class Square:
    """ Defines a square """

    def __init__(self, size=0):
        """ Initialize square object. """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """ retrieve the size attribute """
        return self.__size

    @size.setter
    def size(self, value):
        """ set the size attribute """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Returns the current square area """
        return self.__size ** 2
