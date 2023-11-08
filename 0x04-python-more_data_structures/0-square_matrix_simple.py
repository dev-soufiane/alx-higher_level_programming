#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """Function that computes the square value of all integers of a matrix."""

    sqr_matrix = []
    for row in matrix:
        new_row = []
        for n in row:
            new_row.append(n**2)
        sqr_matrix.append(new_row)

    return sqr_matrix
