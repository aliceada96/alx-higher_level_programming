#!/usr/bin/python3
"""Defines a function that appends text to a file"""


def append_write(filename="", text=""):
    """Returns appended text

     Args:
        filename: name of file
        text: text to be appended
    """
    with open(filename, "a", encoding="UTF-8") as f:
        return (f.write(text))
