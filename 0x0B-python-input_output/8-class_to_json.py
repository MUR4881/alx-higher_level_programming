#!/usr/bin/python3

# -*- coding: utf-8 -*-

"""A simple module containing a simple function, yep that is it
"""


def class_to_json(obj):
    """Access the dictionary description of an object,
    with simple data structure (list, dictionary, string, integer
    and boolean) for JSON serialization of an object

    Args:
        obj: instance of class

    Returns: dictionary description of the objects/class attribute
    """
    return obj.__dict__
