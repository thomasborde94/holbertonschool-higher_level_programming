#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = number % 10
if number >= 0:
    print(f"Last digit of {number} is {n} ", end="")
else:
    print(f"Last digit of {number} is {-(10 - n)} ", end="")

if n > 5:
    print("and is greater than 5")
if n == 0:
    print("and is 0")
if (n < 6) and (n != 0):
    print("and is less than 6 and not 0")
