#!/usr/bin/python3

# -*- coding: utf-8 -*-

"""A simple python script that appends command line arguments to a list
and  stores them to a json file as json objects
"""

# Import Dependencies
from sys import argv
from json import dump
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"
# Reading from file
try:
    lst = load_from_json_file(filename)  # :list : a list to store args
except Exception:
    lst = []

if lst is None:  # Incase of an empty file
    lst = []

# Reading and appending command line arguments
for arg in argv:
    if arg != argv[0]:
        lst.append(arg)

# Saving to json file
save_to_json_file(lst, filename)
