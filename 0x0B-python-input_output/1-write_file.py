#!/usr/bin/python3

# -*- coding: utf-8 -*-

"""A simple module containing a simple file handling function
"""


def write_file(filename="", text=""):
    """a simple function, that over writes a file with some text

    Args:
        filename: The name or path to the file
        text: str: to overwrite the file with

    Return:
        The number of characters/bytes written into the file
    """

    # Open the file in write mode
    with open(filename, "w", encoding="utf-8") as f:
        # Over write the file
        return f.write(text)
