#!/usr/bin/python3
"""Defines a list subclass that can print itself sorted."""


class MyList(list):
    """Represents a list with an extra sorted printing method."""

    def print_sorted(self):
        """Print the list in ascending order, leaving the list unchanged."""
        print(sorted(self))
