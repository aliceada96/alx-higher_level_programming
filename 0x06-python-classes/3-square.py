#!/usr/bin/python3

"""Defines a class called square"""


class Square:
    """defines the class square

    Attributes:
        __size (int): length of square object
    """

    def __init__(self, size=0):
        """Initialize a square class instance.

        Args:
            size (int): len of square

        Returns:
             None

        Raises:
            Typerror: if size type is not int
            ValueError: if size >= 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Defines area which calculates area of square

        Returns:
            Area of square
        """

        return (self.__size * self.__size)
