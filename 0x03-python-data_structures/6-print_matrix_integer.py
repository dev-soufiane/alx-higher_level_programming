#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """Function that prints a matrix of integers."""

    for row in matrix:
        print("{:d} {:d} {:d}".format(*row))
