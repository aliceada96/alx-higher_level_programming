#!/usr/bin/python3
"""Defines a function that checks if obj is an instance of a class"""


def is_kind_of_class(obj, a_class):
    """Returns True if the object is an instance of/inherits from

    Args:
        obj (): object to be compared
        a_class: class thr object is compared to

    Return: True if obj isinstance of/class or inherits class, else false
    """
    if isinstance(obj, a_class):
        return True
    return False
