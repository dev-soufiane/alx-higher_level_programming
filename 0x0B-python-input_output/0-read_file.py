#!/usr/bin/python3
"""
    This module defines a function to read a text file (UTF8)
    and print its content to stdout.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.
    """
    with open(filename, "r", encoding="utf-8") as f:
        file_content = f.read()
        print(file_content, end='')
