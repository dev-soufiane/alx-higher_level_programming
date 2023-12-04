#!/usr/bin/python3
"""
    This module defines a class Square
    that inherits from Rectangle (9-rectangle.py).
"""
Rectangle = __import__('9-rectangle.py').Rectangle


class Square(Rectangle):
    """
    Defines a Square class.
    """
    def __init__(self, size):
        """
        Initializes a square object.
        """
    super().__init__(size, size)
    self.integer_validator("size", size)
    super().__init__(size, size)
    self.__size = size
