#!/usr/bin/python3

# -*- coding: utf-8 -*-

"""A simple module, containing  a simple function, loads a json
represetantion of a python object from a json file
"""
from json import load


def load_from_json_file(filename):
    """Initialize Python object, with it json representation
    from a json file.

    Args:
        filename: The name of the Json file
    """

    # Open the file
    with open(filename, "r", encoding="utf-8") as f:
        # Read the string from the file, and convert to Python Object
        return load(f)
