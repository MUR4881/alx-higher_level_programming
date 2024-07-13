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
