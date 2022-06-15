#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#
from functools import reduce
def getTotalX(a, b):
    lcm = reduce(lambda x, y : x * y // math.gcd(x, y), a)
    gcd = reduce(math.gcd, b)
    print(lcm, gcd)
    count = 0
    for i in range(lcm, gcd + 1, lcm):
        if gcd % i == 0:
            count+=1
    return count