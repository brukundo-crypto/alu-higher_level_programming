#!/usr/bin/python3
"""Defines a function that prints the contents of a text file."""


def read_file(filename=""):
    """Read a UTF-8 text file and print it to stdout.

    Args:
        filename: the path of the file to read.
    """
    with open(filename, encoding="utf-8") as a_file:
        print(a_file.read(), end="")
