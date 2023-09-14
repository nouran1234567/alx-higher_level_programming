#!/usr/bin/python3

# function that creates a copy of the string

def remove_char_at(str, n):
    x = ""
    z = 0
    for c in str:
        if z != n:
            x += c
        z += 1
    return x
