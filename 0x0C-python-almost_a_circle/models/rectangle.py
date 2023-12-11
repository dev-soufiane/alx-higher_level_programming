#!/usr/bin/python3
""" this module defines a class Rectangle that inherits from Base. """
from models.base import Base


class Rectangle(Base):
    """ Defines a class Rectangle. """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initializes a new Rectangle object. """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ Gets width attribute. """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets width attribute. """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Gets height attribute. """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets height attribute. """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Gets x attribute. """
        return self.__x

    @x.setter
    def x(self, value):
        """ Sets x attribute. """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Gets y attribute. """
        return self.__y

    @y.setter
    def y(self, value):
        """ Sets y attribute. """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Returns the area of the Rectangle. """
        return self.width * self.height

    def display(self):
        """
        Print the Rectangle using the `#` character.
        """
        for _ in range(self.y):
            print()

        for _ in range(self.height):
            for _ in range(self.x):
                print(" ", end="")
            for _ in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """
        Returns a string representation of the Rectangle instance.
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """ Assigns an argument to each attribute. """
        attributes = ["id", "width", "height", "x", "y"]

        if args:
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)
