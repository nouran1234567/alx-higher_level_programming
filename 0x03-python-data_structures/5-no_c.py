#!/usr/bin/python3

# function that removes all characters c and C from a string

def no_c(my_string):
    own_str = ''
    for z in my_string:
        if z != 'c' and z != 'C':
            own_str += z

    return (own_str)
