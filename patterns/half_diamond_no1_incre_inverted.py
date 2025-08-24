# 4
# 3 
# 5 4
# 8 7 6
# 12 11 10 9
# 8 7 6
# 5 4
# 3


n=int(input())
a=3
for i in range(1,2*n+1):
    # c=1
    if i<=n:
        c=1
        # k=0
        for j in range(1,i+1):
            print(a,end=" ")
            if j==1:
                k=a
                # print(k)
            a-=1
            c+=1
        a=k+c
    else:
        # print(a)
        if i==n+1:
            c=a-i-n
        for j in range(1,2*n-i+1):
            print(c,end=" ")
            c-=1
        
    print()