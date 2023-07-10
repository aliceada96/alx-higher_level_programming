#!/usr/bin/python3
"""Defines a function that looks up oject attributes & methods"""


def lookup(obj):
    """Returns list of avalilable attributes and methods of obj"""
    return (dir(obj))
