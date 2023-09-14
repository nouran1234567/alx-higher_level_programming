#!/usr/bin/python3

# function that prints a dictionary by ordered keys

def print_sorted_dictionary(own_dic):
    for z in sorted(own_dic.keys()):

        print("{}: {}".format(z, own_dic[z]))
