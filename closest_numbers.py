#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

from collections import defaultdict
def closestNumbers(arr):
    arr.sort()
    dic = defaultdict(list)
    mn = math.inf
    for i in range(len(arr) - 1):
        curr = abs(arr[i] - arr[i+1])
        dic[curr].extend([arr[i], arr[i + 1]])
        mn = min(curr, mn)
    return dic[mn]
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
