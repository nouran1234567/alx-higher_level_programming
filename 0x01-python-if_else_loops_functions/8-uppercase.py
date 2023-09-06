#!/usr/bin/python3
def islower(c):
    if ord(c) <= ord("z") and ord(c) >= ord("a"):
        return True
    else:
        return False


def uppercase(str):
    for c in str:
        if islower(c):
            print("{:c}".format(ord(c) - 32), end="")
    print("{:c}".format(ord(c))
