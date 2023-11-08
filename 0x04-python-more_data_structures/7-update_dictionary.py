#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """Function that replaces or adds key/value in a dictionary."""

    for k, val in a_dictionary.items():
        if k == key:
            a_dictionary[key] = value
            return a_dictionary

    a_dictionary[key] = value

    return a_dictionary
