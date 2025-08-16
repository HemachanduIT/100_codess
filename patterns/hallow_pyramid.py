#         *
#       *   *
#     *       *
#   *           *
# * * * * * * * * *

n=int(input())
for i in range(n):
#space
    for j in range(n-i-1):
        print(" ",end=" ")
#star
    a=2*i+1
    for j in range(a):
        if j==0 or j==a-1 or i==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
#space
    for j in range(n-i-1):
        print(" ",end=" ")
    print()
