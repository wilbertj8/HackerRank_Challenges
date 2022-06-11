#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def findMedian(arr):
    return sorted(arr)[len(arr) // 2]