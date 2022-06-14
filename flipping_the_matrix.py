#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#
def flippingMatrix(matrix):
    # Write your code here
    n = len(matrix) // 2
    output = 0
    for i in range(n):
        for j in range(n):
            output += max(matrix[i][j], matrix[i][~j], matrix[~i][j], matrix[~i][~j])
    return output