#!/usr/bin/python3

"""Defines a class called square"""


class Square:
    """defines the class square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square.
        Args:
        size (int): len of square
        position (int): a tuple of 2 positive ints
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Defines area which calculates area of square.

        Returns:
            Area of square
        """
        return (self.__size * self.__size)

    def my_print(self):
        """Prints in stdout the square using # char"""
        if (self.__size == 0):
            print()

        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("{}".format('#'), end='')
                    if self.__position[0] > 0:
                        print("{}".format(self.__position[0]*' '), end='')
                print()
