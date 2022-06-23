#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
from collections import Counter

def anagram(s):
    if len(s) & 1:
        return -1
    mid = len(s) // 2
    return sum((Counter(s[:mid]) - Counter(s[mid:])).values())