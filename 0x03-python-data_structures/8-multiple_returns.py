#!/usr/bin/python3

# function returns tuple with length of string & first character

def multiple_returns(sentence):
    size = len(sentence)
    first_letter = sentence[0] if size > 0 else "None"
    own_tup = size, first_letter

    return(own_tup)

