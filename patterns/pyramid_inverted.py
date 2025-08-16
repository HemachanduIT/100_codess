    # * * * * * * * * *     
    #   * * * * * * *
    #     * * * * *
    #       * * *
    #         *



n=int(input())
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