# 36
# 60
# the gcd of 36 and  60 is 12

a,b=int(input()),int(input())
n1,n2=a,b
while a!=b:
    if a>b:
        a-=b
    else:
        b-=a
print("the gcd of",n1,"and ",n2,"is",a)
