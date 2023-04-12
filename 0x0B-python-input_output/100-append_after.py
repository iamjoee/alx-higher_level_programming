#!/usr/bin/python3
"""this defines a text file insertion function"""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing the given string in the file
    Args:
        filename (str): name of file
        search_string (str): The string to search for within the file.
        new_string (str): string to insert
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
