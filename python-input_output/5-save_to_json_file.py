#!/usr/bin/python3
"""Defines a function that writes an object to a file as JSON."""
import json


def save_to_json_file(my_obj, filename):
    """Write the JSON representation of my_obj to filename.

    Args:
        my_obj: the object to serialize.
        filename: the path of the file to write.
    """
    with open(filename, "w", encoding="utf-8") as a_file:
        json.dump(my_obj, a_file)
