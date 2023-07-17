#!/usr/bin/python3
"""Defines the model base class."""
import json


class Base:
    """Represents the base class

    Attrinbutes:
        __nb_objects (int): Number of instances
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the base class

        Args:
            id (int): id of instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries

        Args:
             list_dictionaries (list): list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file

        Args:
            list_objs (list): list of inherited instances
        """
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as json_file:
            if list_objs is None:
                json_file.write("[]")
            else:
                dicts_list = [o.to_dictionary() for o in list_objs]
                json_file.write(Base.to_json_string(dicts_list))

    @staticmethod
    def from_json_string(json_string):
        """Teturns the list of the JSON string representation json_string

        Args:
            json_string (str): reps a list of dictionaries
        """
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set

        Args:
            **dictionary(dict): double ptr to dictionary
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new_cls = cls(1, 1)
            else:
                new_cls = cls(1)
            new_cls.update(**dictionary)
            return new_cls

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as json_file:
                dicts_list = Base.from_json_string(json_file.read())
                return [cls.create(**d) for d in dicts_list]
        except IOError:
            return []
