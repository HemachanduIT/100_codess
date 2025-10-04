# input:
#     6
#    Avikel
# output:
#    3
n=int(input())
s=input()
c=0
v=['a','e','i','o','u','A','E','I','O','U']
for i in range(n):
    if s[i] not in v:
        c+=1
print(c)