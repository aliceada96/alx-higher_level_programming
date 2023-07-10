#!/usr/bin/python3
"""defines a base geometry class"""


class BaseGeometry:
    """A geometry module"""

    def area(self):
        """"if not implimemted"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value

        Args:
            name (str): name of parameter
            value (int): parameter to ve validated

        Raises:
            TypeError: if value is noy an int
            ValueErrror: if value is <= o.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
