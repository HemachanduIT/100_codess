# 10, 20, 40, 30, 50, 20, 10, 20
# [10, 20]


from collections import Counter
s=list(map(int,input().split(",")))
d=Counter(s)
res=[k for k,v in d.items() if v>1]
print(res)