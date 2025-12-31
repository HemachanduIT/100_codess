# 36
# 60
# the gcd of 36 and  60 is 12

a,b=int(input()),int(input())
result1,result  2=a,b
while a!=b:
    if a>b:
        a-=b
    else:
        b-=a
print("the gcd of",result1,"and ",result2,"is",a) 

