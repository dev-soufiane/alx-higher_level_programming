#!/usr/bin/python3
"""Using requests package, make a get request to URL
"""
import requests

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    r = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
