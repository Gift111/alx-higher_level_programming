#!/usr/bin/python3

"""Print all possible different combinations of two digits in ascending order. The two digits must be different"""
for 1stdigit in range(0, 10):
    for 2nddigit in range(1stdigit + 1, 10):
        if 1stdigit == 8 and 2nddigit == 9:
            print("{}{}".format(1stdigit, 2nddigit))
        else:
            print("{}{}".format(1stdigit, 2nddigit), end=",")
