#!/usr/bin/python3

# function that divides element by element 2 lists

def list_division(my_list_1, my_list_2, list_length):
    nov_list = []
    for z in range(0, list_length):
        try:
            rzlt = my_list_1[z] / my_list_2[z]
        except TypeError:
            print("wrong type")
            rzlt = 0
        except ZeroDivisionError:
            print("division by 0")
            rzlt = 0
        except IndexError:
            print("out of range")
            rzlt = 0
        finally:
            new_list.append(rzlt)

    return (nov_list)
