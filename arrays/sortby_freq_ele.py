# 10 20 20 20 10 50 50 
# [20, 20, 20, 10, 10, 50, 50]


from collections import Counter
s=list(map(int,input().split()))
d=Counter(s)
arr=sorted(s,key=lambda x:(-d[x],x))
print(arr)