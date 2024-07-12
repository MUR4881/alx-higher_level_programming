#!/usr/bin/python3

# -*- coding: utf-8 -*-

"""A simple module  containing a subclass of the Base class
    'Rectangle'
"""

from models.base import Base


class Rectangle(Base):
    """A Rectangle class Inheriting from Base
    class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initailinzing from the super and base classes

        Args:
            width: of the rectangle instance
            height: of the rectangle instance
            x: co-ordinate of the instance
            y: co-ordinate of the instance
            id: id passed to the super class instantiation
        """
        super().__init__(id)
        self.__x = x  #: int: The x co-ordinate of the object
        self.__y = y  #: int: The y co-ordinate of the object
        self.__width = width  #: int the width of the rect object
        self.__height = height  #: int the height of the rect obj

    @property
    def x(self):
        """getter for the x co-ordinate
        """
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        """getter for the y co-ordinate
        """
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    @property
    def width(self):
        """getter for the width dimension
        """
        return self.__width

    @width.setter
    def width(self, width):
        """Setter for the width dimension
        """
        self.__width = width

    @property
    def height(self):
        """getter for the height attribute
        """
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height
