#!/usr/bin/python3

# function that prints the first x elements of a list and only integers

def safe_print_list_integers(my_list=[], x=0):
    geb = 0
    for z in range(0, x):
        try:
            print("{:d}".format(my_list[z]), end="")
            geb += 1
        except (ValueError, TypeError):
            continue
    print("")

    return (geb)
