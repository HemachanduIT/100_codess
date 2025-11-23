# input
# 5
# 10 20 30 40 50
# 1 3
# 30

# output
# [10, 40, 30, 20, 50] YES [50, 20, 30, 40, 10]

n=int(input())
s=list(map(int,input().split()))
loc1,loc2=map(int,input().split())
key=int(input())
result=''
if loc1<len(s) and loc2<len(s):
    s[loc1],s[loc2]=s[loc2],s[loc1]
# print(s)
if key in s:
    result='YES'

print(s,result,s[::-1])