#!/usr/bin/python3
"""
    This module defines a class Rectangle that inherits from BaseGeometry.
"""


class Rectangle(BaseGeometry):
    """
    Defines a Rectangle class.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle object.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
