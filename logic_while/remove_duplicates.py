s=list(map(int,input().split()))
result=[]
for i in s:
    if i not in result:
        result.append(i)
print(result)