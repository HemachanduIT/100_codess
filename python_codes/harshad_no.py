n=int(input())
s=0
for i in str(n):
    s+=int(i)
if n%s==0:
    print("harshad no")
else:
    print("not a harshad no")