# 4
# 6 6 6 6 
# 5 5 5
# 4 4
# 3

n=int(input())
a=3
c=0
for i in range(1,a+1):
    c+=i

for i in range(n):
    for j in range(n-i):
        print(c,end=" ")
    c-=1
    print()