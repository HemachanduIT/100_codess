s=list(map(int,input().split()))
res=[]
for i in s:
    if i not in res:
        res.append(i)
print(res)