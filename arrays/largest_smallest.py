# 5 4 8 29 262 1 
# the largest no is 262
# the smallest no is 1 

s=list(map(int,input().split()))
lar,small=s[0],s[0]
for i in s:
    if i>lar:
        lar=i
    if i<small:
        small=i


# s.sort()
# print("the smallest no is",s[0])
# print("the largest no is",s[-1])


print("the smallest no is",small)
print("the largest no is",lar)
