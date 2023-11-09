#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    """Function that returns a new dictionary
    with all values multiplied by 2"""

    mul_dict = {}

    for key, val in a_dictionary.items():
        mul_dict[key] = val * 2

    return mul_dict
