#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """Function that returns the number of keys in a dictionary."""

    sorted_keys = sorted(a_dictionary.keys())
    for key in sorted_keys:
        print("{}: {}".format(key, a_dictionary[key]))
