#!/usr/bin/python3
"""this defines string to JSON function"""
import json


def to_json_string(my_obj):
    """ this returns the JSON representation of the string object"""
    return json.dumps(my_obj)
