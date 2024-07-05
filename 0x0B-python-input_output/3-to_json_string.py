#!/usr/bin/python3

# -*- coding: utf-8 -*-

"""A simple module, containing a simple object serialization function
"""
from json import dumps


def to_json_string(my_obj):
    """Generate the Json representation of a python object

    Args:
        my_obj: name/reference of the object

    Return:
        A json representation of the python object (as string)
    """
    return (dumps(my_obj))
