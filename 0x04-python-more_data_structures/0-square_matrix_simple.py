#!/usr/bin/python3

# function that computes the square value of all integers

def square_matrix_simple(matrix=[]):
    sq_mat = []
    for line in matrix:
        sq_mat.append([x**2 for x in line])

    return sq_mat
