#         *****
#       *****
#     *****
#   *****
# *****


n=int(input())
for i in range(n):
    a=n
    for j in range(i,a-1):
        print(" ",end=" ")
    a-=1
    for j in range(n):
        print("*",end="")
    print()