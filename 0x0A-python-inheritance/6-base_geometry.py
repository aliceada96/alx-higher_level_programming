#!/usr/bin/python3
"""defines a base geometry class"""


class BaseGeometry:
    """A geometry module"""

    def area(self):
        """"if not implimemted"""
        raise Exception("area() is not implemented")
