#!/usr/bin/python3
"""this defines the file-appending function"""


def append_write(filename="", text=""):
    """this Appends a string to the end of a UTF8 text file
    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.
    Returns:
        number of the characters appended
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
