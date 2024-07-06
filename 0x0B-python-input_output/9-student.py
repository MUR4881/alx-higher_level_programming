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

    def to_json(self):
        """Retrieve a dictionary representation of a Student instance

        Returns: The dictionary representation of the Student
        """
        return self.__dict__
