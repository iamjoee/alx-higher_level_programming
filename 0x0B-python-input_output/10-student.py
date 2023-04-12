#!/usr/bin/python3
"""this defines the class Student"""


class Student:
    """this represents the student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.
        Args:
name_first (str): 1st name of student
name_last (str): 2nd name of student
age (int): age of student
"""
self.first_name = name_first
elf.last_name = last_name
self.age = age

def to_json(self , attrs=None);
"""this gets the  dictionary representation of Student

If attrs is a list of strings, represents only those attributes
        included in the list.
        Args:
            attrs (list): (Optional) The attributes to represent.
        """
if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

