#!/usr/bin/python3
"""Defines a student class"""


class Student:
    """Represents a student"""
    def __init__(self, first_name, last_name, age):
        """Initializes a student

        Args:
            first_name (str): students first name
            last_name (str): students last name
            age (int): student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns serialization description(dictionary)

        if attrs is a list of strings, only attribute names contained in this
        list must be retrieved else retrieve all attributes

        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(item) == str for item in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Reloads from JSON

        Args
            json (dict): keyvalue pairs rep attributes
        """
        for k, v in json.items():
            setattr(self, k, v)
