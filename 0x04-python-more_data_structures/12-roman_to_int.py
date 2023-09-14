#!/usr/bin/python3

# Create a function def roman_to_int(roman_string)

def roman_to_int(roman_string: str):
    if roman_string is None or type(roman_string) != str:
        return 0
    info = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    numbers = [info[y] for y in roman_string] + [0]
    agi = 0
    for z in range(len(numbers) - 1):
        if numbers[z] >= numbers[z+1]:
            agi += numbers[z]
        else:
            agi -= numbers[z]

    return agi
