#!/usr/bin/python3

def common_elements(set_1, set_2):
    """Function that returns a set of common elements in two sets."""

    common_set = set()

    for e in set_1:
        for el in set_2:
            if e == el:
                common_set.add(e)

    return common_set
