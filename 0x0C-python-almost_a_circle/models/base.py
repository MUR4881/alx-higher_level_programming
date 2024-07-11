#!/usr/bin/python3

# -*- encoding: utf-8 -*-

"""A simple module, entailing a simple Base class called Base
"""


class Base:
    """A simple class designed to be used as a Base class
    for other sub classes, and keeps count of all non id'ed
    instances and instances of it classes
    """
    __nb_objects = 0  #: int: number of instances

    def __init__(self, id=None):
        """Creating instance

        Args:
            id: an integer identification, which is
            defaultely instant count, if not passed
        """
        if id is None:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects  #: int: count or id
        else:
            self.id = id
