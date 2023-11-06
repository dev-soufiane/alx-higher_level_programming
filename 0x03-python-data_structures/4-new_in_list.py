#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """Function that replaces an element in a list at a specific
    position without modifying the original list"""

    my_list_copy = my_list.copy()
    if idx < 0 or idx >= len(my_list):
        return my_list_copy
    my_list_copy[idx] = element
    return my_list_copy
