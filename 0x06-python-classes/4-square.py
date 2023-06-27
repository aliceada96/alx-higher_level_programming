#!/usr/bin/python3

"""Defines a class called square"""


class Square:
    """defines the class square"""

    def __init__(self, size=0):
        """Initialize a square.
        Args:
        size (int): len of square
        """
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value


def area(self):
    """Defines area which calculates area of square.

    Returns:
        Area of square
    """
    return (self.__size * self.__size)
