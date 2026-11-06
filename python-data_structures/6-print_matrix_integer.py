#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return
    for row in matrix:
        for index, number in enumerate(row):
            if index != 0:
                print(" ", end="")
            print("{:d}".format(number), end="")
        print()
