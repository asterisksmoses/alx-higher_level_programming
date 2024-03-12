#!/usr/bin/python3
import random
number = random.randint(-10, 10)

if number > 0:
    print("x{number} is positive")
elif number == 0:
    print("x{number} is zero")
elif number < 0:
    print("x{number} is negative")
