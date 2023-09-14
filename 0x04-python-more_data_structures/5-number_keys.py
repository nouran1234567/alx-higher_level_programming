#!/usr/bin/python3

# function that returns the number of keys in a dictionary.

def number_keys(a_dictionary):
    z = 0
    list_keys = list(a_dictionary.keys())
    for y in list_keys:
        z += 1

    return (z)
