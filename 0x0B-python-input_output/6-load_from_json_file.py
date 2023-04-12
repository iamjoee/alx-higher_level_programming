#!/usr/bin/python3
"""this defines the JSON file-reading function"""
import json


def load_from_json_file(filename):
    """Creates the Python object from the JSON file"""
    with open(filename) as f:
        return json.load(f)
