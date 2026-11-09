#!/usr/bin/python3
"""Defines a Square built on Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


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
