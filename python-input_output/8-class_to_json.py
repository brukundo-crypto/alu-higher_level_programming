#!/usr/bin/python3
"""Defines a function describing an instance as a dictionary."""


def class_to_json(obj):
    """Return the dictionary description of obj for JSON serialization.

    Args:
        obj: an instance whose attributes are all serializable.
    """
    return obj.__dict__.copy()
