#!/usr/bin/python3
"""Defines a function that serializes an object to JSON."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of my_obj as a string."""
    return json.dumps(my_obj)
