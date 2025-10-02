s1,s2=input(),input()
c=0
for i in s1:
    if i not in s2:
        c+=1
for i in s2:
    if i not in s1:
        c+=1
print(c)
