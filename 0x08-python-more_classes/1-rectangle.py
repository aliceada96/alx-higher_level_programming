#!/usr/bin/python3
"""Defines an empty rectangle class."""


class Rectangle:
    """Represents a rectangle."""
    def __init__(self, width=0, height=0):
        """Initialize a new rectangle

        Args:
            width (int): Width of the new rectangle
            height (int): Height of new rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Retrieves the width, a getter and setter(next)"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height"""
        return self.__height

    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value
