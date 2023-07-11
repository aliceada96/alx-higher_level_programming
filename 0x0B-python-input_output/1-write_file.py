#!/usr/bin/python3
"""Defines a function that writes to a file"""


def write_file(filename="", text=""):
    """Returns appended text

    Args:
        filename: name of file
        text: text to be written to file
    """
    with open(filename, "w", encoding="UTF-8") as f:
        return (f.write(text))
