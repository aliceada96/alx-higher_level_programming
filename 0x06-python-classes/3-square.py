#!/usr/bin/python3

"""Defines a class called square"""


class Square:
    """defines the class square"""

    def __init__(self, size=0):
        """Initialize a square.
        Args:
        size (int): len of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size


def area(self):
    """Defines area which calculates area of square.

    Returns:
        Area of square
    """

    return (self.__size * self.__size)
