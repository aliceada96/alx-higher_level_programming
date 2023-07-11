#!/usr/bin/python3
"""Defines a function to covert JSON to string"""
import json


def from_json_string(my_str):
    """Returns JSON rep of an object

    Args:
        my_str: string to be converted
    """
    return json.loads(my_str)
