# )))()(((
# Not Balanced

# (())
# Balanced paranthesis
s=input()
c=0
f=0
for i in s:
    if i=='(':
        c+=1
    if i==')':
        c-=1
    if c<0:
        print("Not Balanced")
        f=1
        break
if f!=1:
    if c==0:
        print("Balanced paranthesis")
    else:
        print("Not Balanced")