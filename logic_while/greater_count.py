def greatercount(n,s):
    res=[]
    for i in range(n):
        c=0
        maxx=s[i]
        for j in range(n):
            # maxx=s[i]
            if maxx>s[j]:
                c+=1
        res.append(c)
    return ' '.join(map(str,res))
n=int(input())
s=list(map(int,input().split()))
print(greatercount(n,s))