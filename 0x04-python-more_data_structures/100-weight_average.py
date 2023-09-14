#!/usr/bin/python3

# function that returns the weighted average of all integers tuple

def weight_average(own_list=[]):
    if not own_list:
        return 0
    x = 0
    y = 0
    for tup in own_list:
        x += tup[0] * tup[1]
        y += tup[1]

    return (x / y)
