# 36
# 60
# the gcd of 36 and  60 is 12

a,b=int(input()),int(input())
res1,res2=a,b
while a!=b:
    if a>b:
        a-=b
    else:
        b-=a
print("the gcd of",res1,"and ",res2,"is",a)
