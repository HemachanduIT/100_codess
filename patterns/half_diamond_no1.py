# 4
# 2 
# 3 3
# 4 4 4
# 5 5 5 5
# 5 5 5 5
# 4 4 4
# 3 3
# 2


n=int(input())
a=3
for i in range(2*n):
    if i<n:
        for j in range(i+1):
            print(a-1,end=" ")
            if i==n-1:
                b=a-1
        a+=1
        # b=a
    else:
        for j in range(2*n-i):
            print(b,end=" ")
        b-=1
    print()