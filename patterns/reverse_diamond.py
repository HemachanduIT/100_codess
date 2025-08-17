# 4
#       * 
#     * *
#   * * *
# * * * *
#   * * *
#     * *
#       *



n=int(input())
for i in range(2*n-1):
    if i<n:
        for j in range(n-i-1):
            print(" ",end=" ")
        for j in range(i+1):
            print("*",end=" ")
    else:
        for j in range(i-n+1):
            print(" ",end=" ")
        for j in range(2*n-i-1):
            print("*",end=" ")
    print()
    