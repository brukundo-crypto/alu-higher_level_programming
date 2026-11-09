#!/usr/bin/python3
"""Defines a function checking strict inheritance."""


def inherits_from(obj, a_class):
    """Return True if obj's class inherited from a_class.

    Returns False when obj is exactly an instance of a_class.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
