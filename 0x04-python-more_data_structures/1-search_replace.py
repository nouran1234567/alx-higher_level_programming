#!/usr/bin/python3

# function that replaces all occurrences of an element by another

def search_replace(my_list, search, replace):
    own_list = list(map(lambda z: replace if z == search else z, own_list))

    return (own_list)
