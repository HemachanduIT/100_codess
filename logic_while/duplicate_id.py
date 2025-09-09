def duplicate(n,s):
    # res=[]
    # for i in range(n+1):
    #     if s[i] not in res:
    #         res.append(s[i])
    #     elif s[i] in res:
    #         return s[i]
    
    
    
    # d=dict()
    # for i in s:
    #     if i in d:
    #         d[i]+=1
    #     else:
    #         d[i]=1
    # res=[k for k,v in d.items() if v>=2]
    # return ''.join(map(str,res))
    
    for i in range(1,n+1):
        if s.count(i)==2:
            return i
    
        

n=int(input())
s=list(map(int,input().split()))
print("the id that appears twice is",duplicate(n,s))