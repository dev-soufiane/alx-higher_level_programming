#!/usr/bin/python3
"""
    This module defines a script that adds all arguments to a Python list,
    and then save them to a file.
"""
from sys import argv
from os.path import exists


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


argc = len(argv)
myList = []

if exists("add_item.json"):
    myList = load_from_json_file("add_item.json")

if argc == 1:
    save_to_json_file(myList, "add_item.json")
else:
    for index in range(1, argc):
        myList.append(argv[index])
    save_to_json_file(myList, "add_item.json")
