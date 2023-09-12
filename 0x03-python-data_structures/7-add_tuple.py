#!/usr/bin/python3

# function that adds 2 tuples

def add_tuple(tuple_a=(), tuple_b=()):
    len_z = len(tuple_a)
    len_y = len(tuple_b)
    if len_z == 0:
        z1 = 0
        z2 = 0
    elif len_z == 1:
        z1 = tuple_a[0]
        z2 = 0
    else:
        z1 = tuple_a[0]
        z2 = tuple_a[1]
    if len_y == 0:
        y1 = 0
        y2 = 0
    elif len_y == 1:
        y1 = tuple_b[0]
        y2 = 0
    else:
        y1 = tuple_b[0]
        y2 = tuple_b[1]
    own_tup = (z1 + y1, z2 + y2)

    return (own_tup)
