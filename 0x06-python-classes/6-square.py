#!/usr/bin/python3
""" Coordinates of a square """


class Square:
    """ Defines a square """

    def __init__(self, size=0, position(0, 0)):
        """ Initialize a square object """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    @property
    def position(self):
        """ Retrieves the position attribute """
        return self.__position

    @position.setter
    def position(self, value):
        """ Sets the position attribute """
        if type(value) is not tuple or len(value) != 2 \
                or not type(value[0]) is int or not type(value[1]) is int \
                or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    @property
    def size(self):
        """ Retrieves the size attribute """
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
            print('\n'*self.__position[1], end='')
            for i in range(0, self.__size):
                print(' '*self.__position[0], end='')
                print('#'*self.__size)
        else:
            print()
