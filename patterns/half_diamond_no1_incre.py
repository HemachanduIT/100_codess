n=int(input())
a=3

for i in range(2*n):
    if i<n:
        for j in range(i+1):
            print(a-1,end=" ")
            a+=1
            if i==n-2:
                b=a-1
    else:
        k=b
        c=-1
        for j in range(2*n-i):
            print(b,end=" ")
            b+=1
            c+=1
        b=k-c
    print()