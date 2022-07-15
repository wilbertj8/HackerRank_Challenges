#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
def isPalindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[~i]:
            return False
return True

def palindromeIndex(s):
    if isPalindrome(s):
        return -1
    for i in range(len(s) // 2):
        if s[i] != s[~i]:
            if isPalindrome(s[:i] + s[i+1:]):
                return i
            elif isPalindrome(s[:~i] + s[len(s)-i:]):
                return len(s) + ~i
            else:
                return -1
    return -1