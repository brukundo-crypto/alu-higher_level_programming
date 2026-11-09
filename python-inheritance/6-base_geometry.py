#!/usr/bin/python3
"""Defines a BaseGeometry class with an unimplemented area."""


class BaseGeometry:
    """Represents the base of every geometry shape."""

    def area(self):
        """Raise an exception, since area is not implemented here.

        Raises:
            Exception: always.
        """
        raise Exception("area() is not implemented")
