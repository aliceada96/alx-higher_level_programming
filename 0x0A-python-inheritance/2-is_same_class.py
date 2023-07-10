#!/usr/bin/python3
"""Defines a function that checks class similarirty"""


def is_same_class(obj, a_class):
    """Returns true if the object is an exact instance of specified class

    Args:
        obj (): object to be compared
        a_class: class thr object is compared to

    Return: True if it is an exact instance of the class, else false
    """
    if type(obj) == a_class:
        return True
    return False
