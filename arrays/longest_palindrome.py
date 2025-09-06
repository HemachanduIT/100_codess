# 1 232 5545455 909090 161
# the largest palindrome among the array elements is 5545455

def isPalindrome(n):
    if len(str(n))<2:
        return False
    k=n
    r=0
    while n!=0:
        r=r*10+n%10
        n//=10
    if r==k:
        return True
    else:
        return False
def longest_palindrome(s):
    c=-1
    for i in s:
        if isPalindrome(i):
            if i>c:
                c=i
    return c       
            
s=list(map(int,input().split()))
# n=len(s)
print("the largest palindrome among the array elements is",longest_palindrome(s))