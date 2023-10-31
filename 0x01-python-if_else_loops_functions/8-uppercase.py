#!/usr/bin/python3
def uppercase(str):
    for c in str:
        print(chr(ord(c) - 32), end='')
    print()
