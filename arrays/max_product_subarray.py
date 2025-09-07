# 1 -2 -3 0 7 -8 -2
# the maximum sub-array product is 112


def subarray(s):
    res=s[0]
    for i in range(len(s)):
        product=1
        for j in range(i,len(s)):
            product*=s[j]
            res=max(res,product)
        # print(res)
    return res
s=list(map(int,input().split()))
print("the maximum sub-array product is",subarray(s))