# 12
# 14
# the lcm of  12 and 14 is 84


a,b=int(input()),int(input())
num1,num2=a,b
while a!=b:
    if a>b:
        a-=b
    else:
        b-=a
hcf=a
lcm=num1*num2//hcf
print("the lcm of ",num1,'and',num2,"is",lcm)
