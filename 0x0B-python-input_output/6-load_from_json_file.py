#!/usr/bin/python3
"""defines a function that creates an object from JSON file"""
import json


def load_from_json_file(filename):
    """Loads object from a JSON file

    Args:
        filename: name of file
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
