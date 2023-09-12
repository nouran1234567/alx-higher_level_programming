#!/usr/bin/python3

#function that prints a matrix of integers

def print_matrix_integer(matrix=[[]]):
    for z in matrix:

        print(' '.join('{:d}'.format(y)for y in z))
