#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    last_num = number % 10
else:
    last_num = (number % -10)
msg = (f"Last digit of {number} is {last_num} and is")
if last_num == 0:
    print(msg, "0")
elif last_num > 5:
    print(msg, "greater than 5")
else:
    print(msg, "less than 6 and not 0")
