#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    res = []
    for let in s:
        if let.islower():
            res.append(chr(97 + (ord(let) + k - 97) % 26))
        elif let.isupper():
            res.append(chr(65 + (ord(let) + k - 65) % 26))
        else:
            res.append(let)
    return "".join(res)
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
