# 12
# 14
# the lcm of  12 and 14 is 84


a,b=int(input()),int(input())
n1,n2=a,b
while a!=b:
    if a>b:
        a-=b
    else:
        b-=a
hcf=a
lcm=n1*n2//hcf
print("the lcm of ",n1,'and',n2,"is",lcm)
