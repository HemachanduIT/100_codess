# 4
# 3 3 3 
# 3 1 3
# 3 2 3
# 3 3 3

n=int(input())
a=1
for i in range(n):
    for j in range(n-1):
        if i==0 or i==n-1 or j==0 or j==n-2:
            print(n-1,end=" ")
        else:
            print(a,end=" ")
            a+=1
    print()