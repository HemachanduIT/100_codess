# 4
# 3 
# 4 5
# 6 7 8
# 9 10 11 12


n=int(input())
a=n
for i in range(n):
    for j in range(i+1):
        print(a-1,end=" ")
        a+=1
    print()