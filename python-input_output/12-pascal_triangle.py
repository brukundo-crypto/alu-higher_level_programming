#!/usr/bin/python3
"""Defines a function that builds Pascal's triangle."""


def pascal_triangle(n):
    """Return Pascal's triangle of n rows as a list of lists.

    Args:
        n: the number of rows.

    Returns:
        An empty list when n is less than or equal to 0.
    """
    triangle = []
    if n <= 0:
        return triangle
    for row_number in range(n):
        row = [1]
        if triangle:
            previous = triangle[-1]
            for index in range(len(previous) - 1):
                row.append(previous[index] + previous[index + 1])
            row.append(1)
        triangle.append(row)
    return triangle
