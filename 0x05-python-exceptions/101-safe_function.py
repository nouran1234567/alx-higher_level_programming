#!/usr/bin/python3

# function that executes a function safely

import sys

def safe_function(fct, *args):
    try:
        rzlt = fct(*args)
        return (rzlt)
    except Exception as z:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)

        return (None)
