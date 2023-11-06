#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """Function that adds 2 tuples."""

    new_tuple = ()

    if len(tuple_a) < 2:
        tuple_a += (0,) * (2 - len(tuple_a))
    if len(tuple_b) < 2:
        tuple_b += (0,) * (2 - len(tuple_b))

    tuple_a = tuple_a[:2]
    tuple_b = tuple_b[:2]

    for i in range(2):
        new_tuple += (tuple_a[i] + tuple_b[i],)

    return new_tuple
