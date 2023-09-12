#!/usr/bin/python3

# function replaces element at specific position without modifying the main

def new_in_list(my_list, idx, element):
    if (idx < 0) or (idx > (len(my_list)-1)):
        return my_list
    coli = [x for x in my_list]
    coli[idx] = element

    return coli
