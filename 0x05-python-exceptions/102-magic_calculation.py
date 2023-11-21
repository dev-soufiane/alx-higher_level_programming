#!/usr/bin/python3
def magic_calculation(a, b):
    """Function that does exactly the same as Python bytecode"""
    res = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too Far")
            else:
                res += (a ** b) / i
        except (Exception):
            res = b + a
            break
    return res
