#!/usr/bin/python3
"""
Define a class `` Rectangle`` with size ``width`` and ``height``
"""


class Rectangle:
    """
    Defines a rectangle with size `` width`` and ``height``
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize ``Rectangle``

        Args:
            width: width of ``Rectangle``
            height: height of ``Rectangle``
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ Returns the width of ``Rectangle`` """
        return self.__width

    @width.setter
    def width(self, value):
        """
        gets width of ``Rectangle``

        Arg:
            value (int): value of thd width of ``Rectangle``
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Return the height of ``Rectangle`` """
        return self.__height

    @height.setter
    def height(self, value):
        """
        gets the height of ``Rectangle``

        Arg:
            value (int): value of height of ``Rectangle``
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Gets the area of ``Rectangle`` """
        return self.__height * self.__width

    def perimeter(self):
        """ Get the perimeter of ``Rectangle`` """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * self.__height + 2 * self.__width

    def __str__(self):
        """ String representation of ``Rectangle`` for users """
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        for i in range(self.__height):
            for j in range(self.__width):
                string = string + str(self.print_symbol)
            if i != self.__height - 1:
                string += "\n"
        return string

    def __repr__(self):
        """ String repressentation of ``Rectangle`` """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ Delete ``Rectangle`` """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compare 2 rectangles for the bigger one.

        Args:
            rect_1 (``Rectangle``): Rectangle one
            rect_2 (``Rectangle``): Rectangle two

        Return:
            Either the bigger rectangle or rect_1 if both has equal area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area == rect_2.area:
            return rect_1
        if rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """ Make rectangle a square """
        return cls(size, size)
