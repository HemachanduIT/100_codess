# 3
# 3 0 1
# the missing no in the serires is 2


n=int(input())
s=list(map(int,input().split()))
# a=[]
for i in range(n+1):
    if i not in s:
        # a.append(i)
        print("the missing no in the serires is",i)
    else:
        continue
# print(*a)