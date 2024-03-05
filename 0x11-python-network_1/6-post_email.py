#!/usr/bin/python3
"""
Use requests package to make a post request sending email param
and display body of response.
"""
import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    value = {'email': sys.argv[2]}
    r = requests.post(url, data=value)
    print(r.text)
