#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#

def separateNumbers(s):
    for i in range(len(s)):
        newS = s[:i+1]
        startingDigit = int(newS)
        
        digit = startingDigit
        while len(newS) < len(s):
            digit += 1
            newS += str(digit)
            if newS == s:
                print("YES {}".format(startingDigit))
                return
    print("NO")

if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)
