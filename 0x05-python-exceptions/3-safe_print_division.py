#!/usr/bin/python3

# function that divides 2 integers and prints the result

def safe_print_division(a, b):
    try:
        rzlt = a / b
    except (TypeError, ZeroDivisionError):
        rzlt = None
    finally:
        print("Inside result: {}".format(rzlt))

    return (rzlt)
