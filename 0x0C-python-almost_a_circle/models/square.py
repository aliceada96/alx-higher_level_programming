#!/usr/bin/python3
"""Defines a rectangle class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Rep a rectangle that ingerits from Base"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a new rectangle

        Args:
            size width (int): size of square
            x (int):
            y (int):
            id (int): instance id

        Raises:
            TypeError: <name of the attribute> must be an integer
            ValueError: <name of the attribute> must be > 0
            ValueError: <name of the attribute> must be >= 0(for x and y)
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get/set the width of the Rectangle."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute:

        Args:
            *args (ints): attribute values
                1st argument should be the id attribute
                2nd argument should be the width attribute
                3rd argument should be the height attribute
                4th argument should be the x attribute
                5th argument should be the y attribute
            **kwargs (dict): New key/value pairs of attributes
        """
        if args and len(args) != 0:
            argc = 0
            for arg in args:
                if argc == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif argc == 1:
                    self.size = arg
                elif argc == 3:
                    self.x = arg
                elif argc == 4:
                    self.y = arg
                argc += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = v
                elif k == "size":
                    self.width = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """print() prints str() a description of the rectangle"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += "(" + str(self.id) + ") " + str(self.x) + "/" + str(self.y)
        string += " - " + str(self.width)
        return (string)
