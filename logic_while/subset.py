
# 1 2
# 1 2 3 4 
# True

s1=input()
s2=input()
flag=True
for i in s1:
    if i not in s2:
        print("False")
        flag=False
        break
if flag:
    print("s1 is subset of s2")
else:
    print("s1 is not a subset of s2")