#!/usr/bin/python3
"""Defines a Square built on Rectangle."""


class BaseGeometry:
    """Represents the base of every geometry shape."""

    def area(self):
        """Raise an exception, since area is not implemented here.

        Raises:
            Exception: always.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Check that value is a positive integer.

        Args:
            name: the name used in the error messages.
            value: the value to validate.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


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


class Square(Rectangle):
    """Represents a square, a rectangle with equal sides."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size: the length of every side, a positive integer.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
