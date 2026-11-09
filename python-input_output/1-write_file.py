#!/usr/bin/python3
"""Defines a function that writes a string to a text file."""


def write_file(filename="", text=""):
    """Write text to a UTF-8 file, replacing anything already there.

    Args:
        filename: the path of the file to write.
        text: the string to write.

    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as a_file:
        return a_file.write(text)
