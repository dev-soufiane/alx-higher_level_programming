#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0:
        strdup = str[:n] + str[n + 1:]
        return (strdup)
    else:
        return (str)
