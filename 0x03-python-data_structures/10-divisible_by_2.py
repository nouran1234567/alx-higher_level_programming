#!/usr/bin/python3

# function that finds all multiples of 2 in a list

def divisible_by_2(my_list=[]):
    own_multi = []
    for z in range(len(my_list)):
        if my_list[z] % 2 == 0:
            own_multi.append(True)
        else:
            own_multi.append(False)

    return (own_multi)
