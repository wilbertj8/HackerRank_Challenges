#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#

def countSort(arr):
    res = [ [] for _ in range(len(arr)) ]
    for index, element in enumerate(arr):
        x = int(element[0])
        s = element[1] if index >= len(arr) // 2 else "-"
        res[x].append(s)
    for array in res:
        for element in array:
            print(element, end = " ")

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
