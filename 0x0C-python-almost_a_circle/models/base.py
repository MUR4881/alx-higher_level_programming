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

    @classmethod
    def save_to_file(cls, list_objs):
        '''Saves list of instances as dictionary,
        to a file named after their __class__name

        Args:
            list_objs: list of object/instances
        '''
        lst = []  #: list: of dicts of the instance attribute
        # Genete dict of instances and append to lst
        if list_objs is not None:
            for obj in list_objs:
                lst.append(obj.to_dictionary())
        # convert list_objs to json string
        jstring = cls.to_json_string(lst)
        # check the the object class and define class name
        # Open the file in over-write mode
        with open(f'{cls.__name__}.json', 'w', encoding='utf-8') as file:
            # Dump the string into the file
            file.write(jstring)

    @staticmethod
    def from_json_string(json_string):
        '''Convert a json string to a python object.
        used for a list of dict in this case
        '''
        if json_string is None:
            return []
        return loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''Create a new of instance of the caller's class

        Args:
            dictionary: a dictionary of attributes and values for the object

        return the new insance
        '''
        # Create new object with dummy variables
        if cls.__name__ == "Rectangle":
            new_obj = cls(1, 1)
        if cls.__name__ == "Square":
            new_obj = cls(1)
        if cls.__name__ == "Base":
            new_obj = cls()
        # update with the passed values passed
        new_obj.update(**dictionary)
        return new_obj

    @classmethod
    def load_from_file(cls):
        '''Load and returns a list of instances from a json file
        (a json file, contain a list of dict of object attributes
        '''
        # Firstly, read from the file
        objlist = []
        try:
            with open(f'{cls.__name__}.json', 'r', encoding="utf-8") as file:
                # Read from the file
                jstring = file.read()
        except FileNotFoundError:
            return objlist

        # Convert json string to python list of dict
        dictlist = cls.from_json_string(jstring)
        # Then create and append object to list
        for dct in dictlist:
            # Creating object and appending to list
            objlist.append(cls.create(**dct))
        return objlist
