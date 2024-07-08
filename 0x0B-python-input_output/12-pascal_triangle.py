#!/usr/bin/python3

# -*- coding: utf-8 -*-

"""A simple module containing a simple, but complex to implement
function
"""


def pascal_triangle(n):
    """A function that generate a lists of integers representing
    the Pascal's triangle of n

    Args:
        n: Where to stop along the pascal chain

    Return:
        The generate list of list (nx) pascal rows
    """
    pascal = []  #: list: list of lists
    pasPos = 1  #: int: The present pascalPosition/row
    # Generate if n is greater or equals to 1
    while (pasPos <= n):
        pasRow = [0] * pasPos  # Dynamically generating the pascal rows
        ix = 0  # Index
        # insert 1's in the first and last index, this still works
        # even if the array/pasPos is size one
        pasRow[ix] = pasRow[-1] = 1
        ix += 2  # Accounting for the two/1 used indexes
        # + 1 is added in loop condition, to support odd (pasPos)
        while (ix * 2 <= pasPos + 1):
            # adding two entries from previous row/array
            # copy has not been seen untill after row/array 1,
            # array 1 doesn't make it into this loop
            new_entry = copy[ix - 1] + copy[ix - 2]
            pasRow[ix - 1] = pasRow[-ix] = new_entry
            ix += 1
        copy = pasRow
        pasPos += 1
        pascal.append(copy)
    # Returning the list 'pascal' whether empty or not
    return pascal
