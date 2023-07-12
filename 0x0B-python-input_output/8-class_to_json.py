#!/usr/bin/python3
"""Defines a function that returns JSON serialization desc"""


def class_to_json(obj):
    """Returns serialization description(dictionary)

    Args:
        obj: an instance of a class
    """
    return obj.__dict__
