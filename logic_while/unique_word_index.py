# input:
#     hello hello good morning good day awesome
# output:
#     3
s=list(map(str,input().split()))
d={}
for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
# print(d)
a=[k for k,v in d.items() if v==1]
res=a[0]
for i in range(len(s)):
    if s[i]==res:
        c=i
        break
print(c)
       