#!/usr/bin/python3
"""this defines a file-writing function"""


def write_file(filename="", text=""):
    """this writes the string to the UtF8 text file
    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        number of the written characters
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
