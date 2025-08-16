    #       *
    #     * * *
    #   * * * * *
    # * * * * * * *
    # * * * * * * *
    #   * * * * *
    #     * * *
    #       *


n=int(input())
for i in range(n):
    #space
    for j in range(n-i+1):
        print(" ",end=" ")
    #star
    for j in range(2*i+1):
        print("*",end=" ")
    #space
    for j in range(n-i+1):
        print(" ",end=" ")
    print()
# n=int(input())
for i in range(n):
    #spaces
    for j in range(i+2):
        print(" ",end=" ")
    #stars
    for j in range((2*(n-i))-1):
        print("*",end=" ")
    #spaces
    for j in range(i+2):
        print(" ",end=" ")
    print()     
