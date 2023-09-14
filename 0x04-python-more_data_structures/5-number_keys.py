#!/usr/bin/python3

# function that returns the number of keys in a dictionary.

def number_keys(own_dic):
    z = 0
    list_keys = list(own_dic.keys())
    for y in list_keys:
        z += 1

    return (z)
