#!/usr/bin/python3
"""Defines a function that appends a string to a text file."""


def append_write(filename="", text=""):
    """Append text at the end of a UTF-8 file, creating it if needed.

    Args:
        filename: the path of the file to append to.
        text: the string to add.

    Returns:
        The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as a_file:
        return a_file.write(text)
