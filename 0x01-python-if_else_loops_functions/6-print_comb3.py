#!/usr/bin/python3

"""Print all possible different combinations of two digits in ascending order. The two digits must be different"""
for 1digit in range(0, 10):
    for 2digit in range(1digit + 1, 10):
        if 1digit == 8 and 2digit == 9:
            print("{}{}".format(1digit, 2digit))
        else:
            print("{}{}".format(1digit, 2digit), end=",")
