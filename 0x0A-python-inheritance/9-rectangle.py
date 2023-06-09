#!/usr/bin/python3
"""Defines a child Retangle class: inherits from BaseGeometry"""
Rectangle1 = __import__("8-rectangle").Rectangle


class Rectangle(Rectangle1):
    """Defines a retangle using BaseGeometry"""

    def __init__(self, width, height):
        """Initialize a rectangle

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """print() prints str() a description of the rectangle"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return (string)
