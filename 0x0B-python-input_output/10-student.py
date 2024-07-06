#!/usr/bin/python3

# -*- coding: utf-8 -*-

"""A simple module containing A simple student class definition
"""


class Student:
    """A simple Student class that defines student with 3
    attributes.
    """

    def __init__(self, first_name, last_name, age):
        """Initializing, 3 of the student attributes
        """
        self.first_name = first_name  #: str: Name
        self.last_name = last_name  #: str: Surname
        self.age = age  #: int: Student age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student instance

        Returns: The dictionary representation of the Student
        """
        # Check, if the attrs, list is not none and contains string
        # make a new dict
        new_dict = {}
        if attrs is not None and type(attrs) is list:
            # popping attributes that are not in the list
            for key in self.__dict__:
                if key in attrs:
                    new_dict[key] = self.__dict__[key]
        # If new_dict is empty
            return new_dict
        # Else return the original dict
        return self.__dict__
