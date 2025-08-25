n=int(input())
a=3
for i in range(1,2*n+1):
    if i<=n:
        c=1
        for j in range(1,i+1):
            if j==1:
                k=a-1
            print(a-1,end=" ")
            a-=1
            c+=1
        a=k+c+1
    else:
        if i==n+1:
            
            b=a-2*i
        # print(a)
        # d=b
        for j in range(2*n-i):
            print(b,end=" ")
            b-=1
            
            
    print()