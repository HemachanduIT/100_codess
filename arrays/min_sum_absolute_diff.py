# 1 2 3 4 5
# the  Minimum sum of absolute difference of given array 5

def minSum(s):
    s.sort()
    summ=0
    summ+=abs(s[0]-s[1])
    summ+=abs(s[len(s)-1]-s[len(s)-2])
    for i in range(1,len(s)-1):
        summ+=min(abs(s[i]-s[i-1]),abs(s[i]-s[i+1]))
    return summ

s=list(map(int,input().split()))
print("the  Minimum sum of absolute difference of given array",minSum(s))