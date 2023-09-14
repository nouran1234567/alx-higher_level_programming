#!/usr/bin/python3

# function that deletes keys with a specific value in a dictionary

def complex_delete(own_dic, value):
    tmp = own_dic.copy()
    for z, y in tmp.items():
        if value == y:
            own_dic.pop(z)

    return own_dic
