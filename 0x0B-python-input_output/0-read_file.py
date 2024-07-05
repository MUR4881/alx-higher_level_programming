#!/usr/bin/python3

# -*- coding: utf-8 -*-

"""Simple module containing, a simple function
"""


def read_file(filename=""):
    """Reads from a text file unto stdout(terminal (screen))

    Args:
        filename: The path/name of the text file

    """

    # open the file
    with open(filename, "r", encoding="utf-8") as f:
        # continue reading till file end
        for line in f:
            print(line, end="")
