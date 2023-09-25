#!/usr/bin/python3

# function that prints an integer

import sys


def safe_print_integer_err(vlu):
    try:
        print("{:d}".format(vlu))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)

        return (False)
