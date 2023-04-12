#!/usr/bin/python3
"""this defines the Python class to JSON function"""


def class_to_json(obj):
    """this returns a dictionary represntation of the  simple data structure"""
    return obj.__dict__
