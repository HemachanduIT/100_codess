# 10 20 10 30 10 20
# 10 3
# 20 2
# 30 1

# from collections import Counter
s=list(map(int,input().split()))
# d=Counter(s)
d=dict()
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
# print(d)
for k,v in d.items():
    print(k,v)

