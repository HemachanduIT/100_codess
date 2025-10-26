import copy
s=list(map(int,input().split()))
a=s.copy()
s.sort()
# print(a)
# print(s)

if a==s:
    print("True")
else:
    print("False")