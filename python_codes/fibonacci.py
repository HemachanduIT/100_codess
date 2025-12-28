n1,n2=0,1
print(n1,n2,end=' ')
s=0
for i in range(2,11):
    s=n1+n2
    print(s,end=' ')
    n1=n2
    n2=s
    # print()