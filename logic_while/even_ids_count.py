def even_count(n,s):
    res=0
    for i in range(n):
        if len(str(s[i]))%2==0:
            res+=1
        
    return res
n=int(input())
s=list(map(int,input().split()))
print(even_count(n,s))