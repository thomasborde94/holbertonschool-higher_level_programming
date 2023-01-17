#!/usr/bin/python3
def print_last_digit(number):
    digit = number % 10
    if number > 0:
        print("{}".format(digit), end="")
        return digit
    else:
        print("{}".format(10 - digit), end="")
        return (10 - digit)
