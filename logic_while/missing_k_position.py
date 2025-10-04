# input:
#     5
#     2 3 4 7 11
# output:
# 9

def missingvalue(k,arr):
    res=[]
    for i in range(1,1001):
        if i not in arr:
            res.append(i)
    return res[k-1]
k=int(input())
arr=list(map(int,input().split()))
print(missingvalue(k,arr))