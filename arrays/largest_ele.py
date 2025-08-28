# 10 20 30 5
# the max ele in list is 30


s=list(map(int,input().split()))
m=s[0]
for i in s:
    if i>m:
        m=i
print("the max ele in list is",m)


# print("the max ele in list is",max(s))

# s.sort()
# print("the max ele in list is",s[-1])