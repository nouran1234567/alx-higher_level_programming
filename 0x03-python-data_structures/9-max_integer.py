#!/usr/bin/python3

# function that finds the biggest integer of a list

def max_integer(my_list):
    if len(my_list) == 0:
        return (None)
    big_num = my_list[0]
    for x in range(len(my_list)):
        if my_list[x] > big_num:
            big_num = my_list[x]

    return (big_num)
