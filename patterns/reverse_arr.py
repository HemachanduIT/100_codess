# 1 2 3 4
# the reverse of arr is 4 3 2 1

import math
s=list(map(int,input().split()))
# s.reverse()
# print(*s)
# print(*s[::-1])
a=[]
for i in reversed(range(len(s))):
    a.append(s[i])
print("the reverse of arr is",*a)