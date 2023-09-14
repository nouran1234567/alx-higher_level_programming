#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda rz: list(map(lambda cz: cz**2, rz)), matrix))
