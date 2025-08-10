n1=int(input())
n2=int(input())
n3=int(input())
l1=n1 if n1>n2 else n2
l2=l1 if l1>n3 else n3
print(l2,"is greatest")