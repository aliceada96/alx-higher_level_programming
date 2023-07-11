#!/usr/bin/python3
"""Defines a function that reads contents of a file"""


def read_file(filename=""):
    """Returns read contents of a file

    Args:
        filename: Name of file whose contents are to be read
    """
    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")
