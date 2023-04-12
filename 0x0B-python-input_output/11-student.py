#!/usr/bin/python3
"""
Contains class student
"""


class Student:
    """Represents the  student"""
    def __init__(self, first_name, last_name, age):
        """Initializes  student"""
        self.first_name = first_name
        self.second_name = second_name
        self.age = age

    def to_json(self, attrs=None):
        """returns the dictionary representation of the Student instance
        with specified attributes"""
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for a in attrs:
            try:
                new_dict[a] = self.__dict__[a]
            except FileNotFoundError:
                pass
        return new_dict

    def reload_from_json(self, json):
        """this replaces all attributes of Student instance"""
        for key in json:
            try:
                setattr(self, key, json[key])
            except FileNotFoundError:
                pass
