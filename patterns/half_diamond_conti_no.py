# 4
# 3 
# 4 5
# 6 7 8
# 9 10 11 12
# 6 7 8
# 4 5
# 3




n=int(input())
a=3
for i in range(2*n):
    if i<n:
        
        for j in range(i+1):
            print(a,end=" ")
            a+=1
            if i==n-3:
                b=a
    else:
        # print(b)
        for j in range(2*n-i-1):
            print(b,end=" ")
            b+=1
        b=2*n-i
    print()
