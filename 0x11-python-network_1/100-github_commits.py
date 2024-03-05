#!/usr/bin/python3
"""Lists 10 most recent commits on a given GitHub repo"""
import sys
import requests


if __name__ == "__main__":
    # Get the arguments, arg1: repo name, arg2: repo owner
    url = "https://api.github.com/repos/{}/{}/commits".format(
            sys.argv[2], sys.argv[1])

    r = requests.get(url)
    commits = r.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
