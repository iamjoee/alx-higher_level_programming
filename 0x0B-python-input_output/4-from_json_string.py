#!/usr/bin/python3
"""this defines JSON to object function"""
import json


def from_json_string(my_str):
    """this returns Python object representation of JSON string"""
    return json.loads(my_str)
