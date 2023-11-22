#!/usr/bin/python3
""" Coordinates of a square """


class Square:
    """ Defines square"""
    def __init__(self, size=0, position=(0, 0)):
        """ initializing a square object """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ Gets the size attribute """
        return self.__size

    @size.setter
    def size(self, value):
        """ Sets the size attribute """
        if not type(value) is int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """ Gets the position attribute """
        return self.__position

    @position.setter
    def position(self, value):
        """ Sets the position attribute """
        if not type(value) is tuple or len(value) != 2 \
                or not type(value[0]) is int or not type(value[1]) is int \
                or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ Returns the square area """
        return self.__size**2

    def my_print(self):
        """ Prints the square forming by '#' symbol """
        if self.__size == 0:
            print()
        else:
            print('\n'*self.__position[1], end='')
            for i in range(0, self.__size):
                print(' '*self.__position[0], end='')
                print('#'*self.__size)
