#!/usr/bin/python3

# program that imports functions from file and handles basic operations

if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    argc = len(argv)
    if argc != 4:
        print('Usage: {} <a> <operator> <b>'.format(argv[0]))
        exit(1)
    ops = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div
    }
    if argv[2] in ops:
        x = int(argv[1])
        y = int(argv[3])
        op = ops[argv[2]]
        result = op(x, y)
        print('{:d} {:s} {:d} = {:d}'.format(x, argv[2], y, result))
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
    exit(0)

