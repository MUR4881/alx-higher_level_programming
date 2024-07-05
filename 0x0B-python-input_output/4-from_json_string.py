#!/usr/bin/python3

# -*- coding: utf-8 -*-

"""A simple module, containing a simple object serialization function
"""
from json import loads


def from_json_string(my_obj):
    """Generate a python object from Json representation (string)

    Args:
        my_obj: str: The string

    Return:
        A Python object
    """
    return (loads(my_obj))
