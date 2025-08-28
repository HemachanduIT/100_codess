# 1 3 4 -2
# the smallest element from the list is -2


s=list(map(int,input().split()))
# m=s[0]
# for i in s:
#     if i<m:
#         m=i
# print("the smallest element from the list is",m)


# print("the smallest element from the list is",min(s))

s.sort()
print("the smallest element from the list is",s[0])