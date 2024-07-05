#!/usr/bin/python3

# -*- coding: utf-8 -*-

"""A simple module containing a simple file handling function
"""


def append_write(filename="", text=""):
    """a simple function, that appends text to a file

    Args:
        filename: The name or path to the file
        text: str: to appends the file with

    Return:
        The number of characters/bytes appended into the file
    """

    # Open the file in append mode
    with open(filename, "a", encoding="utf-8") as f:
        # append to the file
        return f.write(text)
