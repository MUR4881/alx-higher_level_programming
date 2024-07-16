#!/usr/bin/python3

# -*- coding: utf-8 -*-

"""A module contain a subclass of Rectangle(rectangle.py)
    named Square (in this module)
"""


# importing Dependencies
from models.rectangle import Rectangle


class Square(Rectangle):
    '''A Square class, being a subset of the rectangle class
    '''

    def __init__(self, size, x=0, y=0, id=None):
        '''Initializing any new square instance

        Args:
            size: The width, height ofthe square
            x:  The x co-ordinate of the  square
            y:  The y co-ordinate of the square
            id: The assigned identification of the
            object
        '''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Overloading the string method from the base class

        Returns: The a string representation the instance
        """
        return f'[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y}\
 - {self.width}'

    @property
    def size(self):
        '''getter method for size of the square,
        actually, interacting, with width, height,
        attribute/property from the Rectangle(Base)
        class(of the base instance)

        the setter, calls the setter, of width and height
        '''
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.heigth = size

    def update(self, *args, **kwargs):
        '''Updates the attributes of the objects

        Args:
            args: a list, or tuple of args
        '''
        # attributes are ordered here, values
        # passed through args are expected
        if len(args) > 0:
            attrs = ['id', 'size', 'x', 'y']
            for attr, value in zip(attrs, *args):
                self.__setattr__(attr,  value)
        # Going for attributes passed through kwargs
        else:
            for key, value in zip(kwargs.keys(), kwargs.values()):
                if hasattr(self, key):
                    self.__setattr__(key, value)

    def to_dictionary(self):
        '''Generate a dictionary representation of
        a Square instance

        Return: The the diction of the attributes
        '''
        dct = {}
        attrs = ['id', 'x', 'size', 'y']
        for attr in attrs:
            dct[attr] = getattr(self, attr)
        return dct

    def to_list(self):
        '''Generate A list of attributes value of
        a Square instance

        Return: The list of attributes values
        '''
        lst = []
        attrs = ['id', 'size', 'x', 'y']
        # Now return the list value of the attributes
        for attr in attrs:
            lst.append(getattr(self, attr))
        return lst
