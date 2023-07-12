#!/usr/bin/python3
"""Defines a function thats writes object to a txt file"""
import json


def save_to_json_file(my_obj, filename):
    """Uses JSON to write an object to txt file
    
    Args:
        my_obj: Object to be saved
        filename: name of file
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
