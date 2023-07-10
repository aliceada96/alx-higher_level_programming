#!/usr/bin/python3
"""Defines a function that checks subclass"""


def inherits_from(obj, a_class):
    """Returns true only if obj is a subclass

    Args:
        obj (): object to be compared
        a_class: class thr object is compared to

    Returns: True if obj is a subclass, else false
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
