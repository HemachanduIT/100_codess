# n=int(input())
n1=int(input())
n2=int(input())
for i in range(n1,n2+1):
    c=0
    for j in range(n1,i+1):
        if i%j==0:
            c+=1
    if c==2:
        print("prime no's are :",i)
