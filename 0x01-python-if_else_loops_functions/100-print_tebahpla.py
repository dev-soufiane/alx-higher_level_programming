#!/usr/bin/python3

for i in range(ord('Z'), ord('A') - 1, -1):
    if i % 2 == 0:
        print("{}".format(chr(i + 32)), end='')
    else:
        print("{}".format(chr(i)), end='')
