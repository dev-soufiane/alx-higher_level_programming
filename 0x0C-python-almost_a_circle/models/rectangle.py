#!/usr/bin/python3
""" this module defines a class Rectangle that inherits from Base. """
from models.base import Base


class Rectangle(Base):
    """ defines a class Rectangle. """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initializes a new Rectangle object. """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ Gets width attribute. """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets width attribute. """
        self.__width = value

    @property
    def height(self):
        """ Gets height attribute. """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets height attribute. """
        self.__height = value

    @property
    def x(self):
        """ Gets x attribute. """
        return self.__x

    @x.setter
    def x(self, value):
        """ sets x attribute. """
        self.__x = value

    @property
    def y(self):
        """ Gets y attribute. """
        return self.__y

    @y.setter
    def y(self, value):
        """ sets y attribute. """
        self.__y = value
