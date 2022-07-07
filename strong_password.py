#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    digit, lower, upper, special = False, False, False, False
    for char in password:
        if not digit and char in "0123456789":
            digit = True
        elif not lower and char in "abcdefghijklmnopqrstuvwxyz":
            lower = True
        elif not upper and char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            upper = True
        elif not special and char in "!@#$%^&*()-+":
            special = True
    res = 4 - (upper + digit + lower + special)
    return 6 - n if n + res < 6 else res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
