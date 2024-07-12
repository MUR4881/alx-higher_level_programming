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
        self.x = x  #: int: The x co-ordinate of the object
        self.y = y  #: int: The y co-ordinate of the object
        self.width = width  #: int the width of the rect object
        self.height = height  #: int the height of the rect obj

    @property
    def x(self):
        """getter for the x co-ordinate

            The setter ensures the value is
            an integer and not lesser than 0
        """
        return self.__x

    @x.setter
    def x(self, x):
        self.validate(x, 'x')
        self.__x = x

    @property
    def y(self):
        """getter for the y co-ordinate

            The setter ensures the value is
            an integer and not lesser than 0
        """
        return self.__y

    @y.setter
    def y(self, y):
        self.validate(y, 'y')
        self.__y = y

    @property
    def width(self):
        """getter for the width dimension
            The setter ensures the value is
            an integer not lesser or equal
            to zero
        """
        return self.__width

    @width.setter
    def width(self, width):
        """Setter for the width dimension
        """
        self.validate(width, 'width')
        self.__width = width

    @property
    def height(self):
        """getter for the height attribute

            The setter ensures the value is
            an integer not lesser or equal
            to zero
        """
        return self.__height

    @height.setter
    def height(self, height):
        self.validate(height, 'height')
        self.__height = height

    def area(self):
        """Generate the area of the Rectangle instance

        Return: The area calculated
        """
        return self.__width * self.__height

    def validate(self, value, name):
        """Helps validate width, height, x, y
        attributes when setting

        Args:
            value: The value be assigned to the
            attribute
            name: The variable name of the attribute
        """
        if type(value) is int:
            if name in ('x', 'y') and value < 0:
                raise ValueError(f'{name} must be >= 0')
            if name in ('width', 'height') and value <= 0:
                raise ValueError(f'{name} must be > 0')
        else:
            raise TypeError(f"{name} must be an integer")

    def display(self):
        """Print in stdout the Rectangle instance
        with the character #
        """
        print((('#' * self.__width) + '\n') * self.__height, end="")

    def __str__(self):
        """Overiding what is printed when the object
        passed to a print function
        """
        return f'[{self.__class__.__name__}] ({self.id}) \
{self.__x}/{self.__y} - \
{self.__width}/{self.__height}'
