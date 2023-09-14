#!/usr/bin/python3

# function that returns a key with the biggest integer value

def best_score(own_dic):
    return max(own_dic, key=own_dic.get) if own_dic else None
