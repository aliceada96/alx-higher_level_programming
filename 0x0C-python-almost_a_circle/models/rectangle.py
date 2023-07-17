#!/usr/bin/python3
"""Defines a rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Rep a rectangle that ingerits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a new rectangle

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
            x (int):
            y (int):
            id (int): instance id

        Raises:
            TypeError: <name of the attribute> must be an integer
            ValueError: <name of the attribute> must be > 0
            ValueError: <name of the attribute> must be >= 0(for x and y)
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get/set the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get/set the height of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get/set the height of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area value of the Rectangle instance"""
        return self.__height * self.__width

    def display(self):
        """Prints in stdout the Rectangle instance with the character #"""
        if self.height == 0 or self.width == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for i in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for j in range(self.width)]
            print("")

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
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif argc == 1:
                    self.width = arg
                elif argc == 2:
                    self.height = arg
                elif argc == 3:
                    self.x = arg
                elif argc == 4:
                    self.y = arg
                argc += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """print() prints str() a description of the rectangle"""
        string = "[" + str(self.__class__.__name__) + "] "
        string += "(" + str(self.id) + ") " + str(self.x) + "/" + str(self.y)
        string += " - " + str(self.width) + "/" + str(self.height)
        return (string)
