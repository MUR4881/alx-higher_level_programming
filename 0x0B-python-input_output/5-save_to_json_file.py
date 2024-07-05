#!/usr/bin/python3

# -*- coding: utf-8 -*-

"""A simple module, containing  a simple function, which store a json
represetantion of a python object in a file
"""
from json import dump


def save_to_json_file(my_obj, filename):
    """Save Json representation of python, object
    to a json file.

    Args:
        my_obj: Reference/Name of python object
        filename: The name of the file
    """

    # Open the file
    with open(filename, "w", encoding="utf-8") as f:
        # Convert to Json representation and write to the file
        dump(my_obj, f)
