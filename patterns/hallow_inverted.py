#  * * * * * * * * *   
#     *           *
#       *       *
#         *   *
#           *



n=int(input())
for i in range(n):
    #space
    for j in range(i+1):
        print(" ",end=" ")
    #star
    a=(2*(n-i))-1
    for j in range(a):
        if j==a-1 or j==0 or i==0:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    #space
    for j in range(i+1):
        print(" ",end=" ")
    print()