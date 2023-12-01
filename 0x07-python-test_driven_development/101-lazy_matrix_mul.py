#!/usr/bin/python3
"""
Matrix Multiplication with NumPy
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices using NumPy.

    Args:
        m_a (list of lists of ints or floats): First matrix.
        m_b (list of lists of ints or floats): Second matrix.

    Returns:
        list of lists: Resultant matrix after multiplication.
    """
    return np.matmul(m_a, m_b)
