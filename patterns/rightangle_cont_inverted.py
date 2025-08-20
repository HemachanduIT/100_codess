# 5
# 15 14 13 12 11 
# 10 9 8 7
# 6 5 4
# 3 2
# 1

n=int(input())
a=0
for i in range(n,0,-1):
    a+=i
for i in range(n):
    for j in range(n-i):
        print(a,end=" ")
        a-=1
    print()
