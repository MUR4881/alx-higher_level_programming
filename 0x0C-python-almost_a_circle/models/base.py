#!/usr/bin/python3

# -*- encoding: utf-8 -*-

"""A simple module, entailing a simple Base class called Base
"""
from json import load, loads, dump, dumps


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
            Base.__nb_objects += 1
            self.id = Base.__nb_objects  #: int: count or id
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Generates a JSON string representation
        of list_dictionaries

        Return: The json string
        '''
        if list_dictionaries is None:
            return "[]"
        return dumps(list_dictionaries)
