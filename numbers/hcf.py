a=int(input())
b=int(input())
n1,n2=a,b
while a!=b:
    if a>b:
        a-=b
    else:
        b-=a
print("the hcf of ",n1,"and",n2,"is",a)