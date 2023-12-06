#!/usr/bin/python3
"""
    This module defines a function that creates
    an Object from a “JSON file”.
"""
import json


def load_from_json_file(filename):
    """
    Creates an Object from a “JSON file”.
    """
    with open(filename, "r", encoding="utf-8") as jf:
        jf_content = jf.read()
    return json.loads(jf_content)
