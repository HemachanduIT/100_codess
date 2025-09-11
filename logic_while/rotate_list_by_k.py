# 1 2 3 4 5 6 7
# 3
# [5, 6, 7, 1, 2, 3, 4]

def rotatedList(s,k):
    k=k%len(s)
    # res=[]
    # for i in range(k+1,len(s)):
    #     res.append(s[i])
    # for i in range(k+1):
    #     res.append(s[i])
    res=s[k+1:]+s[:k+1]
    return res

s=list(map(int,input().split()))
k=int(input())
print(rotatedList(s,k))