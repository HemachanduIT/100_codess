s1=input()
s2=input()
flag=True
for i in s1:
    if i not in s2:
        print("False")
        break
        flag=False
if flag:
    print("True")
    