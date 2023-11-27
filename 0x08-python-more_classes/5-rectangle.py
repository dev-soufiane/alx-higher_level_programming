#!/usr/bin/python3
""" Detect instance deletion """


class Rectangle:
    """Defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializing a rectangle class
        Args:
            width: represents the width of the rectangle
            height: represents the height of the rectangle
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Returns the rectangle area """
        return self.__width * self.__height

    def perimeter(self):
        """" Returns the rectangle perimeter """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """ Prints out the rectangle """
        if self.__width == 0 or self.__height == 0:
            return ("")
        rect = ""
        for col in range(self.__height):
            for row in range(self.__width):
                rect += "#"
            if col < self.__height - 1:
                rect += "\n"
        return (rect)

    def __repr__(self):
        """ String representation of the rectangle """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """ Deletes rectangle """
        print("Bye rectangle...")
