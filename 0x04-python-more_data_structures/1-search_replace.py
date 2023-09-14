#!/usr/bin/python3

# function that replaces all occurrences of an element by another

def search_replace(my_list, search, replace):

    return [replace if search == z else z for z in my_list]
