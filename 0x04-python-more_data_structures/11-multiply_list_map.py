#!/usr/bin/python3

# function returns list with all values multiplied by number

def multiply_list_map(own_list=[], number=0):
    return (list(map((lambda z: z * number), own_list)))
