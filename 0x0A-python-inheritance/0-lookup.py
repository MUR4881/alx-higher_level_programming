#!/usr/bin/python3

# -*- coding: utf-8 -*-
"""Module Documentation

This module contains a function that returns a list of all the
attribute and methods of a given object

"""


def lookup(obj):
    '''Gets the list of available attributes and methods of an object

    Args:
        obj: A Reference/Alias to the object

    Return: A list containing the attributes of the object

    '''
    return (dir(obj))
