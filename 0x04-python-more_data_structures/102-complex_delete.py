#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    """
    Function that deletes keys with a specific value in a dictionary.
    """

    delete_keys = []

    for key, val in a_dictionary.items():
        if val == value:
            delete_keys.append(key)
    for key in delete_keys:
        del a_dictionary[key]

    return a_dictionary
