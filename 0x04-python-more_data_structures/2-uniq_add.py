#!/usr/bin/python3

# function that adds all unique integers in a list

def uniq_add(my_list=[]):
    own_list = set(my_list)
    z = 0
    for y in own_list:
        z += y

    return (z)
