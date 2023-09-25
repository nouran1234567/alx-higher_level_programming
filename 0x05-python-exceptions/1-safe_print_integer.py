#!/usr/bin/python3

# function that prints an integer with "{:d}".format()

def safe_print_integer(vlu):
    try:
        print("{:d}".format(vlu))
        return (True)
    except (TypeError, ValueError):

        return (False)
