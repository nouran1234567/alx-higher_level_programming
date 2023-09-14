#!/usr/bin/python3

# function that deletes a key in a dictionary

def simple_delete(own_dic, key=""):
    own_dic.pop(key, None)

    return own_dic
