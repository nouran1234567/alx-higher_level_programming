#!/usr/bin/python3

# function that prints a dictionary by ordered keys

def print_sorted_dictionary(my_dict):
    for z in sorted(my_dict.keys()):

        print("{}: {}".format(z, my_dict[z]))
