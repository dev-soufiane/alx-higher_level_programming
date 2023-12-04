#!/usr/bin/python3
"""
    Defines the BaseGeometry class and its subclasses Rectangle and Square.

"""


class BaseGeometry:
    """A class with public instance methods area and integer_validator."""
    def area(self):
        """Raises an exception when called."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a given value is an integer greater than 0.

        Args:
            name (str): The name of the value.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """A representation of a rectangle."""
    def __init__(self, width, height):
        """
        Instantiation of the rectangle with specified width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Informal string representation of the rectangle."""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)


class Square(Rectangle):
    """A representation of a square, a subclass of Rectangle."""
    def __init__(self, size):
        """
        Instantiation of the square with specified size.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Informal string representation of the square."""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
