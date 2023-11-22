#!/usr/bin/python3
""" Printing a square """


class Square:
    """ Defines a square """

    def __init__(self, size=0):
        """ Initialize a square object """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """ retrieves the size attribute """
        return self.__size

    @size.setter
    def size(self, value):
        """ sets the size attribute """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Returns the current square area """
        return self.__size ** 2

    def my_print(self):
        """ Prints in stdout the square with the character #,
        if size is equal to 0, print an empty line """
        if self.__size != 0:
            for i in range(self.__size):
                print("#" * self.__size)
        else:
            print()
