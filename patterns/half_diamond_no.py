# 5
# 3
# 44
# 555
# 6666
# 77777
# 6666
# 555
# 44
# 3


n=int(input())
a=3
for i in range(2*n):
    if i<n:
        for j in range(i+1):
            print(a,end="")
        a+=1
    else:
        for j in range(2*n-i-1):
            print(a-2,end="")
        a-=1
    
    print()