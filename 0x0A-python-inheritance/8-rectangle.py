#!/usr/bin/python3
"""defines a child Retangle class: inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a retangle using BaseGeometry"""

    def __init__(self, width, height):
        """Initialize a rectangle

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__heght = height
