# 4
# 3 
# 4 4
# 5 5 5
# 6 6 6 6


n=int(input())
a=n
for i in range(n):
    for j in range(i+1):
        print(a-1,end=" ")
    a+=1
    print()