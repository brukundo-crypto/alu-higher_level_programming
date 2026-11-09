#!/usr/bin/python3
"""Defines a function that builds an object from a JSON file."""
import json


def load_from_json_file(filename):
    """Return the object described by the JSON held in filename."""
    with open(filename, encoding="utf-8") as a_file:
        return json.load(a_file)
