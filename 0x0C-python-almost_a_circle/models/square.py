#!/usr/bin/python3
"""Contain class `Square` that inherits from `Rectangle` """


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class `Square` that inherits from `Rectangle`:

    In the file models/square.py
    Class Square inherits from Rectangle
    Class constructor: def __init__(self, size, x=0, y=0, id=None):
    Call the super class with id - this super call with use the logic
    of the __init__ of the Rectangle class
    All width, height, x and y validation must inherit from Rectangle -
    same behavior in case of wrong data
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Instantiate class object.
        Arguments
            size: size of square
            x: x axis offset
            y: y axis offset
            id: object id
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Return value of size"""
        return self.width

    @size.setter
    def size(self, value):
        """Set the value for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update values of all parameters"""
        if args and args != 0:
            position = 0
            for arg in args:
                if position == 0:
                    self.id = arg
                elif position == 1:
                    self.size = arg
                elif position == 2:
                    self.x = arg
                elif position == 3:
                    self.y = arg
                else:
                    return
                position += 1
        elif kwargs and len(kwargs) != 0:
            for i, j in kwargs.items():
                if i == "id":
                    self.id = j
                elif i == "size":
                    self.size = j
                elif i == "x":
                    self.x = j
                elif i == "y":
                    self.y = j

    def __str__(self):
        """
        __str__ print information for square

        Return [Square] (<id>) <x>/<y> - <size>
        """
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                  self.y, self.height))

    def to_dictionary(self):
        """Dictionary for attributes and values"""
        return {"id": self.id, "size": self.size,
                "x": self.x, "y": self.y}
