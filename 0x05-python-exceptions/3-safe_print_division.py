#!/usr/bin/python3
def safe_print_division(a, b):
    """Function that divides 2 integers and prints the result."""
    try:
        res = a / b
    except (ZeroDivisionError, TypeError):
        res = None
    finally:
        print("Inside result: {}".format(res))
        return res
