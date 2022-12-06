#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new = []
    for integer in range(len(my_list)):
        if my_list[integer] % 2 == 0:
            new.append(True)
        else:
            new.append(False)
    return new
