#!/usr/bin/python3
"""

This module houses a function dedicated to text indentation.

"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each ".", "?", or ":".

    Parameters:
        text (str): The text to be printed (a string).

    Raises:
        TypeError: If text is not a string

    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    cnt = 0
    while cnt < len(text) and text[cnt] == " ":
        cnt = cnt + 1

    while cnt < len(text):
        print(text[cnt], end="")
        if text[cnt] == "\n" or text[cnt] in ".?:":
            if text[cnt] in ".?:":
                print("\n")
            cnt = cnt + 1
            while cnt < len(text) and text[cnt] == " ":
                cnt = cnt + 1
            continue
        cnt = cnt + 1
