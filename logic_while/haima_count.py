# input:
#     aA
# aaAAbvau
# output:
#     5
s1=set(input())
s2=input()
c=0
for i in s2:
    if i in s1:
        c+=1
print(c)        
