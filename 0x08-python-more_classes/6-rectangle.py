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

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        """Reurns area of rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Reurns perimeter of rectngle"""
        if (self.__width == 0 or self.__height == 0):
            return (0)
        return (self.__height * 2) + (self.__width * 2)

    def __str__(self):
        """Prints the rectangle with the character #."""
        if self.__height == 0 or self.__width == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
