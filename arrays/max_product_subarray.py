# 1 -2 -3 0 7 -8 -2
# the maximum sub-array product is 112


def subarray(s,n):
    # res=s[0]
    # for i in range(len(s)):
    #     product=1
    #     for j in range(i,len(s)):
    #         product*=s[j]
    #         res=max(res,product)
    #     # print(res)
    # return res
    result = s[0]
 
    for i in range(n):
     
        mul = s[i]
       
        # traversing in current subarray
        for j in range(i + 1, n):
            result = max(result, mul)
            mul *= s[j]
         
         
        # updating the result for (n-1)th index.
        result = max(result, mul)
        # print(result)
    return result
s=list(map(int,input().split()))
n=len(s)
print("the maximum sub-say product is",subarray(s,n))