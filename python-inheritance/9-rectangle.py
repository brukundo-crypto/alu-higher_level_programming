#!/usr/bin/python3
"""Defines a Rectangle that knows its area."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle with validated private sides."""

    def __init__(self, width, height):
        """Initialize a new Rectangle.

        Args:
            width: the width, a positive integer.
            height: the height, a positive integer.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the rectangle description."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
