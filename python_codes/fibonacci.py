a,b=0,1
print(a,b,end=' ')
s=0
for i in range(2,11):
    s=a+b
    print(s,end=' ')
    a=b
    b=s
    # print()