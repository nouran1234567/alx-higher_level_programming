#!/usr/bin/python3

# function that prints x elements of a list

def safe_print_list(my_list=[], x=0):
    z = 0
    for y in range(x):
        try:
            print("{}".format(my_list[y]), end="")
            z += 1
        except IndexError:
            break
    print("")

    return (z)
