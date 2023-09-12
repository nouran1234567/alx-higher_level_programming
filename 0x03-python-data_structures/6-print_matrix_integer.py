#!/usr/bin/python3

# function that prints a matrix of integers

def print_matrix_integer(matrix=[[]]):
    for z in range(len(matrix)):
        for y in range(len(matrix[z])):
            print("{:d}".format(matrix[z][y]), end="")
            if y != (len(matrix[z]) - 1):
                print(" ", end="")

        print("")
