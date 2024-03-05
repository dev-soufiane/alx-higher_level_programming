#!/usr/bin/python3
""" Finds a peak in a list of unsorted integers using a binary search approach
"""


def find_peak(list_of_integers):
    """
    Args:
        list_of_integers (list): List of integers to find the peak of.
    Returns:
        int: Peak of list_of_integers or None if the list is empty.
    """
    size = len(list_of_integers)
    mid_end = size
    mid = size // 2

    if size == 0:
        return None

    while True:
        mid_end = mid_end // 2
        if (mid < size - 1 and
                list_of_integers[mid] < list_of_integers[mid + 1]):
            if mid_end // 2 == 0:
                mid_end = 2
            mid = mid + mid_end // 2
        elif mid_end > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
            if mid_end // 2 == 0:
                mid_end = 2
            mid = mid - mid_end // 2
        else:
            return list_of_integers[mid]
