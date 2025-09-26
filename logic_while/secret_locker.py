# input:
#     4
#     921 34 78965 5
# output:
#     949

# def secretLocker(n,s):
#     res=''
#     for i in range(n):
#         r=s[i]
#         z=str(r)
#         if i<len(z):
#             res+=z[i]              
#     return res
n=int(input())
s=list(map(str,input().split()))
# print(secretLocker(n,s))
# print(s[0][0])
res=''
for i in range(n):
    if i<len(s[i]):
        res+=s[i][i]
print(res)