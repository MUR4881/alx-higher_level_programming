#!/usr/bin/python3

# -*- coding: utf-8 -*-

"""A simple module containing a complex function that append a text to some
line of a file
"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file after each line containing
    a specific string

    Args:
        filename: The name of the file to search from
        search_string: The string being search for in each line
        new_string: The String to be appended after the line
    """
    index = 0  # For modifying the list of file lines
    new_string = "\n" + new_string
    # Read the whole file as lines
    with open(filename, "r") as f:
        line_list = f.readlines()

    # Scan through each line, split as list
    for line in line_list:
        if search_string in line:
            modline = line.split("\n")  # split the string as list
            modline.append(new_string)  # append
            line = "".join(modline)  # Convert back to a string
            #  insert the modified string
            line_list[index] = line
        index += 1

    with open(filename, "w") as f:
        f.writelines(line_list)
