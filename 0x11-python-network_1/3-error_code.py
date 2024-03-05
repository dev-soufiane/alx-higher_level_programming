#!/usr/bin/python3
"""
Take in a URL, sends request to URL, dispaly body of response in
utf-8 and manage urllib's error exceptions.
"""
import sys
import urllib.request
import urllib.error

if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.URLError as err:
        print("Error code: {}".format(err.code))
