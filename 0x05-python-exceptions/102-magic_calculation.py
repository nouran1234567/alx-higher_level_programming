#!/usr/bin/python3

# Python function def magic_calculation(a, b)

def magic_calculation(a, b):
    rzlt = 0
    for z in range(1, 3):
        try:
            if z > a:
                raise Exception('Too far')
            else:
                rzlt += a ** b / z
        except Exception:
            rzlt = b + a
            break
    return (rzlt)
