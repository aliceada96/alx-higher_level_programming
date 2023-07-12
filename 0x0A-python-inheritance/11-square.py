"""Defines a child square class: inherits from Rectangle"""
Square1 = __import__("10-square").Square


class Square(Square1):
    """Represents a square inherited from prev task"""

    def __str__(self):
        """Returns new descriprion fro inherited square"""
        rename_ = "Square"
        return super().__str__().replace('Square1', rename_)
