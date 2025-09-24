from collections import Counter
def secondOccurence(s):
    # d=Counter(s)
    # # for i in s:
    # #     if i in d:
    # #         d[i]+=1
    # #     else:
    # #         d[i]=1
    # keys=list(d.keys())
    res=[]
    for i in range(len(s)):
        if s[i] in res:
            return i
        else:
            res.append(s[i])
        return -1
        
s=list(map(int,input().split()))
print(secondOccurence(s))