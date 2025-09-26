def max_repeated(n,s):
    d={}
    for i in s:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    maxx=max(d.values())
    res=[k for k,v in d.items() if v==maxx]
    return min(res)
    
n=int(input())
s=list(map(str,input().lower().split()))
print(max_repeated(n,s))